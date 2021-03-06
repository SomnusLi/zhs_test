from core.result_base import ResultBase
from api.user.user import user
from common.logger import logger


def zhs_login(account, password):
    """
    登录用户
    :param account: 用户名
    :param password: 密码
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    payload = {
        "account": account,
        "password": password
    }
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    res = user.login(data=payload, headers=header)
    result.success = False
    if res.json()["status"] == 1:
        result.success = True
        # result.token = res.json()["login_info"]["token"]
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["status"], res.json()["msg"])
    result.msg = res.json()
    result.response = res
    logger.info("登录用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def zhs_app_login(account, password):
    """
    app用户登录
    """
    result = ResultBase()
    data = {
        "account": account,
        "password": password,
        "clientType": 1,
        "appVersion": "4.4.8"
    }
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Connection": "Keep-Alive",
        "Content-Length": "67",
        "Host": "appteacher.zhihuishu.com"
    }
    res = user.zhs_app_login(data=data, headers=header)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result
