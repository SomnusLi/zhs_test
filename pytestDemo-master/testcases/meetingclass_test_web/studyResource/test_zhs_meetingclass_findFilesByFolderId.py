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




@allure.step("前置登录步骤 ==>> 用户登录")
def step_login(account, uuid):
    logger.info("前置登录步骤 ==>> 用户 {} 登录 ==>> 返回的 uuid 为：{}".format(account, uuid))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("见面课模块")
@allure.feature("web教师端")
class Test_meetingclass_findFilesByFolderId():
    """查询见面课选择资源列表当前层级下文件目录"""

    @allure.story("见面课学习资源")
    @allure.description("查询见面课选择资源列表当前层级下文件目录")
    @allure.issue("https://www.zhihuishu.com/", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.zhihuishu.com/", name="点击，跳转到对应用例的链接地址")
    @allure.title("查询见面课选择资源列表当前层级下文件目录")
    @pytest.mark.single
    def test_zhs_meetingclass_findFilesByFolderId(self, login_fixture_teacher):
        logger.info("*************** 开始执行用例 ***************")
        # login_fixture前置登录
        user_info = login_fixture_teacher
        uuid = user_info.uuid
        account = user_info.account
        step_login(account, uuid)
        cookies = user_info.cookies
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
            logger.info("findLastOpenFile")
            result_findLastOpenFile = findLastOpenFile(courseId, uuid, cookies=cookies)
            assert result_findLastOpenFile.response.status_code == 200
            if result_findLastOpenFile.response.status_code == 200:
                if result_findLastOpenFile.response.json()["rt"] == None:
                    logger.info("见面课没有打开过文件")
                else:
                    logger.info("见面课下最后打开的文件id为：{}".format(result_findLastOpenFile.response.json()["rt"]["fileId"]))
                    folderId = result_findLastOpenFile.response.json()["rt"]["parentIds"][-1]
                    # 最后打开文件的目录
                    logger.info("findFilesByFolderId")
                    result_findFilesByFolderId = findFilesByFolderId(courseId, folderId, uuid, cookies=cookies)
                    assert result_findFilesByFolderId.response.status_code == 200
                    if result_findFilesByFolderId.response.status_code == 200:
                        logger.info("最后打开文件的目录为{}".format(result_findFilesByFolderId.response.json()["rt"]))
        else:
            logger.info("没有正在开启的见面课")
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_zhs_meetingclass_findFilesByFolderId.py"])
