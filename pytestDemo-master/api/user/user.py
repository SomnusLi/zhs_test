import os
from core.rest_client import RestClient
from common.read_data import data

# 文件路径 上级目录
BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
api_root_url = data.load_ini(data_file_path)["host"]["api_root_url"]


class User(RestClient):

    def __init__(self, api_root_url, **kwargs):
        super(User, self).__init__(api_root_url, **kwargs)

    def login(self, **kwargs):
        # 用户登录接口
        return self.post("https://passport.zhihuishu.com/user/validateAccountAndPassword", **kwargs)

    def aidMenuAuth(self, **kwargs):
        # 获取用户权限接口
        return self.post("https://fteaching.zhihuishu.com/login/aidMenuAuth", **kwargs)

    def getLoginInfo(self, **kwargs):
        # 获取用户登录信息
        return self.get("https://onlineservice.zhihuishu.com/login/getLoginUserInfo", **kwargs)

    def login_dd(self, **kwargs):
        # 用户登录接口
        return self.post("https://passport.zhihuishu.com/login", **kwargs)


user = User(api_root_url)
