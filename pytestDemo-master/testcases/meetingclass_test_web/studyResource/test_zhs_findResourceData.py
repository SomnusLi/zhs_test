import random
import pytest
import allure
from operation.course.course import get_courseInfo_teacher
from operation.studyResources.studyResources import *
from operation.meetingclass.meetingclass import *
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
@allure.epic("业务流程测试")
@allure.feature("见面课模块")
class Test_findResourceData():
    """学习资源筛选"""

    @allure.story("用例--学习资源筛选")
    @allure.description("该用例是学习资源筛选")
    @allure.title("测试数据：上游业务获取")
    @pytest.mark.single
    def test_zhs_findResourceData(self, login_fixture_teacher):
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
            courseId = result_findMeetCourseMsg.response.json()["rt"]["courseId"]
            logger.info("findFolderMenu")
            result_findFolderMenu = findFolderMenu(courseId, uuid, cookies=cookies)
            assert result_findFolderMenu.response.status_code == 200
            if result_findFolderMenu.response.status_code == 200:
                rootFolderId = result_findFolderMenu.response.json()["rt"][0]["id"]
            type = randomRangeNum(1, 10)
            # 1 ppt 2 word 3 图片 4 视频 5 Excel 6 pdf 7 其他 8 音频 9 txt 10 压缩包
            logger.info("findResourceData")
            result_findResourceData = findResourceData(rootFolderId, type, meetCourseId, uuid, cookies=cookies)
            assert result_findResourceData.response.status_code == 200
            if result_findResourceData.response.status_code == 200:
                logger.info("筛选type为{}，筛选结果为{}".format(type, result_findResourceData.response.json()["rt"]))
        else:
            logger.info("没有正在开启的见面课")

        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_zhs_findResourceData.py"])
