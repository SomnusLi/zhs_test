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
class Test_createMeetingCourseLiving():
    """创建见面课（语音直播）"""

    @allure.story("创建见面课")
    @allure.description("创建见面课（语音直播）")
    @allure.title("创建见面课（语音直播）")
    @pytest.mark.single
    def test_zhs_createMeetingCourseLiving(self, login_fixture_teacher):
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
                logger.info("该老师无权限开启见面课（语音直播）")
            else:
                logger.info("checkMeetCourseLivingAuthByUuid")
                result_checkMeetCourseLivingAuthByUuid = checkMeetCourseLivingAuthByUuid(uuid,
                                                                                         cookies=cookies)
                assert result_checkMeetCourseLivingAuthByUuid.response.status_code == 200
                if result_checkMeetCourseLivingAuthByUuid.response.status_code == 200 and \
                        result_checkMeetCourseLivingAuthByUuid.response.json()["rt"] == True:
                    result_getRecruitIdByCourseId = getRecruitIdByCourseId(courseId, cookies=cookies)
                    assert result_getRecruitIdByCourseId.response.status_code == 200
                    recruitId = result_getRecruitIdByCourseId.msg
                    result_getSelectClassInfo = getSelectClassInfo(uuid, recruitId, cookies=cookies)
                    assert result_getSelectClassInfo.response.status_code == 200
                    classIds = ""
                    for classlist in result_getSelectClassInfo.response.json()["rt"]["classInfos"]:
                        classIds = classIds + "&{}".format(classlist["id"])
                    classIds = classIds[1:]
                    hours = randomRangeNum(3, 10)
                    openLiveFromType = 1  # 1-web 2-app开启直播 默认为1
                    deviceId = ""  # 设备id
                    equipmentNo = ""  # 设备编号(唯一)
                    playBackStatus = 1  # 视频直播回放 0-不 1-回放 默认为0
                    fromType = 1  # 设备 1-pc 2-app 3-H5 默认1-pc
                    screenType = 1  # 是否允许投屏：1：不允许，2：允许
                    meetCourseAuth = 1  # 用户的见面课权限 默认为0
                    timestamp = ""
                    dateFormate = int(round(time.time() * 1000))
                    logger.info("createMeetingCourseLiving")
                    result_createMeetingCourseLiving = createMeetingCourseLiving(courseId, classIds, recruitId, hours,
                                                                                 deviceId, equipmentNo,
                                                                                 openLiveFromType, screenType,
                                                                                 playBackStatus, fromType,
                                                                                 meetCourseAuth, timestamp, uuid,
                                                                                 dateFormate,
                                                                                 cookies=cookies)
                    assert result_createMeetingCourseLiving.response.status_code == 200
                    if result_createMeetingCourseLiving.response.status_code == 200:
                        logger.info(
                            "创建见面课（语音直播）成功，直播课堂信息为:{}".format(result_createMeetingCourseLiving.response.json()["rt"]))
                else:
                    logger.info("老师没有进行实名认证，无法开启直播课堂")
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_zhs_createMeetingCourseLiving.py"])
