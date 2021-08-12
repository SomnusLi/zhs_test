import os
from core.rest_client import RestClient
from common.read_data import data
from common.filedValueGenerate import get_current_time

# 文件路径 上级目录
BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
api_root_url = data.load_ini(data_file_path)["host"]["api_root_url"]


class User(RestClient):

    def __init__(self, api_root_url, **kwargs):
        super(User, self).__init__(api_root_url, **kwargs)

    def login(self, **kwargs):
        # 用户登录接口
        return self.post(
            "https://passport.zhihuishu.com/user/validateAccountAndPassword?u_asec=099%23KAFEDYEyTpUEhYTLEEEEEpEQz0yFZ6AcDrBoV6AESuOYW6gHSu9qD6NwSYFEJFwlsyaSJXZg%2FonEaKB8Cf8VAM8jv3k64yZTvblxE7E5I3lP%2F37fkpStY0s3YuaHLyZTvbtXE7EFD67EEHQTEEi5DEEEfYFE19dIHOGUp3d8QHQTEEi5DEEEVEFET6imEEwUE7TxEm29EF2d0xEGctgMXREYqiYWvHNlUJ6%2FIhikLweI3kj2qMDBKy0zMJ61ZANrNJ5U0HzqamydRhj2qYDB6OT2qLHoLQtrLLIDB1A0DLL4BwSQRoMTESlkcGE%2FaquYSpXfNV9c1e95zqbVcLD7%2F6kdCyxVaElW8y%2FkNa26%2BsniWV%2BCc5dqPtRzYiUWaUsAGuJxUKIulu2Ydoc2h5c6rP2tSspV1SW%2BCs9xHanqwRaK%2FoQSrLZprtyAGVU07dZsnRni4gvl3zRDrtXnbGA6dUXRWLedaY%2Fzn9pJOsw3Lyl2rUoo8adlQIB%2BY0MMxbrZ8uw0qVLtGcJmVbbaqssRsIlb%2BgCC1S%2FCgQ%2FerypcLOnxrUoM8Ik14qL8P%2B2nTFpjZR%2BceyolGQywUc8CroXR%2FPBPOV28jdCgsQwihgbulscwQQItcIt6PU2bVi24g3uFAeJ6pTvI%2FzljNrhZ8dk6UbW4nw5C%2Bo2Rur1er2kJ1pyCVs1%2FKQihzzWLNyXe9QibPXkCbR2F1OWcQUYUpM%2FtVeuDVRYZAE2rCu1Q8yxKgUJjUK4ebqjRbucaDxkoEdxqWeBLzaC1FKR7UXMoUIrKPVhglO1VwI%2FzZXh%2F6edICQ%2FeVKFLIotFNeXTQVMz7Yn8DpXxr0%2BhgUwD%2FPb%2BKIPqruiPNWoVjbkg4Vnyc1Xw1s%2FUv344qATpU%2FZ4Dz%2BYEdChlKaGcTYh9uw0v9E23IbHQ2kR%2Fy2%2Bwss%2BbMhSOR%2B6LQsduMc26HEqLrXCtL2W%2FScFPVJo%2F147L0%2Fd4revedbhr6%2FvY%2B48lP1%2B4M9XIx4lTc1Z4tFtIG118dZwtwCZAMe2S09ZpAzlL2sUzdWeUQVJN91JSs%2BnxFaveI1Cb2q7T2i3V0cWrGdFz92WSyc%2FLSCobMaKPxOciOJT42E%2BrYYIvlrsZeey9vW6%2FyRDPxgcjVsKN%2FXv8q26VOXNGwhvaY%2BJCVLKUOYuxeiublM8PbwtQKigSRG2wnWZYWamrzv6ayJ5PdSV8I3Rsfk8txZeEFibNzw9ILRE1u1BYbXAKd2pvdeQCedDaN1%2BV29CP%2Bb7YV%2BYrcryULdwPbCGleI4YUuQ%2BO3Tp1X6xpBKrfQAUdQEgRcndRcvgScCVsJ0cLOcLrsTuQrGrMscrd8YLLSSwqCgCp93rgXpLy8kr6XaPFZTzdp8SRxA1GhdCpw7rjDt9y%2Fmr6FnbUQRzP1tnOIB5qCtD2JIri733y9Mr0MZPQbqrzkanw2n%2BGCWsEFEp3llsyaSt3llllle33iS1pRlluUdt37qn3llWLaStEGdllle33iSwwAoE7EIlllbAdC5aoyrE7EhT3l%2F%2FonljYFET%2FdEsyaSt3QTEEjtBKlVBYFET6i5EEw5E7EFlllbrfITEE9lluZdtJZPfYFE19dqQyGzp9d%2BZnMTEEvl1H1dqa3lKrnxE7EJlllP%2F37mwPITEE9lluZdtTRhMYFEwCEEsyGfJpDjC0h9SzBQ4fITETEYluZdtTSGOmJK%2BqW2ushjMYFEwCwlsyGfweDjC0h9SzBQ4fITETqbluZdtTDQN2hD%2BX8JQbkDYyhIuYFEw3dI0sS2h%2FlllW6r%2FHQTEEi5DEEE&u_atype=2",
            **kwargs)

    def aidMenuAuth(self, **kwargs):
        # 获取用户权限接口
        return self.post("https://fteaching.zhihuishu.com/login/aidMenuAuth", **kwargs)

    def getLoginInfo(self, **kwargs):
        # 获取用户登录信息
        return self.get("https://onlineservice.zhihuishu.com/login/getLoginUserInfo", **kwargs)

    def queryTeacherSchoolId(self, uuid, **kwargs):
        # 获取用户登录学校
        return self.get(
            "https://onlineservice.zhihuishu.com/teacher/index/queryTeacherSchoolId?uuid={}&date={}".format(uuid,
                                                                                                            get_current_time()),
            **kwargs)

    def zhs_app_login(self, **kwargs):
        # app用户登录接口
        return self.post("https://appteacher.zhihuishu.com/appteacher/teacher/base/newLoginTeacherAppV2", **kwargs)


user = User(api_root_url)
