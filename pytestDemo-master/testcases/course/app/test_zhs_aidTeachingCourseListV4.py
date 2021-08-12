import pytest
import allure
from operation.course.course import *
from testcases.conftest import api_data
from common.logger import logger
import requests
from common.filedValueGenerate import add_cookies


@allure.step("前置登录步骤 ==>> 用户登录")
def step_login(account, uuid):
    logger.info("前置登录步骤 ==>> 用户 {} 登录 ==>> 返回的 uuid 为：{}".format(account, uuid))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("课程列表模块")
@allure.feature("老师app端")
class Test_aidTeachingCourseListV4():
    """app获取老师的课程列表"""

    @allure.story("app获取老师的课程列表")
    @allure.description("app获取老师的课程列表")
    @allure.issue("https://www.zhihuishu.com/", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.zhihuishu.com/", name="点击，跳转到对应用例的链接地址")
    @allure.title("app获取老师的课程列表")
    @pytest.mark.single
    def test_zhs_aidTeachingCourseListV4(self, login_fixture_teacher_app):
        logger.info("*************** 开始执行用例 ***************")
        # login_fixture前置登录
        user_info_app = login_fixture_teacher_app
        uuid = user_info_app.json()["rt"]["loginInfo"]["uuId"]
        account = user_info_app.request.body[8:19]
        access_token = user_info_app.json()["rt"]["access_token"]
        step_login(account, uuid)
        logger.info("aidTeachingCourseListV4")
        result_aidTeachingCourseListV4 = aidTeachingCourseListV4(access_token, uuid)
        assert result_aidTeachingCourseListV4.response.status_code == 200
        if result_aidTeachingCourseListV4.response.status_code == 200:
            logger.info("该老师课程信息为：{}".format(result_aidTeachingCourseListV4.response.json()["rt"]))

        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_zhs_aidTeachingCourseListV4.py"])
