import random

import pytest
import allure
from operation.course.course import *
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
class Test_updateMeetCourseTeacherSetting_app():
    """app更改见面课审核状态"""

    @allure.story("创建见面课")
    @allure.description("app更改见面课审核状态")
    @allure.title("app更改见面课审核状态")
    @pytest.mark.single
    def test_zhs_updateMeetCourseTeacherSetting_app(self, login_fixture_teacher_app):
        logger.info("*************** 开始执行用例 ***************")
        # login_fixture前置登录
        user_info_app = login_fixture_teacher_app
        uuid = user_info_app.json()["rt"]["loginInfo"]["uuId"]
        account = user_info_app.request.body[8:19]
        access_token = user_info_app.json()["rt"]["access_token"]
        step_login(account, uuid)
        result_aidTeachingCourseListV4 = aidTeachingCourseListV4(access_token, uuid)
        assert result_aidTeachingCourseListV4.response.status_code == 200
        if result_aidTeachingCourseListV4.response.status_code == 200 and \
                result_aidTeachingCourseListV4.response.json()["rt"] != []:
            courseList = random.sample(result_aidTeachingCourseListV4.response.json()["rt"], 1)
            courseId = courseList[0]["courseId"]
            recruitId = courseList[0]["recruitId"]
            courseName = courseList[0]["courseName"]
            logger.info("courseId: {} ,recruitId: {} ,课程名称为 {}".format(courseId, recruitId, courseName))
            logger.info("getMeetCourseTeacherSetting_app")
            result_getMeetCourseTeacherSetting_app = getMeetCourseTeacherSetting_app(access_token, courseId, uuid)
            assert result_getMeetCourseTeacherSetting_app.response.status_code == 200
            if result_getMeetCourseTeacherSetting_app.response.status_code == 200:
                isAuditMeetingCourse = result_getMeetCourseTeacherSetting_app.response.json()["rt"][
                    "isAuditMeetingCourse"]
                logger.info("该课程面课审核状态为：{},{}".format(isAuditMeetingCourse,
                                                      "本见面课无需审核" if isAuditMeetingCourse == 0 else "见面课需要审核"))
                logger.info("updateMeetCourseTeacherSetting_app")
                result_updateMeetCourseTeacherSetting_app = updateMeetCourseTeacherSetting_app(access_token, courseId,
                                                                                               isAuditMeetingCourse,
                                                                                               uuid)
                assert result_updateMeetCourseTeacherSetting_app.response.status_code == 200
                logger.info(result_updateMeetCourseTeacherSetting_app.response.json()["rt"])
            logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_zhs_updateMeetCourseTeacherSetting_app.py"])
