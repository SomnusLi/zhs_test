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
class Test_finishCoursePrepare():
    """app完成备课卡片"""

    @allure.story("互动-备课")
    @allure.description("app完成备课卡片")
    @allure.title("app完成备课卡片")
    @pytest.mark.single
    def test_zhs_finishCoursePrepare(self, login_fixture_teacher_app):
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
            logger.info("findMeetCourseAndPrepareData")
            result_findMeetCourseAndPrepareData = findMeetCourseAndPrepareData(meetCourseId, access_token=access_token)
            assert result_findMeetCourseAndPrepareData.response.status_code == 200
            if result_findMeetCourseAndPrepareData.response.status_code == 200:
                parentId = result_findMeetCourseAndPrepareData.response.json()["rt"]
                logger.info("当前见面课备课id为：{}".format(parentId))
                result_findCoursePrepareChildenApp = findCoursePrepareChildenApp(parentId, uuid,
                                                                                 access_token=access_token)
                assert result_findCoursePrepareChildenApp.response.status_code == 200
                if result_findCoursePrepareChildenApp.response.status_code == 200:
                    if result_findCoursePrepareChildenApp.response.json()["rt"]["CoursePreparList"] != "":
                        for CoursePreparList in result_findCoursePrepareChildenApp.response.json()["rt"][
                            "CoursePreparList"]:
                            logger.info("该备课下的子卡片为：{}".format(CoursePreparList))
                        coursePreparId = \
                            random.sample(result_findCoursePrepareChildenApp.response.json()["rt"]["CoursePreparList"],
                                          1)[
                                0]["id"]
                        result_findCoursePrepareDetail = findCoursePrepareDetail(coursePreparId, meetCourseId, uuid,
                                                                                 access_token=access_token)
                        assert result_findCoursePrepareDetail.response.status_code == 200
                        if result_findCoursePrepareDetail.response.status_code == 200:
                            logger.info("该备课卡片的详细信息为：{}".format(
                                result_findCoursePrepareDetail.response.json()["rt"]["coursePrepar"]))
                            if result_findCoursePrepareDetail.response.json()["rt"]["coursePrepar"][
                                "coursePreparOperater"] != None:
                                logger.info("该备课卡片已经完成")
                            else:
                                publishStatus = 2  # 2是完成
                                operateTime = int(round(time.time() * 1000))
                                intervalTime = randomRangeNum(0, result_findCoursePrepareDetail.response.json()["rt"][
                                    "coursePrepar"]["planTime"])
                                result_saveCoursePrepareOperater = saveCoursePrepareOperater(coursePreparId,
                                                                                             intervalTime,
                                                                                             publishStatus, operateTime,
                                                                                             uuid,
                                                                                             meetCourseId,
                                                                                             access_token=access_token)
                                assert result_saveCoursePrepareOperater.response.status_code == 200
                                logger.info("返回信息为：{}".format(result_saveCoursePrepareOperater.response.json()["rt"]))
                    else:
                        logger.info("该备课没有子卡片")

        else:
            logger.info("没有正在开启的见面课")
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_zhs_finishCoursePrepare.py"])
