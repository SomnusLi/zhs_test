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
@allure.epic("业务流程测试")
@allure.feature("见面课模块")
class Test_signUserIdsHistory():
    """查询已签未签学生的相关信息"""

    @allure.story("用例--查询已签未签学生的相关信息")
    @allure.description("该用例查询已签未签学生的相关信息")
    @allure.issue("https://hikeservice.zhihuishu.com/student/course/aided/getMyCourseLis", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://hikeservice.zhihuishu.com/student/course/aided/getMyCourseLis", name="点击，跳转到对应用例的链接地址")
    @allure.title(
        "测试数据：上游业务获取")
    @pytest.mark.single
    def test_zhs_signUserIdsHistory(self, login_fixture_teacher):
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
            logger.info("screenCourseClassInteractionListV2")
            page = 0
            pageSize = 100
            result_screenCourseClassInteractionListV2 = screenCourseClassInteractionListV2(meetCourseId, page, pageSize,
                                                                                           uuid,
                                                                                           cookies=cookies)
            assert result_screenCourseClassInteractionListV2.response.status_code == 200
            if result_screenCourseClassInteractionListV2.response.json()["rt"]["interactionListGoing"] == []:
                logger.info("没有正在进行中的互动")
            else:
                for ListGoing in result_screenCourseClassInteractionListV2.response.json()["rt"][
                    "interactionListGoing"]:
                    if ListGoing["type"] == 1:
                        checkId = ListGoing["interactionMap"]["signId"]
                        for checkType in range(1, 3):
                            userName = ""
                            result_signUserIdsHistory = signUserIdsHistory(checkId, checkType, userName, groupId, uuid,
                                                                           cookies=cookies)
                            assert result_signUserIdsHistory.response.status_code == 200
            if result_screenCourseClassInteractionListV2.response.json()["rt"]["InteractionDetailDtos"] == []:
                logger.info("本见面课没有互动")
            else:
                for DetailDtos in result_screenCourseClassInteractionListV2.response.json()["rt"][
                    "InteractionDetailDtos"]:
                    if DetailDtos["type"] == 1:
                        checkId = DetailDtos["interactionMap"]["signId"]
                        for checkType in range(1, 3):
                            userName = ""
                            result_signUserIdsHistory = signUserIdsHistory(checkId, checkType, userName, groupId, uuid,
                                                                           cookies=cookies)
                            assert result_signUserIdsHistory.response.status_code == 200
        else:
            logger.info("没有正在开启的见面课")


logger.info("*************** 结束执行用例 ***************")

if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_zhs_signUserIdsHistory.py"])