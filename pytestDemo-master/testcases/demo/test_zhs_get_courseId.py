import pytest
import allure
from operation.course.course import get_courseInfo
from testcases.conftest import api_data
from common.logger import logger
import requests


# @allure.step("步骤1 ==>> 根据ID修改用户信息")
# def step_1(id):
#     logger.info("步骤1 ==>> 修改用户ID：{}".format(id))

@allure.step("前置登录步骤 ==>> 用户登录")
def step_login(account, uuid):
    logger.info("前置登录步骤 ==>> 用户 {} 登录 ==>> 返回的 uuid 为：{}".format(account, uuid))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("见面课模块")
@allure.feature("课程列表模块")
class TestGetCourseId():
    """获取用户的课程列表"""

    @allure.story("获取用户的课程列表")
    @allure.description("该用例是针对获取用户修改接口的测试")
    @allure.issue("https://www.zhihuishu.com/", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.zhihuishu.com/", name="点击，跳转到对应用例的链接地址")
    @allure.title(
        "上游业务获取")
    @pytest.mark.single
    # @pytest.mark.parametrize("id, new_password, new_telephone, new_sex, new_address, "
    #                          "except_result, except_code, except_msg",
    #                          api_data["test_update_user"])
    # @pytest.mark.usefixtures("Get_courseId")
    @pytest.mark.skip
    def test_get_courseId(self, login_fixture):
        logger.info("*************** 开始执行用例 ***************")
        # login_fixture前置登录
        user_info = login_fixture
        uuid = user_info.uuid
        account = user_info.account
        step_login(account, uuid)
        # cookies要传str类型
        result = get_courseInfo(uuid, requests.utils.dict_from_cookiejar(user_info.cookies))
        assert result.response.status_code == 200
        logger.info("code ==>> 实际结果：{}".format(result.response.json().get("status")))
        # assert result.response.json().get("status") == except_status
        # assert set(six.viewitems(except_msg)).issubset(set(six.viewitems(result.msg)))
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_zhs_get_courseInfo_student.py"])
