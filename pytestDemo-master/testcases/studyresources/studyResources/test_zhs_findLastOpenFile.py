import random
import pytest
import allure
from operation.course.course import get_courseInfo_teacher
from operation.studyResources.studyResources import *
from testcases.conftest import api_data
from common.logger import logger
from common.filedValueGenerate import add_cookies
import requests


# @allure.step("步骤1 ==>> 根据ID修改用户信息")
# def step_1(id):
#     logger.info("步骤1 ==>> 修改用户ID：{}".format(id))

@allure.step("前置登录步骤 ==>> 用户登录")
def step_login(account, uuid):
    logger.info("前置登录步骤 ==>> 用户 {} 登录 ==>> 返回的 uuid 为：{}".format(account, uuid))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("学习资源模块")
@allure.feature("教师端学习资源")
class Test_findLastOpenFile():
    """查询见面课最后打开的文件"""

    @allure.story("查询见面课最后打开的文件")
    @allure.description("查询见面课最后打开的文件")
    @allure.issue("https://www.zhihuishu.com/", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.zhihuishu.com/", name="点击，跳转到对应用例的链接地址")
    @allure.title("查询见面课最后打开的文件")
    @pytest.mark.single
    def test_zhs_findLastOpenFile(self, login_fixture_teacher):
        logger.info("*************** 开始执行用例 ***************")
        # login_fixture前置登录
        user_info = login_fixture_teacher
        uuid = user_info.json().get("uuid")
        account = user_info.request.body[8:19]
        step_login(account, uuid)
        cookies = add_cookies(requests.utils.dict_from_cookiejar(user_info.cookies))
        logger.info("get_courseInfo_teacher")
        result_get_courseInfo_teacher = get_courseInfo_teacher(uuid, cookies=cookies)
        courseId = random.sample(result_get_courseInfo_teacher.response.json()["rt"]["courseList"], 1)[0]["courseId"]
        logger.info("findLastOpenFile")
        result_findLastOpenFile = findLastOpenFile(courseId, uuid, cookies=cookies)
        assert result_findLastOpenFile.response.status_code == 200
        if result_findLastOpenFile.response.status_code == 200:
            if result_findLastOpenFile.response.json()["rt"] == None:
                logger.info("课程没有打开过文件")
            else:
                logger.info("课程下最后打开的文件id为：{}".format(result_findLastOpenFile.response.json()["rt"]["fileId"]))
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_zhs_findLastOpenFile.py"])
