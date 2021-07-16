from core.result_base import ResultBase
from api.studyResources.studyResources import studyResources
from common.logger import logger
from common.filedValueGenerate import get_current_time
import time


def findFolderMenu(courseId, uuid, cookies):
    """
    查询课程下学习资源目录
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json"
    }

    res = studyResources.findFolderMenu(courseId, uuid, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询课程下学习资源目录 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def queryAllFileCount(courseId, uuid, cookies):
    """
    查询课程下学习资源总数
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "courseId": courseId,
        "uuid": uuid,
        "dateFormate": int(round(time.time() * 1000))
    }
    res = studyResources.queryAllFileCount(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def findLastOpenFile(courseId, uuid, cookies):
    """
    查询见面课最后打开的文件
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    res = studyResources.findLastOpenFile(courseId, uuid, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def findFilesByFolderId(courseId, folderId, uuid, cookies):
    """
    根据FolderId查找目录下文件
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json"
    }

    res = studyResources.findFilesByFolderId(courseId, folderId, uuid, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def importOneFileToMeetCourse(meetCourseId, dataId, uuid, cookies):
    """
    选择学习资源里的文件
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "meetCourseId": meetCourseId,
        "dataId": dataId,
        "uuid": uuid,
        "dateFormate": int(round(time.time() * 1000))
    }
    res = studyResources.importOneFileToMeetCourse(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def canUseFile(fileId, role, sourceId, courseId, uuid, cookies):
    """
    查询见面课课件使用权限
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    res = studyResources.canUseFile(fileId, role, sourceId, courseId, uuid, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result
