from core.result_base import ResultBase
from api.user.user import user
from common.logger import logger
from common.filedValueGenerate import get_current_time


def getLoginInfo(cookies):
    """
    根据用户uuid，返回用户权限
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json"
    }
    res = user.getLoginInfo(headers=header, cookies=cookies)
    result.success = False
    if res.json()["code"] == "200":
        result.success = True
        # result.token = res.json()["login_info"]["token"]
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["msg"])
    result.msg = res.json()
    result.response = res
    # logger.info("登录用户 ==>> 返回权限 ==>> {}".format(result.response.json()["rt"]))
    return result


def queryTeacherSchoolId(uuid, cookies):
    """
    根据用户uuid，返回用户学校信息
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json"
    }
    res = user.queryTeacherSchoolId(uuid, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
        # result.token = res.json()["login_info"]["token"]
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["msg"])
    result.msg = res.json()
    result.response = res
    # logger.info("登录用户 ==>> 返回权限 ==>> {}".format(result.response.json()["rt"]))
    return result
