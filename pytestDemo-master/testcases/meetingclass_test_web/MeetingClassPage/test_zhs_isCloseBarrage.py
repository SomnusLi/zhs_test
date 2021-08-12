import pytest
import allure
from operation.course.course import *
from operation.meetingclass.meetingclass import *
from operation.user.getLoginInfo import queryTeacherSchoolId
from testcases.conftest import api_data
from common.logger import logger
from common.filedValueGenerate import add_cookies, randomRangeNum
import requests


@allure.step("前置登录步骤 ==>> 用户登录")
def step_login(account, uuid):
    logger.info("前置登录步骤 ==>> 用户 {} 登录 ==>> 返回的 uuid 为：{}".format(account, uuid))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("见面课模块")
@allure.feature("web教师端")
class Test_isCloseBarrage():
    """查询弹幕是否关闭"""

    @allure.story("见面课信息")
    @allure.description("查询弹幕是否关闭")
    @allure.title("查询弹幕是否关闭")
    @pytest.mark.single
    def test_zhs_isCloseBarrage(self, login_fixture_teacher):
        logger.info("*************** 开始执行用例 ***************")
        # login_fixture前置登录
        user_info = login_fixture_teacher
        uuid = user_info.uuid
        account = user_info.account
        step_login(account, uuid)
        cookies = user_info.cookies
        logger.info("getStartingMeetCourseList")
        result_onlineservice_getStartingMeetCourseList = onlineservice_getStartingMeetCourseList(uuid, cookies=cookies)
        assert result_onlineservice_getStartingMeetCourseList.response.status_code == 200
        if result_onlineservice_getStartingMeetCourseList.response.json()["rt"] != []:
            logger.info("有正在开启的见面课")
            meetCourseId = result_onlineservice_getStartingMeetCourseList.response.json()["rt"][0]["meetCourseId"]
            logger.info("isCloseBarrage")
            result_isCloseBarrage = isCloseBarrage(meetCourseId, uuid, cookies=cookies)
            assert result_isCloseBarrage.response.status_code == 200
            if result_isCloseBarrage.response.json()["rt"]:
                logger.info("老师已开启答疑")
            else:
                logger.info("老师未开启答疑")
        else:
            logger.info("没有正在开启的见面课")
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_zhs_isCloseBarrage.py"])
