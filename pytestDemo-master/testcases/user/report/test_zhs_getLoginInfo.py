import pytest
import allure

from operation.user.getLoginInfo import getLoginInfo
from testcases.conftest import api_data
from common.logger import logger
import requests


@allure.step("前置登录步骤 ==>> 用户登录")
def step_login(account, uuid):
    logger.info("前置登录步骤 ==>> 用户 {} 登录 ==>> 返回的 uuid 为：{}".format(account, uuid))


@allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("针对单个接口的测试")
@allure.feature("获取用户信息模块")
class TestzhsLogin():
    """获取用户权限"""

    @allure.story("用例--获取用户权限")
    @allure.description("获取用户权限")
    @allure.issue("https://passport.zhihuishu.com/user/validateAccountAndPassword", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://passport.zhihuishu.com/user/validateAccountAndPassword", name="点击，跳转到对应用例的链接地址")
    def test_zhs_getLoginInfo(self, login_fixture):
        logger.info("*************** 开始执行用例 ***************")
        # login_fixture前置登录
        user_info = login_fixture
        uuid = user_info.json().get("uuid")
        account = user_info.request.body[8:19]
        step_login(account, uuid)
        # cookies要传str类型
        result = getLoginInfo(requests.utils.dict_from_cookiejar(user_info.cookies))
        assert result.response.status_code == 200
        logger.info("code ==>> 实际结果：{}".format(result.response.json().get("status")))
        # assert result.response.json().get("status") == except_status
        # assert set(six.viewitems(except_msg)).issubset(set(six.viewitems(result.msg)))
        logger.info("*************** 结束执行用例 ***************")

    # @allure.story("用例--获取某个用户信息")
    # @allure.description("该用例是针对获取单个用户信息接口的测试")
    # @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    # @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    # @allure.title("测试数据：【 {username}，{except_result}，{except_code}，{except_msg} 】")
    # @pytest.mark.single
    # @pytest.mark.parametrize("username, except_result, except_code, except_msg",
    #                          api_data["test_get_get_one_user_info"])


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_zhs_aidMenuAuth.py"])

# https://appcomm-user.zhihuishu.com/app-commserv-user/userInfo/checkNeedAuth