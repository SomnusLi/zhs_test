import random

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
class Test_chatDeleteVote_app():
    """app删除投票"""

    @allure.story("互动-投票")
    @allure.description("app删除投票")
    @allure.title("app删除投票")
    @pytest.mark.single
    def test_zhs_chatDeleteVote_app(self, login_fixture_teacher_app):
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
            courseClassId = result_getStartingMeetCourseList_app.response.json()["rt"][0]["meetCourseId"]
            logger.info("screenCourseClassInteractionListV2_app")
            page = 0
            pageSize = 2000
            showClassType = 0
            result_screenCourseClassInteractionListV2_app = screenCourseClassInteractionListV2_app(access_token,
                                                                                                   courseClassId, page,
                                                                                                   pageSize,
                                                                                                   showClassType,
                                                                                                   uuid)
            assert result_screenCourseClassInteractionListV2_app.response.status_code == 200
            logger.info(
                "正在进行的活动列表为：{} \n 已结束的活动列表为：{}".format(
                    result_screenCourseClassInteractionListV2_app.response.json()["rt"]["interactionListGoing"],
                    result_screenCourseClassInteractionListV2_app.response.json()["rt"]["InteractionDetailDtos"]))
            voteids = []
            for interactionListGoingList in result_screenCourseClassInteractionListV2_app.response.json()["rt"][
                "interactionListGoing"]:
                if interactionListGoingList["type"] == 2:
                    voteids.append(interactionListGoingList["interactionMap"]["voteId"])
            for InteractionDetailDtosList in result_screenCourseClassInteractionListV2_app.response.json()["rt"][
                "InteractionDetailDtos"]:
                if InteractionDetailDtosList["type"] == 2:
                    voteids.append(InteractionDetailDtosList["interactionMap"]["voteId"])
            logger.info(voteids)
            if voteids == []:
                logger.info("没有投票")
            else:
                voteId = random.sample(voteids, 1)[0]
                result_chatDeleteVote_app = chatDeleteVote_app(uuid, voteId, access_token=access_token)
                assert result_chatDeleteVote_app.response.status_code == 200
                if result_chatDeleteVote_app.response.status_code == 200:
                    logger.info("投票id为{}，返回信息为：{}".format(voteId, result_chatDeleteVote_app.response.json()["rt"]))
        else:
            logger.info("没有正在开启的见面课")
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_zhs_chatDeleteVote_app.py"])