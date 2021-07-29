# import pytest
# import allure
#
# from operation.user.login import zhs_login
# from testcases.conftest import api_data
# from common.logger import logger
#
#
# @allure.step("步骤1 ==>> 登录")
# def step_1():
#     logger.info("步骤1 ==>> 登录")
#
#
# # @allure.step("步骤1 ==>> 获取某个用户信息")
# # def step_2(username):
# #     logger.info("步骤1 ==>> 获取某个用户信息：{}".format(username))
#
#
# @allure.severity(allure.severity_level.TRIVIAL)
# @allure.epic("针对单个接口的测试")
# @allure.feature("获取用户信息模块")
# class TestzhsLogin():
#     """用户登录"""
#
#     @allure.story("模拟用户登录的test测试")
#     @allure.description("该用例用户登录的test测试")
#     @allure.issue("https://passport.zhihuishu.com/user/validateAccountAndPassword", name="点击，跳转到对应BUG的链接地址")
#     @allure.testcase("https://passport.zhihuishu.com/user/validateAccountAndPassword", name="点击，跳转到对应用例的链接地址")
#     @pytest.mark.single
#     @pytest.mark.parametrize("account,password,except_result, except_status, except_msg",
#                              api_data["test_zhs_login"])
#     def test_zhs_login(self, account, password, except_result, except_status, except_msg):
#         logger.info("*************** 开始执行用例 ***************")
#         step_1()
#         # account = "13592540004"
#         # password = "Aa123456"
#         # except_result = True
#         # except_status = 1
#         # except_msg = {'pwd': 'df4da95099ee4510a4fabea36b430c9c', 'uuid': 'EY6W3opP', 'status': 1}
#         result = zhs_login(account, password)
#         # print(result.__dict__)
#         assert result.response.status_code == 200
#         assert result.success == except_result, result.error
#         logger.info("code ==>> 期望结果：{}， 实际结果：{}".format(except_status, result.response.json().get("status")))
#         assert result.response.json().get("status") == except_status
#         # assert set(six.viewitems(except_msg)).issubset(set(six.viewitems(result.msg)))
#         logger.info("*************** 结束执行用例 ***************")
#
#     # @allure.story("获取某个用户信息")
#     # @allure.description("该用例是针对获取单个用户信息接口的测试")
#     # @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
#     # @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
#     # @allure.title("【 {username}，{except_result}，{except_code}，{except_msg} 】")
#     # @pytest.mark.single
#     # @pytest.mark.parametrize("username, except_result, except_code, except_msg",
#     #                          api_data["test_get_get_one_user_info"])
#
#
# if __name__ == '__main__':
#     pytest.main(["-v", "-s", "test_zhs_Login.py"])
