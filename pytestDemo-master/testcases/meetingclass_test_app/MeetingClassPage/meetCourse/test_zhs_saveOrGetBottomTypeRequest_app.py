import pytest
import allure
from operation.course.course import get_courseInfo_teacher
from operation.meetingclass.meetingclass import *
from testcases.conftest import api_data
from common.logger import logger
from common.filedValueGenerate import getRandomList
import requests


@allure.step("前置登录步骤 ==>> 用户登录")
def step_login(account, uuid):
    logger.info("前置登录步骤 ==>> 用户 {} 登录 ==>> 返回的 uuid 为：{}".format(account, uuid))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("业务流程测试")
@allure.feature("见面课模块")
class Test_saveOrGetBottomTypeRequest_app():
    """app查询/修改常用工具列表"""

    @allure.story("用例--app查询/修改常用工具列表")
    @allure.description("该用例是app查询/修改常用工具列表")
    @allure.issue("https://hikeservice.zhihuishu.com/student/course/aided/getMyCourseLis", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://hikeservice.zhihuishu.com/student/course/aided/getMyCourseLis", name="点击，跳转到对应用例的链接地址")
    @allure.title(
        "测试数据：上游业务获取")
    @pytest.mark.single
    def test_zhs_saveOrGetBottomTypeRequest_app(self, login_fixture_teacher_app):
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
            type = randomRangeNum(0, 1)  # 0 修改  1 查询
            if type == 1:
                logger.info("saveOrGetBottomTypeRequest_app")
                result_saveOrGetBottomTypeRequest_app = saveOrGetBottomTypeRequest_app(access_token, type, uuid)
                assert result_saveOrGetBottomTypeRequest_app.response.status_code == 200
                logger.info(
                    "查询的常用工具type为：{}".format(result_saveOrGetBottomTypeRequest_app.response.json()["rt"]["typeStr"]))
            else:
                typeStr = getRandomList(3)
                logger.info("saveOrGetBottomTypeRequest_app")
                result_saveOrGetBottomTypeRequest_app = saveOrGetBottomTypeRequest_app(access_token, type, uuid,
                                                                                       typeStr)
                assert result_saveOrGetBottomTypeRequest_app.response.status_code == 200
                logger.info(
                    "返回信息为：{}".format(result_saveOrGetBottomTypeRequest_app.response.json()["rt"]["resultMessage"]))
        else:
            logger.info("没有正在开启的见面课")
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_zhs_saveOrGetBottomTypeRequest_app.py"])
