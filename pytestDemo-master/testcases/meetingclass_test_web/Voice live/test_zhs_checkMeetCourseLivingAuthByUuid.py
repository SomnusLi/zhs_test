import pytest
import allure
from operation.course.course import get_courseInfo_teacher
from operation.meetingclass.meetingclass import checkMeetCourseLivingAuthByUuid
from testcases.conftest import api_data
from common.logger import logger
from common.filedValueGenerate import add_cookies
import requests


@allure.step("前置登录步骤 ==>> 用户登录")
def step_login(account, uuid):
    logger.info("前置登录步骤 ==>> 用户 {} 登录 ==>> 返回的 uuid 为：{}".format(account, uuid))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("见面课模块")
@allure.feature("web教师端")
class Test_checkMeetCourseLivingAuthByUuid():
    """查询老师是否进行了直播认证"""

    @allure.story("见面课直播")
    @allure.description("查询老师是否进行了直播认证")
    @allure.issue("https://www.zhihuishu.com/", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.zhihuishu.com/", name="点击，跳转到对应用例的链接地址")
    @allure.title("查询老师是否进行了直播认证")
    @pytest.mark.single
    def test_zhs_checkMeetCourseLivingAuthByUuid(self, login_fixture_teacher):
        logger.info("*************** 开始执行用例 ***************")
        # login_fixture前置登录
        user_info = login_fixture_teacher
        uuid = user_info.uuid
        account = user_info.account
        step_login(account, uuid)
        cookies = user_info.cookies
        result_checkMeetCourseLivingAuthByUuid = checkMeetCourseLivingAuthByUuid(uuid,
                                                                                 cookies=cookies)
        assert result_checkMeetCourseLivingAuthByUuid.response.status_code == 200
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_zhs_checkMeetCourseLivingAuthByUuid.py"])
