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
class Test_startMeetingCourseLiving():
    """开启直播"""

    @allure.story("见面课直播")
    @allure.description("开启直播")
    @allure.issue("https://www.zhihuishu.com/", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.zhihuishu.com/", name="点击，跳转到对应用例的链接地址")
    @allure.title("开启直播")
    @pytest.mark.single
    def test_zhs_startMeetingCourseLiving(self, login_fixture_teacher):
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

            if result_findMeetCourseLiveStatus.response.json()["rt"]["isliving"] != 2:
                logger.info("checkMeetCourseLivingAuthByUuid")
                result_checkMeetCourseLivingAuthByUuid = checkMeetCourseLivingAuthByUuid(uuid,
                                                                                         cookies=cookies)
                assert result_checkMeetCourseLivingAuthByUuid.response.status_code == 200
                type = "3"
                # 功能点id：1.资源库会员 2.资源库选课会员 3.视频直播(手机版) 4.直播白板 5.直播录屏 6.师说会员 7.数据中心 8.设备直播(手机端) 9.金课评审会员 10.共享题库 11.管理者教学指挥中心 12.数据联动 13.单点登录 14.学校门户(PC版本) 15.学校门户(手机版本) 16.防作弊管理 17.校内加速 18.定制服务 19.专业版期末报告 20.校资源库 21.校内spoc教学 22.视频监考 23.AI监考
                logger.info("verifyMembershipFunctionPermissions")
                result_verifyMembershipFunctionPermissions = verifyMembershipFunctionPermissions(type, uuid,
                                                                                                 cookies=cookies)
                assert result_verifyMembershipFunctionPermissions.response.status_code == 200
                if result_checkMeetCourseLivingAuthByUuid.response.json()["rt"]:
                    if result_verifyMembershipFunctionPermissions.response.json()["rt"]["auth"]:
                        logger.info("findMeetCourseMsg")
                        result_findMeetCourseMsg = findMeetCourseMsg(meetCourseId, uuid,
                                                                     cookies=cookies)
                        assert result_findMeetCourseMsg.response.status_code == 200
                        groupId = result_findMeetCourseMsg.response.json()["rt"]["groupId"]
                        openLiveFromType = 1
                        logger.info("startMeetingCourseLiving")
                        result_startMeetingCourseLiving = startMeetingCourseLiving(groupId, openLiveFromType,
                                                                                   meetCourseId, uuid, cookies=cookies)
                        assert result_startMeetingCourseLiving.response.status_code == 200
                    else:
                        logger.info("老师没有开通付费直播的权限")
                else:
                    logger.info("老师未进行用户直播认证")
            else:
                logger.info("该用户已开启直播")
        else:
            logger.info("没有正在开启的见面课")
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_zhs_startMeetingCourseLiving.py"])
