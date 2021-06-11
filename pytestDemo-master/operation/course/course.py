from core.result_base import ResultBase
from api.course.course import Course
from common.logger import logger
from common.filedValueGenerate import get_current_time


def get_courseInfo_student(uuid, cookies):
    """
    根据用户uuid，返回课程信息 学生端

    """
    print(cookies)
    result = ResultBase()
    header = {
        "Content-Type": "application/json"
    }

    res = Course.getcourselist_student(uuid, get_current_time(), headers=header, cookies=cookies)
    result.success = False
    if res.json()["code"] == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()
    result.response = res
    logger.info("该学生获取课程列表 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result

def get_courseInfo_teacher(uuid, cookies):
    """
    根据用户uuid，返回课程信息 教师端

    """
    print(cookies)
    result = ResultBase()
    header = {
        "Content-Type": "application/json"
    }

    res = Course.getcourselist_teacher(uuid, get_current_time(), headers=header, cookies=cookies)
    result.success = False
    if res.json()["status"] == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["status"], res.json()["message"])
    result.msg = res.json()
    result.response = res
    logger.info("该老师获取课程列表 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result
