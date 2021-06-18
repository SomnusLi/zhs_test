from core.result_base import ResultBase
from api.user.user import user
from common.logger import logger
from common.filedValueGenerate import get_current_time


def aidMenuAuth(uuid, cookies):
    """
    根据用户uuid，返回用户权限
    """
    result = ResultBase()
    payload = {
        "uuid": uuid,
        "date": get_current_time()
    }
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    res = user.aidMenuAuth(data=payload, headers=header, cookies=cookies)
    result.success = False
    if res.json()["status"] == "200":
        result.success = True
        # result.token = res.json()["login_info"]["token"]
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["status"], res.json()["msg"])
    result.msg = res.json()
    result.response = res
    logger.info("登录用户 ==>> 返回权限 ==>> {}".format(result.response.json()["rt"]))
    return result
