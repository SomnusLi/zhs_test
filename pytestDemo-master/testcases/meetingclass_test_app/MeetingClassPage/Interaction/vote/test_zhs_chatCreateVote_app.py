import random

import pytest
import allure
from common.filedValueGenerate import *
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
class Test_chatCreateVote_app():
    """app创建投票"""

    @allure.story("互动-投票")
    @allure.description("app创建投票")
    @allure.title("app创建投票")
    @pytest.mark.single
    def test_zhs_chatCreateVote_app(self, login_fixture_teacher_app):
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
            groupIds = result_getMeetCourseInfo_app.response.json()["rt"]["groupId"]
            limitTime = randomRangeNum(0, 180) * 60
            isMultiple = 1  # randomRangeNum(0, 1)  # 0 不可多选 1可多选
            isAnonymous = randomRangeNum(0, 1)  # 0公开 1不公开
            isSaveWaitPublish = randomRangeNum(0, 1)  # 0 立即发布 1保存到稍后发布
            isVoterScan = randomRangeNum(0, 1)  # 0 不允许参与者 查看结果 1 允许查看结果
            voteOptions = "["
            voteOptionsnum = randomRangeNum(2, 9)  # 选项个数
            logger.info(voteOptionsnum)
            correctAnswerList = []
            for i in range(0, voteOptionsnum):
                voteOptions = voteOptions + "'" + getAutoStr(randomRangeNum(1, 10)) + "',"
                correctAnswerList.append(chr(65 + i))
            if isMultiple == 0:
                correctAnswer = random.sample(correctAnswerList, 1)
                logger.info(correctAnswer)
            else:
                correctAnswer = random.sample(correctAnswerList, randomRangeNum(2, voteOptionsnum))
                logger.info(correctAnswer)
            voteOptions = voteOptions + "]"
            logger.info(voteOptions)
            voteQuestion = getAutoStr(randomRangeNum(5, 10))
            voteTimerSend = int(round(time.time() * 1000)) + randomRangeNum(0, 180) * 60 * 1000 if randomRangeNum(0,
                                                                                                                  1) == 0 else ""
            logger.info(voteTimerSend)
            logger.info("chatCreateVote_app")
            result_chatCreateVote_app = chatCreateVote_app(correctAnswer, groupIds, isAnonymous, isMultiple,
                                                           isSaveWaitPublish, isVoterScan, limitTime, uuid, voteOptions,
                                                           voteQuestion, voteTimerSend, access_token=access_token)
            assert result_chatCreateVote_app.response.status_code == 200
            if result_chatCreateVote_app.response.status_code == 200:
                logger.info(
                    "{}，创建的voteid为{}".format(result_chatCreateVote_app.response.json()["rt"]["resultMessage"],
                                             result_chatCreateVote_app.response.json()["rt"]["voteId"]))
        else:
            logger.info("没有正在开启的见面课")
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_zhs_chatCreateVote_app.py"])
