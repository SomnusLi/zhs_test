import pytest
import allure
import os
from operation.user.login import zhs_login
from testcases.conftest import api_data
from common.logger import logger
from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("用户模块")
@allure.feature("用户登录测试")
class Test_seleniumlogintest():
    """selenium用户登录"""

    @allure.story("selenium用户登录")
    @allure.description("selenium用户登录")
    @allure.issue("https://passport.zhihuishu.com/user/validateAccountAndPassword", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://passport.zhihuishu.com/user/validateAccountAndPassword", name="点击，跳转到对应用例的链接地址")
    @allure.title("selenium用户登录")
    @pytest.mark.skip()
    def test_zhs_seleniumlogintest(self):
        logger.info("*************** 开始执行用例 ***************")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--incognito")
        chromedriver_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                                         "config\chromedriver.exe")
        logger.info(chromedriver_path)
        logger.info(chrome_options)
        browser = webdriver.Chrome(chromedriver_path, options=chrome_options)
        browser.get("https://passport.zhihuishu.com/login?service=https://onlineservice.zhihuishu.com/login/gologin")
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
        logger.info(cookies)
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_zhs_seleniumlogintest.py"])
