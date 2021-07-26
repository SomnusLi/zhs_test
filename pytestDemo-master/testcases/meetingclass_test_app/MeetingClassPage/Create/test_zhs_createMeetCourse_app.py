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
@allure.epic("业务流程测试")
@allure.feature("见面课模块")
class Test_createMeetCourse_app():
    """app创建见面课"""

    @allure.story("用例--app创建见面课")
    @allure.description("该用例是app创建见面课")
    @allure.title(
        "测试数据：上游业务获取")
    @pytest.mark.single
    def test_zhs_createMeetCourse_app(self, login_fixture_teacher_app):
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
        else:
            logger.info("没有正在开启的见面课")
            result_aidTeachingCourseListV4 = aidTeachingCourseListV4(access_token, uuid)
            assert result_aidTeachingCourseListV4.response.status_code == 200
            if result_aidTeachingCourseListV4.response.status_code == 200 and \
                    result_aidTeachingCourseListV4.response.json()["rt"] != []:
                courseList = random.sample(result_aidTeachingCourseListV4.response.json()["rt"], 1)
                courseId = courseList[0]["courseId"]
                recruitId = courseList[0]["recruitId"]
                courseName = courseList[0]["courseName"]
                logger.info("courseId: {} ,recruitId: {} ,课程名称为 {}".format(courseId, recruitId, courseName))
                logger.info("aidTeachingCourseClasses_app")
                result_aidTeachingCourseClasses_app = aidTeachingCourseClasses_app(access_token, recruitId, uuid)
                assert result_aidTeachingCourseClasses_app.response.status_code == 200
                classIds = []
                if result_aidTeachingCourseClasses_app.response.status_code == 200:
                    if result_aidTeachingCourseClasses_app.response.json()["rt"] != None:
                        classList = random.sample(result_aidTeachingCourseClasses_app.response.json()["rt"],
                                                  randomRangeNum(1, len(
                                                      result_aidTeachingCourseClasses_app.response.json()[
                                                          "rt"])))
                        for classIdList in classList:
                            classIds.append(classIdList["classId"])
                    logger.info(classIds)
                    hours = randomRangeNum(3, 10)
                    result_createMeetCourse_app = createMeetCourse_app(access_token, classIds, courseId, hours,
                                                                       recruitId, uuid)
                    assert result_createMeetCourse_app.response.status_code == 200
                    logger.info(result_createMeetCourse_app.response.json()["rt"])
                else:
                    logger.info("该课程下没有班级")
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_zhs_createMeetCourse_app.py"])
