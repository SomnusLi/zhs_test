import random

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
class Test_importOneFileToMeetCourse_app():
    """app选择文件投屏"""

    @allure.story("见面课学习资源")
    @allure.description("app选择文件投屏")
    @allure.title("app选择文件投屏")
    @pytest.mark.single
    def test_zhs_importOneFileToMeetCourse_app(self, login_fixture_teacher_app):
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
            role = 1
            logger.info("getMeetCourseInfo_app")
            result_getMeetCourseInfo_app = getMeetCourseInfo_app(access_token, meetCourseId, role, uuid)
            assert result_getMeetCourseInfo_app.response.status_code == 200
            courseId = result_getMeetCourseInfo_app.response.json()["rt"]["courseId"]
            logger.info("aidTeachingFolderId_app")
            result_aidTeachingFolderId_app = aidTeachingFolderId_app(access_token, courseId, uuid)
            assert result_aidTeachingFolderId_app.response.status_code == 200
            rootFolderId = result_aidTeachingFolderId_app.response.json()["rt"]["folderId"]
            logger.info("本课程学习资源根目录为：{}".format(rootFolderId))
            logger.info("findResourceData_app")
            result_findResourceData_app = findResourceData_app(access_token, rootFolderId, uuid)
            assert result_findResourceData_app.response.status_code == 200
            logger.info("该课程下学习资源为：{}".format(result_findResourceData_app.response.json()["rt"]["fileInfo"]))
            dataIds = []
            if result_findResourceData_app.response.json()["rt"]["fileInfo"] != []:
                for FirstList in result_findResourceData_app.response.json()["rt"]["fileInfo"]:
                    for dataIdList in FirstList["fileList"]:
                        dataIds.append(dataIdList["dataId"])
                logger.info("dataIds:{}".format(dataIds))
                dataId = random.sample(dataIds, 1)
                result_importOneFileToMeetCourse_app = importOneFileToMeetCourse(meetCourseId, dataId, uuid,
                                                                                 access_token=access_token)
                assert result_importOneFileToMeetCourse_app.response.status_code == 200
                if result_importOneFileToMeetCourse_app.response.status_code == 200:
                    logger.info("导入信息为：{}".format(result_importOneFileToMeetCourse_app.response.json()["rt"]))
            else:
                logger.info("该课程下没有学习资源")
        else:
            logger.info("没有正在开启的见面课")
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_zhs_importOneFileToMeetCourse_app.py"])
