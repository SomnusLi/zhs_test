import pytest
import allure
from operation.course.course import get_courseInfo_teacher
from operation.meetingclass.meetingclass import verifyMembershipFunctionPermissions
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
class Test_verifyMembershipFunctionPermissions():
    """校验用户的功能权限"""

    @allure.story("见面课信息")
    @allure.description("校验用户的功能权限")
    @allure.issue("https://www.zhihuishu.com/", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.zhihuishu.com/", name="点击，跳转到对应用例的链接地址")
    @allure.title("校验用户的功能权限")
    @pytest.mark.single
    def test_zhs_verifyMembershipFunctionPermissions(self, login_fixture_teacher):
        logger.info("*************** 开始执行用例 ***************")
        # login_fixture前置登录
        user_info = login_fixture_teacher
        uuid = user_info.uuid
        account = user_info.account
        step_login(account, uuid)
        cookies = user_info.cookies
        type = "3&8"
        # 功能点id：1.资源库会员 2.资源库选课会员 3.视频直播(手机版) 4.直播白板 5.直播录屏 6.师说会员 7.数据中心 8.设备直播(手机端) 9.金课评审会员 10.共享题库 11.管理者教学指挥中心 12.数据联动 13.单点登录 14.学校门户(PC版本) 15.学校门户(手机版本) 16.防作弊管理 17.校内加速 18.定制服务 19.专业版期末报告 20.校资源库 21.校内spoc教学 22.视频监考 23.AI监考
        result_verifyMembershipFunctionPermissions = verifyMembershipFunctionPermissions(type, uuid,
                                                                                         cookies=cookies)
        assert result_verifyMembershipFunctionPermissions.response.status_code == 200
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_zhs_verifyMembershipFunctionPermissions.py"])
