import pytest
import os
import allure
from api.user.user import user
from common.read_data import data
from common.logger import logger
import time
from selenium import webdriver
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
                if days_diff > 1:
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
            browser.get(
                "https://passport.zhihuishu.com/login?service=https://onlineservice.zhihuishu.com/login/gologin")
            time.sleep(3)
            browser.find_element_by_xpath("//*[@id='lUsername']").send_keys("13122285260")
            time.sleep(1)
            browser.find_element_by_xpath("//*[@id='lPassword']").send_keys("Aa111111")
            time.sleep(1)
            browser.find_element_by_xpath("//*[@id='f_sign_up']/div[1]/span").click()
            time.sleep(3)
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
