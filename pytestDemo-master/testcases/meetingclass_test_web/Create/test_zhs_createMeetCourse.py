import pytest
import allure
from operation.course.course import *
from operation.meetingclass.meetingclass import *
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
class Test_creatMeetCourse():
    """创建见面课"""

    @allure.story("创建见面课")
    @allure.description("创建见面课")
    @allure.issue("https://www.zhihuishu.com/", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.zhihuishu.com/", name="点击，跳转到对应用例的链接地址")
    @allure.title("创建见面课")
    @pytest.mark.single
    def test_zhs_creatMeetCourse(self, login_fixture_teacher):
        logger.info("*************** 开始执行用例 ***************")
        # login_fixture前置登录
        user_info = login_fixture_teacher
        uuid = user_info.uuid
        account = user_info.account
        step_login(account, uuid)
        cookies = user_info.cookies
        result_get_courseInfo_teacher = get_courseInfo_teacher(uuid,
                                                               cookies=cookies)

        assert result_get_courseInfo_teacher.response.status_code == 200
        courseList = result_get_courseInfo_teacher.response.json()["rt"]["courseList"]
        courseId = courseList[randomRangeNum(0, len(courseList) - 1)]["courseId"]
        result_onlineservice_getStartingMeetCourseList = onlineservice_getStartingMeetCourseList(uuid,
                                                                                                 cookies=cookies)
        assert result_onlineservice_getStartingMeetCourseList.response.status_code == 200
        if result_onlineservice_getStartingMeetCourseList.response.json()["rt"] != []:
            logger.info("有正在开启的见面课")
        else:
            result_getUserRoleByCourseId = getUserRoleByCourseId(uuid, courseId,
                                                                 cookies=cookies)
            assert result_getUserRoleByCourseId.response.status_code == 200
            if result_getUserRoleByCourseId.response.json()["rt"] == 2:
                logger.info("该老师无权限开启见面课")
            else:
                result_getRecruitIdByCourseId = getRecruitIdByCourseId(courseId, cookies=cookies)
                assert result_getRecruitIdByCourseId.response.status_code == 200
                recruitId = result_getRecruitIdByCourseId.msg
                result_getSelectClassInfo = getSelectClassInfo(uuid, recruitId, cookies=cookies)
                assert result_getSelectClassInfo.response.status_code == 200
                classIds = ""
                for classlist in result_getSelectClassInfo.response.json()["rt"]["classInfos"]:
                    classIds = classIds + "&{}".format(classlist["id"])
                classIds = classIds[1:]
                result_creatMeetCourse = creatMeetCourse(uuid, courseId, classIds, recruitId,
                                                         cookies=cookies)
                assert result_creatMeetCourse.response.status_code == 200
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_zhs_createMeetCourse.py"])
