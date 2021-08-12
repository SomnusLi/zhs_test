import pytest
import os
import allure
from api.user.user import user
from common.read_data import data
from common.logger import logger
import time
from ruamel import yaml
import selenium
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

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


# 注释部分为数据库数据清理
# @allure.step("前置步骤 ==>> 清理数据")
# def step_first():
#     logger.info("******************************")
#     logger.info("前置步骤开始 ==>> 清理数据")
#
#
# @allure.step("后置步骤 ==>> 清理数据")
# def step_last():
#     logger.info("后置步骤开始 ==>> 清理数据")
#
#
# @allure.step("前置步骤 ==>> 管理员用户登录")
# def step_login(username, password):
#     logger.info("前置步骤 ==>> 管理员 {} 登录，返回信息 为：{}".format(username, password))
@allure.step("前置步骤 ==>> 用户登录")
def step_login(account, password):
    logger.info("前置步骤 ==>> 用户 {} 登录，返回信息 为：{}".format(account, password))


#
#
# @pytest.fixture(scope="session")
# def login_fixture():
#     username = base_data["init_admin_user"]["username"]
#     password = base_data["init_admin_user"]["password"]
#     header = {
#         "Content-Type": "application/x-www-form-urlencoded"
#     }
#     payload = {
#         "username": username,
#         "password": password
#     }
#     loginInfo = user.login(data=payload, headers=header)
#     step_login(username, password)
#     yield loginInfo.json()
@pytest.fixture(scope="session")
def login_fixture_student():
    account = base_data["init_user_login_student"]["account"]
    password = base_data["init_user_login_student"]["password"]
    payload = {
        "account": account,
        "password": password
    }
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    cookies = {"Hm_lvt_0a1b7151d8c580761c3aef32a3d501c6": "{}".format(int(time.time())),
               "Hm_lpvt_0a1b7151d8c580761c3aef32a3d501c6": "{}".format(int(time.time())), "source": "-1"}
    login_info = user.login(data=payload, headers=header, cookies=cookies)
    step_login(account, password)
    yield login_info


@pytest.fixture(scope="session")
def login_fixture_teacher():
    account = base_data["init_user_login_teacher"]["account"]
    password = base_data["init_user_login_teacher"]["password"]
    uuid = base_data["init_user_login_teacher"]["uuid"]
    #
    # payload = {
    #     "account": account,
    #     "password": password
    # }
    # header = {
    #     "Content-Type": "application/x-www-form-urlencoded"
    # }
    # cookies = {"Hm_lvt_0a1b7151d8c580761c3aef32a3d501c6": "{}".format(int(time.time())),
    #            "Hm_lpvt_0a1b7151d8c580761c3aef32a3d501c6": "{}".format(int(time.time())), "source": "-1"}
    # login_info = user.login(data=payload, headers=header, cookies=cookies)
    # step_login(account, password)
    # yield login_info
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
            # logger.info(
            #     "保存的cookies中时间为：{}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(cookies_time))))
            # logger.info("现在的时间：{}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now_time))))
            now_time_change = time.strftime("%Y-%m-%d", time.localtime(now_time))
            cookies_time_change = time.strftime("%Y-%m-%d", time.localtime(cookies_time))
            logger.info(
                "保存的cookies中时间为：{}".format(cookies_time_change))
            logger.info("现在的时间：{}".format(now_time_change))
            days_diff = (now_time - cookies_time) / 3600 / 24
            logger.info("相差天数{}".format(days_diff))
            if now_time_change > cookies_time_change:
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
        browser.find_element_by_xpath("//*[@id='lUsername']").send_keys(account)
        time.sleep(1)
        browser.find_element_by_xpath("//*[@id='lPassword']").clear()
        browser.find_element_by_xpath("//*[@id='lPassword']").send_keys(password)
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
        time.sleep(10)
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
    login_fixture_teacher.uuid = uuid
    login_fixture_teacher.cookies = cookies
    login_fixture_teacher.account = account
    return login_fixture_teacher


@pytest.fixture(scope="session")
def login_fixture_teacher_app():
    account = base_data["init_user_login_teacher"]["account"]
    password = base_data["init_user_login_teacher"]["password"]

    data = {
        "account": account,
        "password": password,
        "clientType": 1,
        "appVersion": "4.4.8"
    }
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Connection": "Keep-Alive",
        "Content-Length": "67",
        "Host": "appteacher.zhihuishu.com"
    }
    login_info_app = user.zhs_app_login(data=data, headers=header)
    step_login(account, password)
    yield login_info_app
#
# @pytest.fixture(scope="function")
# def insert_delete_user():
#     """删除用户前，先在数据库插入一条用户数据"""
#     insert_sql = base_data["init_sql"]["insert_delete_user"][0]
#     db.execute_db(insert_sql)
#     step_first()
#     logger.info("删除用户操作：插入新用户--准备用于删除用户")
#     logger.info("执行前置SQL：{}".format(insert_sql))
#     yield
#     # 因为有些情况是不给删除管理员用户的，这种情况需要手动清理上面插入的数据
#     del_sql = base_data["init_sql"]["insert_delete_user"][1]
#     db.execute_db(del_sql)
#     step_last()
#     logger.info("删除用户操作：手工清理处理失败的数据")
#     logger.info("执行后置SQL：{}".format(del_sql))
#
#
# @pytest.fixture(scope="function")
# def delete_register_user():
#     """注册用户前，先删除数据，用例执行之后，再次删除以清理数据"""
#     del_sql = base_data["init_sql"]["delete_register_user"]
#     db.execute_db(del_sql)
#     step_first()
#     logger.info("注册用户操作：清理用户--准备注册新用户")
#     logger.info("执行前置SQL：{}".format(del_sql))
#     yield
#     db.execute_db(del_sql)
#     step_last()
#     logger.info("注册用户操作：删除注册的用户")
#     logger.info("执行后置SQL：{}".format(del_sql))
#
#
# @pytest.fixture(scope="function")
# def update_user_telephone():
#     """修改用户前，因为手机号唯一，为了使用例重复执行，每次需要先修改手机号，再执行用例"""
#     update_sql = base_data["init_sql"]["update_user_telephone"]
#     db.execute_db(update_sql)
#     step_first()
#     logger.info("修改用户操作：手工修改用户的手机号，以便用例重复执行")
#     logger.info("执行SQL：{}".format(update_sql))
