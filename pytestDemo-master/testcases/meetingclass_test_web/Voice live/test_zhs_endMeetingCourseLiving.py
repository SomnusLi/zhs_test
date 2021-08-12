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
class Test_endMeetingCourseLiving():
    """关闭直播"""

    @allure.story("见面课直播")
    @allure.description("关闭直播")
    @allure.issue("https://www.zhihuishu.com/", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.zhihuishu.com/", name="点击，跳转到对应用例的链接地址")
    @allure.title("关闭直播")
    @pytest.mark.single
    def test_zhs_endMeetingCourseLiving(self, login_fixture_teacher):

        logger.info("*************** 开始执行用例 ***************")
        # login_fixture前置登录
        user_info = login_fixture_teacher
        uuid = user_info.uuid
        account = user_info.account
        step_login(account, uuid)
        cookies = user_info.cookies
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
            if result_findMeetCourseLiveStatus.response.json()["rt"]["isliving"] == 2:
                logger.info("该用户已开启直播")
                openLiveFromType = 1  # 1-web 2-app关闭直播 默认为1
                result_endMeetingCourseLiving = endMeetingCourseLiving(meetCourseId, openLiveFromType, uuid,
                                                                       cookies=cookies)
                assert result_endMeetingCourseLiving.response.status_code == 200
            else:
                logger.info("该用户没有开启直播")
        else:
            logger.info("没有正在开启的见面课")
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_zhs_endMeetingCourseLiving.py"])
