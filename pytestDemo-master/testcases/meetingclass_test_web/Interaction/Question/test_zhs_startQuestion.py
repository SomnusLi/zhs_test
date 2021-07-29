import pytest
import allure
from operation.course.course import *
from operation.meetingclass.meetingclass import *
from testcases.conftest import api_data
from common.logger import logger
from common.filedValueGenerate import add_cookies, randomRangeNum
import requests


@allure.step("前置登录步骤 ==>> 用户登录")
def step_login(account, uuid):
    logger.info("前置登录步骤 ==>> 用户 {} 登录 ==>> 返回的 uuid 为：{}".format(account, uuid))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("见面课模块")
@allure.feature("web教师端")
class Test_startQuestion():
    """创建答疑"""

    @allure.story("互动-答疑")
    @allure.description("创建答疑")
    @allure.issue("https://www.zhihuishu.com/", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.zhihuishu.com/", name="点击，跳转到对应用例的链接地址")
    @allure.title("创建答疑")
    @pytest.mark.single
    def test_zhs_startQuestion(self, login_fixture_teacher):
        logger.info("*************** 开始执行用例 ***************")
        # login_fixture前置登录
        user_info = login_fixture_teacher
        uuid = user_info.json().get("uuid")
        account = user_info.request.body[8:19]
        step_login(account, uuid)
        cookies = add_cookies(requests.utils.dict_from_cookiejar(user_info.cookies))
        result_get_courseInfo_teacher = get_courseInfo_teacher(uuid,
                                                               cookies=cookies)

        assert result_get_courseInfo_teacher.response.status_code == 200
        result_onlineservice_getStartingMeetCourseList = onlineservice_getStartingMeetCourseList(uuid,
                                                                                                 cookies=cookies)
        assert result_onlineservice_getStartingMeetCourseList.response.status_code == 200
        if result_onlineservice_getStartingMeetCourseList.response.json()["rt"] != []:
            logger.info("有正在开启的见面课")
            meetCourseId = result_onlineservice_getStartingMeetCourseList.response.json()["rt"][0]["meetCourseId"]
            courseClassId = meetCourseId
            logger.info("findMeetCourseMsg")
            result_findMeetCourseMsg = findMeetCourseMsg(meetCourseId, uuid,
                                                         cookies=cookies)
            assert result_findMeetCourseMsg.response.status_code == 200
            groupId = result_findMeetCourseMsg.response.json()["rt"]["groupId"]
            courseId = result_findMeetCourseMsg.response.json()["rt"]["courseId"]
            logger.info("checkExistQuestion")
            result_checkExistQuestion = checkExistQuestion(groupId, uuid, cookies=cookies)
            assert result_checkExistQuestion.response.status_code == 200
            logger.info("getRecruitIdByCourseId")
            result_getRecruitIdByCourseId = getRecruitIdByCourseId(courseId, cookies=cookies)
            assert result_getRecruitIdByCourseId.response.status_code == 200
            recruitId = result_getRecruitIdByCourseId.msg
            if result_checkExistQuestion.response.json()["rt"]["result"] == 1:
                rushQuestionId = result_checkExistQuestion.response.json()["rt"]["rushQuestionId"]
                logger.info("有正在进行中的提问，提问id为{}".format(rushQuestionId))
            elif result_checkExistQuestion.response.json()["rt"]["result"] == 2:
                logger.info("没有正在进行的提问")
                anonymous = randomRangeNum(1, 2)  # 是否允许学生之间匿名 1：允许 2：不允许
                result_startQuestion = startQuestion(anonymous, groupId, courseClassId, uuid, recruitId,
                                                     cookies=cookies)
                assert result_startQuestion.response.status_code == 200
                if result_startQuestion.response.json()["rt"]["resultStatus"] == 1:
                    logger.info("{}，创建的答疑id为{}".format(result_startQuestion.response.json()["rt"]["resultMessage"],
                                                       result_startQuestion.response.json()["rt"]["rushQuestionId"]))
            else:
                logger.info("提问已结束")

        else:
            logger.info("没有正在开启的见面课")
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_zhs_startQuestion.py"])
