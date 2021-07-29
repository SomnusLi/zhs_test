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
@allure.epic("见面课模块")
@allure.feature("web教师端")
class Test_importOneFileToMeetCourse():
    """选择学习资源里的文件"""

    @allure.story("见面课学习资源")
    @allure.description("选择学习资源里的文件")
    @allure.issue("https://www.zhihuishu.com/", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.zhihuishu.com/", name="点击，跳转到对应用例的链接地址")
    @allure.title("选择学习资源里的文件")
    @pytest.mark.single
    def test_zhs_importOneFileToMeetCourse(self, login_fixture_teacher):
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
                logger.info("课程目录为{}".format(result_findFolderMenu.response.json()["rt"]))
            FolderListAll = []
            # 遍历所有目录 拿出所有的FolderId
            # 根目录
            logger.info("queryAllFileCount")
            result_queryAllFileCount = queryAllFileCount(courseId, uuid, cookies=cookies)
            assert result_queryAllFileCount.response.status_code == 200
            if result_queryAllFileCount.response.status_code == 200:
                logger.info("课程下资源总数为{}".format(result_queryAllFileCount.response.json()["rt"]))
            if result_queryAllFileCount.response.json()["rt"] != 0:
                for FolderList in result_findFolderMenu.response.json()["rt"]:
                    FolderListAll.append(FolderList["id"])
                    logger.info(FolderList)
                    if FolderList["childs"] != None:
                        # 1级目录
                        for FolderList_childs_1 in FolderList["childs"]:
                            FolderListAll.append(FolderList_childs_1["id"])
                            logger.info(FolderList_childs_1)
                            if FolderList_childs_1["childs"] != None:
                                # 2级目录
                                for FolderList_childs_2 in FolderList_childs_1["childs"]:
                                    FolderListAll.append(FolderList_childs_2["id"])
                                    logger.info(FolderList_childs_2)
                                    if FolderList_childs_2["childs"] != None:
                                        # 3级目录 如果有
                                        for FolderList_childs_3 in FolderList_childs_2["childs"]:
                                            FolderListAll.append(FolderList_childs_3["id"])
                                            logger.info(FolderList_childs_3)
                logger.info(FolderListAll)
                # 随机取folderId 根据folderId 随机取dataId
                Flag_Folder = True
                while Flag_Folder:
                    folderId = random.sample(FolderListAll, 1)[0]
                    logger.info("findFilesByFolderId")
                    result_findFilesByFolderId = findFilesByFolderId(courseId, folderId, uuid, cookies=cookies)
                    assert result_findFilesByFolderId.response.status_code == 200
                    if result_findFilesByFolderId.response.status_code == 200:
                        logger.info("选择的目录为{}".format(result_findFilesByFolderId.response.json()["rt"]))
                        if result_findFilesByFolderId.response.json()["rt"] != []:
                            Flag_Folder = False
                            logger.info(result_findFilesByFolderId.response.json()["rt"])
                            # fileId 对应dataId！！！！！！！！！！误导人！！！
                            dataId = random.sample(result_findFilesByFolderId.response.json()["rt"], 1)[0]["fileId"]
                            logger.info("dataId是{}".format(dataId))
                logger.info("importOneFileToMeetCourse")
                result_importOneFileToMeetCourse = importOneFileToMeetCourse(meetCourseId, dataId, uuid,
                                                                             cookies=cookies)
                assert result_importOneFileToMeetCourse.response.status_code == 200
                if result_importOneFileToMeetCourse.response.status_code == 200:
                    logger.info("导入信息为：{}".format(result_importOneFileToMeetCourse.response.json()["rt"]))

            else:
                logger.info("该课程下没有资源可选择")
        else:
            logger.info("没有正在开启的见面课")
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_zhs_importOneFileToMeetCourse.py"])
