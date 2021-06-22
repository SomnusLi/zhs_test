import pytest
import allure
from operation.course.course import get_courseInfo_teacher
from operation.meetingclass.meetingclass import getStartingMeetCourseList
from testcases.conftest import api_data
from common.logger import logger
from common.filedValueGenerate import *
import requests


# @allure.step("步骤1 ==>> 根据ID修改用户信息")
# def step_1(id):
#     logger.info("步骤1 ==>> 修改用户ID：{}".format(id))

@allure.step("前置登录步骤 ==>> 用户登录")
def step_login(account, uuid):
    logger.info("前置登录步骤 ==>> 用户 {} 登录 ==>> 返回的 uuid 为：{}".format(account, uuid))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("业务流程测试")
@allure.feature("见面课模块")
class Test_getStartingMeetCourseList():
    """查询用户是否有进行中的见面课"""

    @allure.story("用例--根据课程/uuid查询相应角色是否有进行中的见面课")
    @allure.description("该用例是针对查询用户是否有进行中的见面课")
    @allure.issue("https://hikeservice.zhihuishu.com/student/course/aided/getMyCourseLis", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://hikeservice.zhihuishu.com/student/course/aided/getMyCourseLis", name="点击，跳转到对应用例的链接地址")
    @allure.title(
        "测试数据：上游业务获取")
    @pytest.mark.single
    # @pytest.mark.parametrize("id, new_password, new_telephone, new_sex, new_address, "
    #                          "except_result, except_code, except_msg",
    #                          api_data["test_update_user"])
    # @pytest.mark.usefixtures("Get_courseId")
    def test_zhs_getStartingMeetCourseList(self, login_fixture_teacher):
        logger.info("*************** 开始执行用例 ***************")
        # login_fixture前置登录
        user_info = login_fixture_teacher
        uuid = user_info.json().get("uuid")
        account = user_info.request.body[8:19]
        step_login(account, uuid)
        result_get_courseInfo_teacher = get_courseInfo_teacher(uuid,
                                                               cookies=add_cookies(requests.utils.dict_from_cookiejar(
                                                                   user_info.cookies)))
        courseList = result_get_courseInfo_teacher.response.json()["rt"]["courseList"]
        courseId = courseList[randomRangeNum(0, len(courseList) - 1)]["courseId"]
        print(courseId)
        assert result_get_courseInfo_teacher.response.status_code == 200

        result_getStartingMeetCourseList = getStartingMeetCourseList(uuid, courseId,
                                                                     cookies=add_cookies(
                                                                         requests.utils.dict_from_cookiejar(
                                                                             user_info.cookies)))
        assert result_getStartingMeetCourseList.response.status_code == 200
        # logger.info("code ==>> 实际结果：{}".format(result.response.json().get("result")))
        # assert result.response.json().get("status") == except_status
        # assert set(six.viewitems(except_msg)).issubset(set(six.viewitems(result.msg)))
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_zhs_getStartingMeetCourseList.py"])
