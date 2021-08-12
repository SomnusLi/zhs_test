import pytest
import allure
from operation.course.course import get_courseInfo_teacher
from operation.meetingclass.meetingclass import getUserRoleByCourseId
from testcases.conftest import api_data
from common.logger import logger
from common.filedValueGenerate import add_cookies
import requests


@allure.step("前置登录步骤 ==>> 用户登录")
def step_login(account, uuid):
    logger.info("前置登录步骤 ==>> 用户 {} 登录 ==>> 返回的 uuid 为：{}".format(account, uuid))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("见面课模块")
@allure.feature("web教师端")
class Test_getUserRoleByCourseId():
    """查询用户角色创建见面课的权限"""

    @allure.story("创建见面课")
    @allure.description("查询用户角色创建见面课的权限")
    @allure.issue("https://www.zhihuishu.com/", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.zhihuishu.com/", name="点击，跳转到对应用例的链接地址")
    @allure.title("查询用户角色创建见面课的权限")
    @pytest.mark.single
    def test_zhs_getUserRoleByCourseId(self, login_fixture_teacher):
        logger.info("*************** 开始执行用例 ***************")
        # login_fixture前置登录
        user_info = login_fixture_teacher
        uuid = user_info.uuid
        account = user_info.account
        step_login(account, uuid)
        cookies = user_info.cookies
        result_get_courseInfo_teacher = get_courseInfo_teacher(uuid,
                                                               cookies=cookies)
        courseId = result_get_courseInfo_teacher.response.json()["rt"]["courseList"][0]["courseId"]
        assert result_get_courseInfo_teacher.response.status_code == 200

        result_getUserRoleByCourseId = getUserRoleByCourseId(uuid, courseId,
                                                             cookies=cookies)
        assert result_getUserRoleByCourseId.response.status_code == 200
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_zhs_getUserRoleByCourseId.py"])
