from core.result_base import ResultBase
from api.course.course import Course
from common.logger import logger
from common.filedValueGenerate import get_current_time


def get_courseInfo_student(uuid, cookies):
    """
    根据用户uuid，返回课程信息 学生端

    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json"
    }

    res = Course.getcourselist_student(uuid, get_current_time(), headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("该学生获取课程列表 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def get_courseInfo_teacher(uuid, cookies):
    """
    根据用户uuid，返回课程信息 教师端

    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json"
    }

    res = Course.getcourselist_teacher(uuid, get_current_time(), headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["status"], res.json()["message"])
    result.msg = res.json()
    result.response = res
    logger.info("该老师获取课程列表 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def getRecruitIdByCourseId(courseId, cookies):
    """
    根据课程id，返回招生id 教师端

    """
    print(cookies)
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }

    res = Course.getRecruitIdByCourseId(courseId, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["status"], res.json()["message"])
    result.msg = res.json()
    result.response = res
    logger.info("该课程的招生id ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def aidTeachingCourseListV4(access_token, uuid):
    """
    app获取老师的课程列表
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_token": access_token
    }
    data = {
        "uuid": uuid
    }
    res = Course.aidTeachingCourseListV4(data=data, headers=header)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def aidTeachingCourseClasses_app(access_token, recruitId, uuid):
    """
    app查询用户课程下的班级
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_token": access_token
    }
    data = {
        "uuid": uuid,
        "recruitId": recruitId,
        "pageNum": 0,
        "pageSize": 100
    }
    res = Course.aidTeachingCourseClasses_app(data=data, headers=header)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result
