import pytest
import allure
from operation.course.course import *
from operation.meetingclass.meetingclass import *
from testcases.conftest import api_data
from common.logger import logger
from common.filedValueGenerate import add_cookies, randomRangeNum, getRandomCheckGesture
import requests
import random


@allure.step("前置登录步骤 ==>> 用户登录")
def step_login(account, uuid):
    logger.info("前置登录步骤 ==>> 用户 {} 登录 ==>> 返回的 uuid 为：{}".format(account, uuid))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("见面课模块")
@allure.feature("web教师端")
class Test_chatVotePublishFastVote():
    """快速创建投票"""

    @allure.story("互动-投票")
    @allure.description("快速创建投票")
    @allure.issue("https://www.zhihuishu.com/", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.zhihuishu.com/", name="点击，跳转到对应用例的链接地址")
    @allure.title("快速创建投票")
    @pytest.mark.single
    def test_zhs_chatVotePublishFastVote(self, login_fixture_teacher):
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
            logger.info("findMeetCourseMsg")
            result_findMeetCourseMsg = findMeetCourseMsg(meetCourseId, uuid,
                                                         cookies=cookies)
            assert result_findMeetCourseMsg.response.status_code == 200
            groupId = result_findMeetCourseMsg.response.json()["rt"]["groupId"]
            type = randomRangeNum(1, 3)  # 题目类型 1单选题 2判断题 3多选题
            if type == 1:
                optionCount = randomRangeNum(2, 10)
            elif type == 2:
                optionCount = randomRangeNum(2, 9)
            elif type == 3:
                optionCount = randomRangeNum(2, 10)
            limitTime = randomRangeNum(0, 180) * 60
            logger.info("chatVotePublishFastVote")
            result_chatVotePublishFastVote = chatVotePublishFastVote(groupId, type, optionCount, limitTime, uuid,
                                                                     cookies=cookies)
            assert result_chatVotePublishFastVote.response.status_code == 200
            logger.info(result_chatVotePublishFastVote.response.json()["rt"]["resultMessage"])
        else:
            logger.info("没有正在开启的见面课")
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_zhs_chatVotePublishFastVote.py"])
