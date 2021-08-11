import pytest
import allure
from operation.meetingclass.meetingclass import *
from testcases.conftest import api_data
from common.logger import logger
from operation.studyResources.studyResources import *
import requests


@allure.step("前置登录步骤 ==>> 用户登录")
def step_login(account, uuid):
    logger.info("前置登录步骤 ==>> 用户 {} 登录 ==>> 返回的 uuid 为：{}".format(account, uuid))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("见面课模块")
@allure.feature("app教师端")
class Test_quryRushAnswerDetail_app():
    """app查询抢答详细"""

    @allure.story("互动-抢答")
    @allure.description("app查询抢答详细")
    @allure.title("app查询抢答详细")
    @pytest.mark.single
    def test_zhs_quryRushAnswerDetail_app(self, login_fixture_teacher_app):
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
            groupId = result_getMeetCourseInfo_app.response.json()["rt"]["groupId"]
            logger.info("findRunningPreemptive_app")
            result_findRunningPreemptive_app = findRunningPreemptive_app(groupId, uuid, access_token=access_token)
            assert result_findRunningPreemptive_app.response.status_code == 200
            if result_findRunningPreemptive_app.response.status_code == 200:
                if result_findRunningPreemptive_app.response.json()["rt"]["rushAnswerId"] != "":
                    rushAnswerId = result_findRunningPreemptive_app.response.json()["rt"]["rushAnswerId"]
                    logger.info("有正在进行中的抢答，抢答id为：{}".format(rushAnswerId))
                    logger.info("endRushAnswer_app")
                    result_endRushAnswer_app = endRushAnswer_app(rushAnswerId, groupId, uuid, access_token=access_token)
                    assert result_endRushAnswer_app.response.status_code == 200
                    if result_endRushAnswer_app.response.status_code == 200:
                        logger.info("{}".format(result_endRushAnswer_app.response.json()["rt"]["resultMessage"]))
                    result_quryRushAnswerDetail = quryRushAnswerDetail_app(rushAnswerId, groupId, uuid,
                                                                           access_token=access_token)
                    assert result_quryRushAnswerDetail.response.status_code == 200
                    if result_quryRushAnswerDetail.response.status_code == 200:
                        logger.info("抢答的id为{}，抢答的详情为{}".format(rushAnswerId,
                                                               result_quryRushAnswerDetail.response.json()["rt"]["rs"]))
                else:
                    logger.info("没有正在进行中的抢答")
        else:
            logger.info("没有正在开启的见面课")
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_zhs_quryRushAnswerDetail_app.py"])
