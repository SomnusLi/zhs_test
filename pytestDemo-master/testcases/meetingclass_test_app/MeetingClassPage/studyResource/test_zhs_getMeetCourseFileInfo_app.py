import pytest
import allure
from operation.meetingclass.meetingclass import *
from testcases.conftest import api_data
from common.logger import logger
from operation.studyResources.studyResources import *
import requests


@allure.step("前置登录步骤 ==>> 用户登录")
def step_login(account, uuid):
    logger.info("前置登录步骤 ==>> 用户 {} 登录 ==>> 返回的 uuid 为：{}".format(account, uuid))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("见面课模块")
@allure.feature("app教师端")
class Test_getMeetCourseFileInfo_app():
    """app查询当前投屏文件信息"""

    @allure.story("见面课学习资源")
    @allure.description("app查询当前投屏文件信息")
    @allure.title("app查询当前投屏文件信息")
    @pytest.mark.single
    def test_zhs_getMeetCourseFileInfo_app(self, login_fixture_teacher_app):
        logger.info("*************** 开始执行用例 ***************")
        # login_fixture前置登录
        user_info_app = login_fixture_teacher_app
        uuid = user_info_app.json()["rt"]["loginInfo"]["uuId"]
        account = user_info_app.request.body[8:19]
        access_token = user_info_app.json()["rt"]["access_token"]
        step_login(account, uuid)
        logger.info("getStartingMeetCourseList_app")
        result_getStartingMeetCourseList_app = getStartingMeetCourseList_app(access_token, uuid)
        assert result_getStartingMeetCourseList_app.response.status_code == 200
        if result_getStartingMeetCourseList_app.response.json()["rt"] != []:
            logger.info("有正在开启的见面课")
            meetCourseId = result_getStartingMeetCourseList_app.response.json()["rt"][0]["meetCourseId"]
            pageNum = 0
            pageSize = -1  # -1表示当前投屏的课件
            logger.info("getMeetCourseFileList_app")
            result_getMeetCourseFileList_app = getMeetCourseFileList_app(access_token, meetCourseId, pageNum, pageSize,
                                                                         uuid)
            assert result_getMeetCourseFileList_app.response.status_code == 200
            dataId = result_getMeetCourseFileList_app.response.json()["rt"]["dataList"][0]["dataId"]
            logger.info("getMeetCourseFileInfo_app.py")
            result_getMeetCourseFileInfo_app = getMeetCourseFileInfo_app(access_token, dataId, meetCourseId, uuid)
            assert result_getMeetCourseFileInfo_app.response.status_code == 200
            logger.info("见面课当前投屏课件为：{}".format(result_getMeetCourseFileInfo_app.response.json()["rt"]))
        else:
            logger.info("没有正在开启的见面课")
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_zhs_getMeetCourseFileInfo_app.py"])
