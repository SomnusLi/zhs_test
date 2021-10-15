import time

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
class Test_setWhiteboardStatus():
    """更改直播课堂的白板状态"""

    @allure.story("见面课直播")
    @allure.description("更改直播课堂的白板状态")
    @allure.title("更改直播课堂的白板状态")
    @pytest.mark.single
    def test_zhs_setWhiteboardStatus(self, login_fixture_teacher):
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
            logger.info("findMeetCourseLiveStatus")
            fromType = 1
            role = 1
            result_findMeetCourseLiveStatus = findMeetCourseLiveStatus(meetCourseId, role, fromType, uuid,
                                                                       cookies=cookies)
            assert result_findMeetCourseLiveStatus.response.status_code == 200
            openLiveFromType = result_findMeetCourseLiveStatus.response.json()["rt"]["openLiveFromType"]
            if result_findMeetCourseLiveStatus.response.status_code == 200:
                if openLiveFromType == -1:
                    logger.info("见面课类型为课堂工具")
                else:
                    if openLiveFromType == 1:
                        logger.info("见面课类型为直播课堂（语音）")
                    if openLiveFromType == 2:
                        logger.info("见面课类型为直播课堂（视频）")
                    logger.info("findWhiteboardInfo")
                    appType = 3  # ??
                    dateFormate = int(round(time.time() * 1000))
                    result_findWhiteboardInfo = findWhiteboardInfo(meetCourseId, appType, uuid, dateFormate,
                                                                   cookies=cookies)
                    assert result_findWhiteboardInfo.response.status_code == 200
                    if result_findWhiteboardInfo.response.status_code == 200:
                        logger.info("白板信息为：{}".format(result_findWhiteboardInfo.response.json()["rt"]))
                    logger.info("findWhiteboardStatus")
                    result_findWhiteboardStatus = findWhiteboardStatus(meetCourseId, uuid, dateFormate, cookies=cookies)
                    assert result_findWhiteboardStatus.response.status_code == 200
                    WhiteboardStatus = result_findWhiteboardStatus.response.json()["rt"]
                    if result_findWhiteboardStatus.response.status_code == 200:
                        logger.info(
                            "白板{}".format("已开启" if WhiteboardStatus else "未开启"))
                    logger.info("setWhiteboardStatus")
                    type = 1 if WhiteboardStatus else 0
                    result_setWhiteboardStatus = setWhiteboardStatus(meetCourseId, type, uuid, dateFormate,
                                                                     cookies=cookies)
                    assert result_setWhiteboardStatus.response.status_code == 200
                    logger.info("白板状态已变更")
        else:
            logger.info("没有正在开启的见面课")
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_zhs_setWhiteboardStatus.py"])
