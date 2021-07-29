import pytest
import allure
from operation.course.course import get_courseInfo_teacher
from testcases.conftest import api_data
from common.logger import logger
import requests
from common.filedValueGenerate import add_cookies


@allure.step("前置登录步骤 ==>> 用户登录")
def step_login(account, uuid):
    logger.info("前置登录步骤 ==>> 用户 {} 登录 ==>> 返回的 uuid 为：{}".format(account, uuid))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("课程列表模块")
@allure.feature("web教师端")
class TestGetCourseId():
    """获取用户(教师)的课程列表"""

    @allure.story("获取用户(教师)的课程列表")
    @allure.description("获取用户(教师)的课程列表")
    @allure.issue("https://www.zhihuishu.com/", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.zhihuishu.com/", name="点击，跳转到对应用例的链接地址")
    @allure.title("获取用户(教师)的课程列表")
    @pytest.mark.single
    def test_get_courseInfo_teacher(self, login_fixture_teacher):
        logger.info("*************** 开始执行用例 ***************")
        # login_fixture前置登录
        user_info = login_fixture_teacher
        uuid = user_info.json().get("uuid")
        account = user_info.request.body[8:19]
        step_login(account, uuid)
        cookies = add_cookies(requests.utils.dict_from_cookiejar(user_info.cookies))
        result = get_courseInfo_teacher(uuid, cookies=cookies)
        logger.info(result.response.text)
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_zhs_get_courseInfo_teacher.py"])
