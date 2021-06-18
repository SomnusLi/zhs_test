from core.result_base import ResultBase
from api.meetingclass.meetingclass import MeetingClass
from common.logger import logger
from common.filedValueGenerate import get_current_time


def getUserRoleByCourseId(uuid, couresId, cookies):
    """
    根据用户uuid，返回课程权限信息 教师端

    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json"
    }

    res = MeetingClass.getUserRoleByCourseId(uuid, couresId, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()
    result.response = res
    logger.info("权限查询 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def getStartingMeetCourseList(uuid, couresId, cookies):
    """
    根据用户uuid，返回正在进行中的见面课信息 教师端

    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    json = {
        "courseId": couresId,
        "uuid": uuid,
        "role": 1
        # 调用来源，0：学生(知到)，1：老师（教师圈）
    }

    res = MeetingClass.getStartingMeetCourseList(data=json, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()
    result.response = res
    logger.info("权限查询 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def getMeetCourseTeacherSetting(uuid, couresId, cookies):
    """
    根据用户uuid，返回见面课时是否需要审核的默认设置 教师端

    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    json = {
        "courseId": couresId,
        "uuid": uuid,
        "role": 1
        # 调用来源，0：学生(知到)，1：老师（教师圈）
    }

    res = MeetingClass.getMeetCourseTeacherSetting(data=json, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()
    result.response = res
    logger.info("权限查询 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def getSelectClassInfo(uuid, recruitId, cookies):
    """
    根据用户uuid，返回见面课时是否需要审核的默认设置 教师端

    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    res = MeetingClass.getSelectClassInfo(recruitId, uuid, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()
    result.response = res
    logger.info("权限查询 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


