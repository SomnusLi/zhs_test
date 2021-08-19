import pytest
import allure
from operation.course.course import *
from operation.meetingclass.meetingclass import *
from testcases.conftest import api_data
from common.logger import logger
from common.filedValueGenerate import add_cookies, randomRangeNum
import requests
import random


@allure.step("前置登录步骤 ==>> 用户登录")
def step_login(account, uuid):
    logger.info("前置登录步骤 ==>> 用户 {} 登录 ==>> 返回的 uuid 为：{}".format(account, uuid))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("见面课模块")
@allure.feature("web教师端")
class Test_chatVotePublishAnswers():
    """发布投票答案"""

    @allure.story("互动-投票")
    @allure.description("发布投票答案")
    @allure.title("发布投票答案")
    @pytest.mark.single
    def test_zhs_chatVotePublishAnswers(self, login_fixture_teacher):
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
            logger.info("screenCourseClassInteractionListV2")
            page = 0
            pageSize = 100
            result_screenCourseClassInteractionListV2 = screenCourseClassInteractionListV2(meetCourseId, page, pageSize,
                                                                                           uuid,
                                                                                           cookies=cookies)
            assert result_screenCourseClassInteractionListV2.response.status_code == 200
            logger.info("findMeetCourseMsg")
            result_findMeetCourseMsg = findMeetCourseMsg(meetCourseId, uuid,
                                                         cookies=cookies)
            assert result_findMeetCourseMsg.response.status_code == 200
            groupId = result_findMeetCourseMsg.response.json()["rt"]["groupId"]
            num_going_vote = False
            num_ended_vote = False
            voteIds = []
            if result_screenCourseClassInteractionListV2.response.json()["rt"]["interactionListGoing"] == []:
                logger.info("没有正在进行中的互动")
            else:
                for ListGoing in result_screenCourseClassInteractionListV2.response.json()["rt"][
                    "interactionListGoing"]:
                    if ListGoing["type"] == 2:
                        num_going_vote = True
                        voteIds.append(ListGoing["interactionMap"]["voteId"])
            if result_screenCourseClassInteractionListV2.response.json()["rt"]["InteractionDetailDtos"] == []:
                logger.info("本见面课没有互动")
            else:
                for DetailDtos in result_screenCourseClassInteractionListV2.response.json()["rt"][
                    "InteractionDetailDtos"]:
                    if DetailDtos["type"] == 2:
                        num_ended_vote = True
                        voteIds.append(DetailDtos["interactionMap"]["voteId"])

            logger.info(voteIds)
            Flag_vote = True
            while Flag_vote and voteIds != []:
                voteId = random.sample(voteIds, 1)[0]
                voteIds.remove(voteId)
                logger.info("chatVoteDetail")
                result_chatVoteDetail = chatVoteDetail(voteId, uuid, cookies=cookies)
                assert result_chatVoteDetail.response.status_code == 200
                if result_chatVoteDetail.response.status_code == 200:
                    logger.info("投票id为{}，投票详情为：{}".format(voteId, result_chatVoteDetail.response.json()["rt"]))
                    if result_chatVoteDetail.response.json()["rt"]["correctItems"] == "":
                        logger.info("该投票没有设置正确答案！")
                        Flag_vote = True
                    else:
                        if result_chatVoteDetail.response.json()["rt"]["isPublishAnswer"] == 1:
                            logger.info("投票id为{}，投票已经发布答案了".format(voteId))
                            Flag_vote = True
                        elif result_chatVoteDetail.response.json()["rt"]["isPublishAnswer"] == 0:
                            logger.info("该投票是快速投票，无法公布答案")
                            Flag_vote = True
                        else:
                            logger.info("chatVotePublishAnswers_app")
                            Flag_vote = False
                            result_chatVotePublishAnswers = chatVotePublishAnswers(groupId, uuid, voteId,
                                                                                   cookies=cookies)
                            assert result_chatVotePublishAnswers.response.status_code == 200
                            if result_chatVotePublishAnswers.response.status_code == 200:
                                logger.info("投票id为{}，返回信息为：{}".format(voteId,
                                                                      result_chatVotePublishAnswers.response.json()[
                                                                          "rt"]))
            if Flag_vote and voteIds == []:
                logger.info("全部投票已经发布答案")
            if num_going_vote:
                logger.info("有正在进行中的投票")
            else:
                logger.info("没有正在进行中的投票")
            if num_ended_vote:
                logger.info("有已结束的投票")
            else:
                logger.info("没有已结束的投票")
        else:
            logger.info("没有正在开启的见面课")


logger.info("*************** 结束执行用例 ***************")

if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_zhs_chatVotePublishAnswers.py"])
