import pytest
import allure

from operation.user.aidMenuAuth import aidMenuAuth
from testcases.conftest import api_data
from common.logger import logger
from common.filedValueGenerate import add_cookies
import requests


@allure.step("前置登录步骤 ==>> 用户登录")
def step_login(account, uuid):
    logger.info("前置登录步骤 ==>> 用户 {} 登录 ==>> 返回的 uuid 为：{}".format(account, uuid))


@allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("用户模块")
@allure.feature("获取用户信息")
class Test_aidMenuAuth():
    """获取用户权限"""

    @allure.story("获取用户权限")
    @allure.description("获取用户权限")
    @allure.issue("https://www.zhihuishu.com/", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.zhihuishu.com/", name="点击，跳转到对应用例的链接地址")
    @allure.title("获取用户权限")
    def test_zhs_aidMenuAuth(self, login_fixture_teacher):
        logger.info("*************** 开始执行用例 ***************")
        # login_fixture前置登录
        user_info = login_fixture_teacher
        uuid = user_info.uuid
        account = user_info.account
        cookies = user_info.cookies
        step_login(account, uuid)
        result = aidMenuAuth(uuid, cookies=cookies)
        assert result.response.status_code == 200
        logger.info("code ==>> 实际结果：{}".format(result.response.json().get("status")))
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_zhs_aidMenuAuth.py"])
