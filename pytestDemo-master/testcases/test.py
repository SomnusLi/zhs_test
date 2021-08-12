import pytest
import os
import allure
from api.user.user import user
from common.read_data import data
from common.logger import logger
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from ruamel import yaml

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def get_data(yaml_file_name):
    try:
        data_file_path = os.path.join(BASE_PATH, "data", yaml_file_name)
        yaml_data = data.load_yaml(data_file_path)
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        return yaml_data


base_data = get_data("base_data.yml")
api_data = get_data("api_test_data.yml")
scenario_data = get_data("scenario_test_data.yml")


class Test_test():
    @pytest.mark.skip
    def test_test(self):
        cookies_data = get_data("cookies_test_data.yml")
        logger.info(cookies_data)
        is_cookies_expired = False
        if cookies_data == None:
            logger.info("文件无内容")
            is_cookies_expired = True
        else:
            cookies_time = cookies_data["datatime"]
            now_time = int(round(time.time()))
            if cookies_time != None:
                logger.info("cookies_time:{},now_time:{}".format(cookies_time, now_time))
                logger.info(
                    "保存的cookies中时间为：{}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(cookies_time))))
                logger.info("现在的时间：{}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now_time))))
                days_diff = (now_time - cookies_time) / 3600 / 24
                logger.info("相差天数{}".format(days_diff))
                if days_diff > 0:
                    is_cookies_expired = True
                elif cookies_data["cookies"] == None:
                    is_cookies_expired = True
                else:
                    cookies = {}
                    for key in cookies_data["cookies"]:
                        cookies[key] = cookies_data["cookies"][key]
            else:
                is_cookies_expired = True
        if is_cookies_expired:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chromedriver_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
                                             "config\chromedriver.exe")
            logger.info(chromedriver_path)
            logger.info(chrome_options)
            browser = webdriver.Chrome(chromedriver_path, options=chrome_options)
            browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                "source": """
                Object.defineProperty(navigator, 'webdriver', {
                  get: () => undefined
                })
              """
            })
            browser.get(
                "https://passport.zhihuishu.com/login?service=https://onlineservice.zhihuishu.com/login/gologin")
            try:
                t = browser.find_element_by_class_name("waf-nc-title").get_attribute("textContent")
                logger.info(t)
                if t == "安全验证":
                    logger.info("需要安全验证")
                    move_element = browser.find_element_by_xpath("//*[@id='nc_1_n1z']")
                    logger.info("按住滑块")
                    ActionChains(browser).click_and_hold(on_element=move_element).perform()
                    time.sleep(3)
                    # 滑块x轴距离根据屏幕分辨率调整
                    ActionChains(browser).move_to_element_with_offset(to_element=move_element, xoffset=300,
                                                                      yoffset=0).perform()
                    logger.info("滑块滑到最右侧")
                    ActionChains(browser).release(on_element=move_element).perform()
                else:
                    logger.info("没有找到登录验证元素，无需登录验证")
            except:
                logger.info("无需登录验证")
            time.sleep(3)
            browser.find_element_by_xpath("//*[@id='lUsername']").clear()
            browser.find_element_by_xpath("//*[@id='lUsername']").send_keys("13122285260")
            time.sleep(1)
            browser.find_element_by_xpath("//*[@id='lPassword']").clear()
            browser.find_element_by_xpath("//*[@id='lPassword']").send_keys("Aa111111")
            time.sleep(1)
            browser.find_element_by_xpath("//*[@id='f_sign_up']/div[1]/span").click()
            try:
                t = browser.find_element_by_class_name("waf-nc-title").get_attribute("textContent")
                logger.info(t)
                if t == "安全验证":
                    logger.info("需要安全验证")
                    move_element = browser.find_element_by_xpath("//*[@id='nc_1_n1z']")
                    ActionChains(browser).click_and_hold(on_element=move_element).perform()
                    logger.info("按住滑块")
                    time.sleep(3)
                    # 滑块x轴距离根据屏幕分辨率调整
                    ActionChains(browser).move_to_element_with_offset(to_element=move_element, xoffset=300,
                                                                      yoffset=0).perform()
                    logger.info("滑块滑到最右侧")
                    ActionChains(browser).release(on_element=move_element).perform()
                else:
                    logger.info("没有找到登录验证元素，无需登录验证")
            except:
                logger.info("无需登录验证")

            browser.get("https://appcomm-user.zhihuishu.com/app-commserv-user/userInfo/checkNeedAuth")
            time.sleep(20)
            request_log = browser.get_log('performance')
            logger.info(request_log)
            list_cookies = browser.get_cookies()
            cookies = {}
            for s in list_cookies:
                cookies[s["name"]] = s["value"]
            browser.quit()
            cookies_data = {
                "cookies": cookies,
                "account": 13122285260,
                "datatime": int(round(time.time()))
            }
            yamlpath = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
                                    "data\\cookies_test_data.yml")
            with open(yamlpath, "w", encoding="utf-8") as f:
                yaml.dump(cookies_data, f, Dumper=yaml.RoundTripDumper)
        logger.info(cookies)
        return cookies


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test.py"])
