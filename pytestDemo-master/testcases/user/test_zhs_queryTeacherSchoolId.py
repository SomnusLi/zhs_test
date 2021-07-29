import pytest
import allure

from operation.user.getLoginInfo import queryTeacherSchoolId
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
class Test_queryTeacherSchoolId():
    """获取教师学校ID"""

    @allure.story("获取教师学校ID")
    @allure.description("获取教师学校ID")
    @allure.issue("https://passport.zhihuishu.com/user/validateAccountAndPassword", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://passport.zhihuishu.com/user/validateAccountAndPassword", name="点击，跳转到对应用例的链接地址")
    @allure.title("获取教师学校ID")
    def test_zhs_queryTeacherSchoolId(self, login_fixture_teacher):
        logger.info("*************** 开始执行用例 ***************")
        # login_fixture前置登录
        user_info = login_fixture_teacher
        uuid = user_info.json().get("uuid")
        account = user_info.request.body[8:19]
        password = user_info.request.body[29:37]
        step_login(account, uuid)
        cookies = add_cookies(requests.utils.dict_from_cookiejar(user_info.cookies))
        logger.info("queryTeacherSchoolId")
        result_queryTeacherSchoolId = queryTeacherSchoolId(uuid, cookies=cookies)
        assert result_queryTeacherSchoolId.response.status_code == 200
        logger.info("code ==>> 老师学校：{}".format(result_queryTeacherSchoolId.response.json().get("result")))
        # assert result.response.json().get("status") == except_status
        # assert set(six.viewitems(except_msg)).issubset(set(six.viewitems(result.msg)))
        logger.info("*************** 结束执行用例 ***************")

    # @allure.story("获取某个用户信息")
    # @allure.description("该用例是针对获取单个用户信息接口的测试")
    # @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    # @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    # @allure.title("【 {username}，{except_result}，{except_code}，{except_msg} 】")
    # @pytest.mark.single
    # @pytest.mark.parametrize("username, except_result, except_code, except_msg",
    #                          api_data["test_get_get_one_user_info"])


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_zhs_queryTeacherSchoolId.py"])
