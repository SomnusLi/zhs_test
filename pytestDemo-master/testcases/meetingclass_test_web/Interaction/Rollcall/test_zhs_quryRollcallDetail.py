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
class Test_quryRollcallDetail():
    """查询随机点名结果"""

    @allure.story("互动-点名")
    @allure.description("查询随机点名结果")
    @allure.issue("https://www.zhihuishu.com/", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.zhihuishu.com/", name="点击，跳转到对应用例的链接地址")
    @allure.title("查询随机点名结果")
    @pytest.mark.single
    def test_zhs_quryRollcallDetail(self, login_fixture_teacher):
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
            num_going_rollcall = False
            num_ended_rollcall = False
            if result_screenCourseClassInteractionListV2.response.json()["rt"]["interactionListGoing"] == []:
                logger.info("没有正在进行中的互动")
            else:
                for ListGoing in result_screenCourseClassInteractionListV2.response.json()["rt"][
                    "interactionListGoing"]:
                    if ListGoing["type"] == 3:
                        num_going_rollcall = True
                        rollcallId = ListGoing["interactionMap"]["rollcallId"]
                        logger.info("quryRollcallDetail")
                        result_quryRollcallDetail = quryRollcallDetail(rollcallId, uuid, cookies=cookies)
                        assert result_quryRollcallDetail.response.status_code == 200
            if result_screenCourseClassInteractionListV2.response.json()["rt"]["InteractionDetailDtos"] == []:
                logger.info("本见面课没有互动")
            else:
                for DetailDtos in result_screenCourseClassInteractionListV2.response.json()["rt"][
                    "InteractionDetailDtos"]:
                    if DetailDtos["type"] == 3:
                        num_ended_rollcall = True
                        rollcallId = DetailDtos["interactionMap"]["rollcallId"]
                        logger.info("quryRollcallDetail")
                        result_quryRollcallDetail = quryRollcallDetail(rollcallId, uuid, cookies=cookies)
                        assert result_quryRollcallDetail.response.status_code == 200
            if num_going_rollcall:
                logger.info("有正在进行中的随机点名")
            else:
                logger.info("没有正在进行中的随机点名")
            if num_ended_rollcall:
                logger.info("有已结束的随机点名")
            else:
                logger.info("没有已结束的随机点名")
        else:
            logger.info("没有正在开启的见面课")


logger.info("*************** 结束执行用例 ***************")

if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_zhs_quryRollcallDetail.py"])
