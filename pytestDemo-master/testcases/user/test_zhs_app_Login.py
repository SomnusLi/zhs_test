import pytest
import allure

from operation.user.login import zhs_app_login
from testcases.conftest import api_data
from common.logger import logger


@allure.step("步骤1 ==>> 登录")
def step_1():
    logger.info("步骤1 ==>> 登录")


# @allure.step("步骤1 ==>> 获取某个用户信息")
# def step_2(username):
#     logger.info("步骤1 ==>> 获取某个用户信息：{}".format(username))


@allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("针对单个接口的测试")
@allure.feature("获取用户信息模块")
class Test_login():
    """app用户登录"""

    @allure.story("用例--app用户登录")
    @allure.description("该用例app用户登录")
    @allure.issue("https://passport.zhihuishu.com/user/validateAccountAndPassword", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://passport.zhihuishu.com/user/validateAccountAndPassword", name="点击，跳转到对应用例的链接地址")
    @pytest.mark.single
    @pytest.mark.parametrize("account,password", api_data["test_zhs_app_login"])
    def test_zhs_login(self, account, password):
        logger.info("*************** 开始执行用例 ***************")
        # step_1()
        result_zhs_app_login = zhs_app_login(account, password)
        assert result_zhs_app_login.response.status_code == 200
        if result_zhs_app_login.response.status_code == 200:
            logger.info(result_zhs_app_login.response.json()["rt"])
            logger.info("账户的access_token为{}".format(result_zhs_app_login.response.json()["rt"]["access_token"]))
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_zhs_Login.py"])
