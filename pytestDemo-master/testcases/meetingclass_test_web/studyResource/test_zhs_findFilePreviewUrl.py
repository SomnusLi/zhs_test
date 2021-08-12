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
class Test_findFilePreviewUrl():
    """查询web端见面课投屏地址"""

    @allure.story("见面课学习资源")
    @allure.description("查询web端见面课投屏地址")
    @allure.issue("https://www.zhihuishu.com/", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.zhihuishu.com/", name="点击，跳转到对应用例的链接地址")
    @allure.title("查询web端见面课投屏地址")
    @pytest.mark.single
    def test_zhs_findFilePreviewUrl(self, login_fixture_teacher):
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
            logger.info("开启直播的courseId为{}".format(courseId))
            logger.info("findRecentViewFile")
            result_findRecentViewFile = findRecentViewFile(meetCourseId, uuid, cookies=cookies)
            assert result_findRecentViewFile.response.status_code == 200
            if result_findRecentViewFile.response.status_code == 200:
                logger.info("最近打开的文件数量为{}".format(result_findRecentViewFile.response.json()["rt"]["fileNum"]))
                if result_findRecentViewFile.response.json()["rt"]["fileNum"] == 0:
                    logger.info("没有打开的课件")
                else:
                    dataId = result_findRecentViewFile.response.json()["rt"]["dataList"][0]["sourceId"]
                    fileId = result_findRecentViewFile.response.json()["rt"]["dataList"][0]["dataId"]
                    fileSource = 2  # 1.学习资源 2.课堂文件
                    result_findFilePreviewUrl = findFilePreviewUrl(dataId, fileId, fileSource, meetCourseId, courseId,
                                                                   uuid, cookies=cookies)
                    assert result_findFilePreviewUrl.response.status_code == 200
                    logger.info(result_findFilePreviewUrl.response.json()["rt"])
        else:
            logger.info("没有正在开启的见面课")

        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_zhs_findFilePreviewUrl.py"])
