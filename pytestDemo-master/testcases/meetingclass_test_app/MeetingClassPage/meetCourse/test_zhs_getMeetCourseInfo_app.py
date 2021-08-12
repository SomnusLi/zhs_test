import pytest
import allure
from operation.course.course import get_courseInfo_teacher
from operation.meetingclass.meetingclass import *
from testcases.conftest import api_data
from common.logger import logger
from common.filedValueGenerate import add_cookies
import requests


@allure.step("前置登录步骤 ==>> 用户登录")
def step_login(account, uuid):
    logger.info("前置登录步骤 ==>> 用户 {} 登录 ==>> 返回的 uuid 为：{}".format(account, uuid))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("见面课模块")
@allure.feature("app教师端")
class Test_getMeetCourseInfo_app():
    """app查询正在进行中的见面课信息"""

    @allure.story("见面课信息")
    @allure.description("app查询正在进行中的见面课信息")
    @allure.title("app查询正在进行中的见面课信息")
    @pytest.mark.single
    def test_zhs_getMeetCourseInfo_app(self, login_fixture_teacher_app):
        logger.info("*************** 开始执行用例 ***************")
        # login_fixture前置登录
        user_info_app = login_fixture_teacher_app
        uuid = user_info_app.json()["rt"]["loginInfo"]["uuId"]
        account = user_info_app.request.body[8:19]
        access_token = user_info_app.json()["rt"]["access_token"]
        step_login(account, uuid)
        logger.info("getStartingMeetCourseList_app")
        result_getStartingMeetCourseList_app = getStartingMeetCourseList_app(access_token, uuid)
        assert result_getStartingMeetCourseList_app.response.status_code == 200
        if result_getStartingMeetCourseList_app.response.json()["rt"] != []:
            logger.info("有正在开启的见面课")
            meetCourseId = result_getStartingMeetCourseList_app.response.json()["rt"][0]["meetCourseId"]
            role = 1
            logger.info("getMeetCourseInfo_app")
            result_getMeetCourseInfo_app = getMeetCourseInfo_app(access_token, meetCourseId, role, uuid)
            assert result_getMeetCourseInfo_app.response.status_code == 200
            hours = result_getMeetCourseInfo_app.response.json()["rt"]["hours"]
            groupId = result_getMeetCourseInfo_app.response.json()["rt"]["groupId"]
            recruitId = result_getMeetCourseInfo_app.response.json()["rt"]["recruitId"]
            courseId = result_getMeetCourseInfo_app.response.json()["rt"]["courseId"]
            groupIdList = result_getMeetCourseInfo_app.response.json()["rt"]["groupIdList"]
            logger.info(
                "见面课信息为如下：见面课时间为{}小时，groupId：{}，recruitId：{}，courseId：{}，groupIdList：{}".format(hours, groupId,
                                                                                                recruitId, courseId,
                                                                                                groupIdList))
        else:
            logger.info("没有正在开启的见面课")
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_zhs_getMeetCourseInfo_app.py"])
