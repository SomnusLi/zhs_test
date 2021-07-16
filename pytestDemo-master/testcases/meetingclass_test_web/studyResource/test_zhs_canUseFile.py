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
class Test_canUseFile():
    """查询见面课课件使用权限"""

    @allure.story("用例--查询见面课课件使用权限")
    @allure.description("该用例是查询见面课课件使用权限")
    @allure.issue("https://hikeservice.zhihuishu.com/student/course/aided/getMyCourseLis", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://hikeservice.zhihuishu.com/student/course/aided/getMyCourseLis", name="点击，跳转到对应用例的链接地址")
    @allure.title("测试数据：上游业务获取")
    @pytest.mark.single
    def test_zhs_canUseFile(self, login_fixture_teacher):
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
            logger.info("开启直播的courseId为{}".format(courseId))
            logger.info("findRecentViewFile")
            result_findRecentViewFile = findRecentViewFile(meetCourseId, uuid, cookies=cookies)
            assert result_findRecentViewFile.response.status_code == 200
            if result_findRecentViewFile.response.status_code == 200:
                logger.info("最近打开的文件数量为{}".format(result_findRecentViewFile.response.json()["rt"]["fileNum"]))
                if result_findRecentViewFile.response.json()["rt"]["fileNum"] == 0:
                    logger.info("没有打开的课件")
                else:
                    sourceId = result_findRecentViewFile.response.json()["rt"]["dataList"][0]["sourceId"]
                    fileId = result_findRecentViewFile.response.json()["rt"]["dataList"][0]["dataId"]
                    role = 1
                    result_canUseFile = canUseFile(fileId, role, sourceId, courseId, uuid, cookies=cookies)
                    assert result_canUseFile.response.status_code == 200
                    if result_canUseFile.response.status_code == 200:
                        if result_canUseFile.response.json()["rt"]["fileStatus"] == 0:
                            logger.info("该资源可以正常使用")
                        elif result_canUseFile.response.json()["rt"]["fileStatus"] == 1:
                            logger.info(result_canUseFile.response.json()["rt"]["title"])
                        else:
                            logger.info(result_canUseFile.response.json()["rt"]["title"] + "  " +
                                        result_canUseFile.response.json()["rt"]["describe"])
        else:
            logger.info("没有正在开启的见面课")

        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_zhs_canUseFile.py"])
