import pytest
import allure
from operation.course.course import *
from operation.meetingclass.meetingclass import *
from testcases.conftest import api_data
from common.logger import logger
from common.filedValueGenerate import add_cookies, randomRangeNum, getRandomCheckGesture
import requests
import random


@allure.step("前置登录步骤 ==>> 用户登录")
def step_login(account, uuid):
    logger.info("前置登录步骤 ==>> 用户 {} 登录 ==>> 返回的 uuid 为：{}".format(account, uuid))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("业务流程测试")
@allure.feature("见面课模块")
class Test_startRollcall():
    """开始点名"""

    @allure.story("用例--开始点名")
    @allure.description("该用例开始点名")
    @allure.issue("https://hikeservice.zhihuishu.com/student/course/aided/getMyCourseLis", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://hikeservice.zhihuishu.com/student/course/aided/getMyCourseLis", name="点击，跳转到对应用例的链接地址")
    @allure.title("测试数据：上游业务获取")
    @pytest.mark.single
    def test_zhs_startRollcall(self, login_fixture_teacher):
        logger.info("*************** 开始执行用例 ***************")
        # login_fixture前置登录
        user_info = login_fixture_teacher
        uuid = user_info.json().get("uuid")
        account = user_info.request.body[8:19]
        step_login(account, uuid)
        cookies = add_cookies(requests.utils.dict_from_cookiejar(user_info.cookies))
        logger.info("getStartingMeetCourseList")
        result_onlineservice_getStartingMeetCourseList = onlineservice_getStartingMeetCourseList(uuid,
                                                                                                 cookies=cookies)
        assert result_onlineservice_getStartingMeetCourseList.response.status_code == 200
        if result_onlineservice_getStartingMeetCourseList.response.json()["rt"] != []:
            logger.info("有正在开启的见面课")
            meetCourseId = result_onlineservice_getStartingMeetCourseList.response.json()["rt"][0]["meetCourseId"]
            courseName = result_onlineservice_getStartingMeetCourseList.response.json()["rt"][0]["courseName"]
            logger.info("get_courseInfo_teacher")
            result_get_courseInfo_teacher = get_courseInfo_teacher(uuid, cookies=cookies)
            for courseList in result_get_courseInfo_teacher.response.json()["rt"]["courseList"]:
                if courseName == courseList["courseName"]:
                    courseId = courseList["courseId"]
                    break
            logger.info("开启直播的courseId为{}".format(courseId))
            logger.info("findMeetCourseMsg")
            result_findMeetCourseMsg = findMeetCourseMsg(meetCourseId, uuid,
                                                         cookies=cookies)
            assert result_findMeetCourseMsg.response.status_code == 200
            groupId = result_findMeetCourseMsg.response.json()["rt"]["groupId"]
            logger.info("findMeetCourseStudentInfo")
            result_findMeetCourseStudentInfo = findMeetCourseStudentInfo(groupId, meetCourseId, courseId, uuid,
                                                                         cookies=cookies)
            assert result_findMeetCourseStudentInfo.response.status_code == 200
            StudentNum = len(result_findMeetCourseStudentInfo.response.json()["rt"])
            count = randomRangeNum(1, StudentNum)
            logger.info("startRollcall")
            result_startRollcall = startRollcall(groupId, count, uuid, cookies=cookies)
            assert result_startRollcall.response.status_code == 200
        else:
            logger.info("没有正在开启的见面课")
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_zhs_startRollcall.py"])