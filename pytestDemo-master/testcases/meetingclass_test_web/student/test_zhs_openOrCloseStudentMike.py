import random

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
@allure.feature("web教师端")
class Test_openOrCloseStudentMike():
    """邀请学生上/下麦"""

    @allure.story("学生信息")
    @allure.description("邀请学生上/下麦")
    @allure.issue("https://www.zhihuishu.com/", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.zhihuishu.com/", name="点击，跳转到对应用例的链接地址")
    @allure.title("邀请学生上/下麦")
    @pytest.mark.single
    def test_zhs_openOrCloseStudentMike(self, login_fixture_teacher):
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
            logger.info("findMeetCourseLiveStatus")
            fromType = 1
            role = 1
            result_findMeetCourseLiveStatus = findMeetCourseLiveStatus(meetCourseId, role, fromType, uuid,
                                                                       cookies=cookies)
            assert result_findMeetCourseLiveStatus.response.status_code == 200
            logger.info("findMeetCourseMsg")
            result_findMeetCourseMsg = findMeetCourseMsg(meetCourseId, uuid,
                                                         cookies=cookies)
            assert result_findMeetCourseMsg.response.status_code == 200
            courseId = result_findMeetCourseMsg.response.json()["rt"]["courseId"]
            groupId = result_findMeetCourseMsg.response.json()["rt"]["groupId"]
            logger.info("开启直播的courseId为{}".format(courseId))
            logger.info("getOnline")
            result_getOnline = getOnline(groupId, cookies=cookies)
            assert result_getOnline.response.status_code == 200
            if result_getOnline.response.status_code == 200:
                logger.info("在线学生数为{}，id为{}".format(len(result_getOnline.response.json()["rt"]),
                                                    result_getOnline.response.json()["rt"]))
            onlineStudentList = []
            for onlineStudent in result_getOnline.response.json()["rt"]:
                onlineStudentList.append(int(onlineStudent))

            if result_findMeetCourseLiveStatus.response.json()["rt"]["isliving"] == 2:
                meetCourseLivingId = result_findMeetCourseLiveStatus.response.json()["rt"]["meetCourseLivingId"]
                logger.info("该用户已开启直播")
                logger.info("findOpenMikeList")
                result_findOpenMikeList = findOpenMikeList(meetCourseId, meetCourseLivingId, courseId, uuid,
                                                           cookies=cookies)
                assert result_findOpenMikeList.response.status_code == 200
                openMikeList = []
                if result_findOpenMikeList.response.status_code == 200:
                    for mikelist in result_findOpenMikeList.response.json()["rt"]:
                        openMikeList.append(mikelist["userId"])
                logger.info("在线学生数为{},学生id为{}".format(len(onlineStudentList), onlineStudentList))
                logger.info("上麦学生总数为{}，学生id为{}".format(len(openMikeList), openMikeList))
                if len(onlineStudentList) != 0:
                    studentId = random.sample(onlineStudentList, 1)[0]

                    if studentId in openMikeList:
                        logger.info("该学生正在上麦状态")
                        type = 1  # 下麦
                        result_openOrCloseStudentMike = openOrCloseStudentMike(studentId, groupId, meetCourseLivingId,
                                                                               meetCourseId, type, uuid,
                                                                               cookies=cookies)
                        assert result_openOrCloseStudentMike.response.status_code == 200
                        if result_openOrCloseStudentMike.response.json()["rt"] == 1:
                            logger.info("下麦成功")
                    else:
                        logger.info("该学生没有上麦")
                        type = 0  # 上麦
                        result_openOrCloseStudentMike = openOrCloseStudentMike(studentId, groupId, meetCourseLivingId,
                                                                               meetCourseId, type, uuid,
                                                                               cookies=cookies)
                        assert result_openOrCloseStudentMike.response.status_code == 200
                        if result_openOrCloseStudentMike.response.json()["rt"] == 1:
                            logger.info("已向学生发送上麦请求")

            else:
                logger.info("该用户没有开启直播")
        else:
            logger.info("没有正在开启的见面课")
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_zhs_openOrCloseStudentMike.py"])
