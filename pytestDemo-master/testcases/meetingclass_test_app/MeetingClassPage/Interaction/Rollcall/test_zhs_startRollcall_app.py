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
class Test_startRollcall_app():
    """app开始随机点名"""

    @allure.story("互动-点名")
    @allure.description("app开始随机点名")
    @allure.title("app开始随机点名")
    @pytest.mark.single
    def test_zhs_startRollcall_app(self, login_fixture_teacher_app):
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
            logger.info("getGroupMemberCount_app")
            result_getGroupMemberCount_app = getGroupMemberCount_app(groupId, uuid, access_token=access_token)
            assert result_getGroupMemberCount_app.response.status_code == 200
            sumCount = result_getGroupMemberCount_app.response.json()["rt"]["sumCount"]
            logger.info("群组数量为：{}".format(sumCount))
            if sumCount == 1:
                # logger.info("人数不够,无法创建随机点名！")
                count = 1
            else:
                count = randomRangeNum(1, sumCount - 1)
            logger.info("startRollcall_app")
            result_startRollcall_app = startRollcall_app(count, groupId, uuid, access_token=access_token)
            assert result_startRollcall_app.response.status_code == 200
            logger.info("随机点名详情：{}".format(result_startRollcall_app.response.json()["rt"]["personList"]))
        else:
            logger.info("没有正在开启的见面课")
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_zhs_startRollcall_app.py"])
