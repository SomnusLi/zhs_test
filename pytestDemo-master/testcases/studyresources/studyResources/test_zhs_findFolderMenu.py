import random
import pytest
import allure
from operation.course.course import get_courseInfo_teacher
from operation.studyResources.studyResources import *
from testcases.conftest import api_data
from common.logger import logger
from common.filedValueGenerate import add_cookies
import requests




@allure.step("前置登录步骤 ==>> 用户登录")
def step_login(account, uuid):
    logger.info("前置登录步骤 ==>> 用户 {} 登录 ==>> 返回的 uuid 为：{}".format(account, uuid))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("学习资源模块")
@allure.feature("教师端学习资源")
class Test_findFolderMenu():
    """查询课程下学习资源目录"""

    @allure.story("查询课程下学习资源目录")
    @allure.description("查询课程下学习资源目录")
    @allure.title("查询课程下学习资源目录")
    @pytest.mark.single
    def test_zhs_findFolderMenu(self, login_fixture_teacher):
        logger.info("*************** 开始执行用例 ***************")
        # login_fixture前置登录
        user_info = login_fixture_teacher
        uuid = user_info.uuid
        account = user_info.account
        step_login(account, uuid)
        cookies = user_info.cookies
        logger.info("get_courseInfo_teacher")
        result_get_courseInfo_teacher = get_courseInfo_teacher(uuid, cookies=cookies)
        courseId = random.sample(result_get_courseInfo_teacher.response.json()["rt"]["courseList"], 1)[0]["courseId"]
        logger.info("findFolderMenu")
        result_findFolderMenu = findFolderMenu(courseId, uuid, cookies=cookies)
        assert result_findFolderMenu.response.status_code == 200
        if result_findFolderMenu.response.status_code == 200:
            logger.info("课程目录为{}".format(result_findFolderMenu.response.json()["rt"]))
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_zhs_findFolderMenu.py"])
