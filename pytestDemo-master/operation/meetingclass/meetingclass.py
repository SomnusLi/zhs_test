import time

from core.result_base import ResultBase
from api.meetingclass.meetingclass import MeetingClass
from common.logger import logger
from common.filedValueGenerate import randomRangeNum, get_current_time


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
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
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
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def onlineservice_getStartingMeetCourseList(uuid, cookies):
    """
    根据用户uuid，返回正在进行中的见面课信息 教师端

    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    json = {
        "uuid": uuid,
        "role": 1,
        "date": get_current_time()
        # 调用来源，0：学生(知到)，1：老师（教师圈）
    }

    res = MeetingClass.onlineservice_getStartingMeetCourseList(data=json, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
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
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
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
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def creatMeetCourse(uuid, courseId, classIds, recruitId, cookies):
    """
    创建见面课

    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    res = MeetingClass.creatMeetCourse(courseId, classIds, recruitId, randomRangeNum(3, 10), uuid, headers=header,
                                       cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def endMeetCourse(meetCourseId, uuid, cookies):
    """
    结束见面课

    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    res = MeetingClass.endMeetCourse(meetCourseId, uuid, headers=header,
                                     cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def findMeetCourseMsg(meetCourseId, uuid, cookies):
    """
    查询见面课基本信息

    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    res = MeetingClass.findMeetCourseMsg(meetCourseId, uuid, headers=header,
                                         cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def findMeetCourseLiveStatus(meetCourseId, uuid, cookies):
    """
    查询见面课直播信息

    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "meetCourseId": meetCourseId,
        "role": 1,  # 用户角色 1 老师 2 学生
        "fromType": 1,  # 设备 1 pc 2 app 3 h5 非必填 默认2
        "uuid": uuid
    }
    res = MeetingClass.findMeetCourseLiveStatus(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def findMeetcourseUserAuthData(uuid, schoolId, meetCourseId, cookies):
    """
    查询见面课用户直播权限

    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "meetCourseId": meetCourseId,
        "schoolId": schoolId,  # 非必填
        "isFrom": 0,  # 非必填 0默认 1直播分享
        "uuid": uuid
    }
    res = MeetingClass.findMeetcourseUserAuthData(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def findOnGoingSignIdsAndRushQuestionId(uuid, groupId, cookies):
    """
    查询见面课下进行的签到和提问

    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    res = MeetingClass.findOnGoingSignIdsAndRushQuestionId(uuid, groupId, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def findRecentViewFile(meetCourseId, uuid, cookies):
    """
    查询见面课最近打开的课堂文件

    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    res = MeetingClass.findRecentViewFile(meetCourseId, uuid, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def getHuanxinUserMessage(uuid, cookies):
    """
    获取环信用户信息

    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    res = MeetingClass.getHuanxinUserMessage(uuid, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def getChatroomIdByGroupId(groupId, cookies):
    """
    根据群组id获取群聊id
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    res = MeetingClass.getChatroomIdByGroupId(groupId, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def upIsHandAndSpeechByMeetingCourseId(isHandUp, meetCourseId, uuid, isInteractiveSpeech, cookies):
    """
    更新直播是否允许举手和发言
    """
    list_change = ["0", "2", "1"]
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "meetCourseId": meetCourseId,
        "uuid": uuid,
        "isHandUp": list_change[isHandUp],
        "isInteractiveSpeech": list_change[isInteractiveSpeech]
    }
    res = MeetingClass.upIsHandAndSpeechByMeetingCourseId(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def checkMeetCourseLivingAuthByUuid(uuid, cookies):
    """
    查询老师是否进行了直播认证
    """

    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "uuid": uuid
    }
    res = MeetingClass.checkMeetCourseLivingAuthByUuid(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def verifyMembershipFunctionPermissions(type, uuid, cookies):
    """
    校验用户的功能权限
    """

    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    res = MeetingClass.verifyMembershipFunctionPermissions(type, uuid, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def startMeetingCourseLiving(groupId, openLiveFromType, meetCourseId, uuid, cookies):
    """
    开启直播
    """

    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "groupId": groupId,
        "openLiveFromType": openLiveFromType,
        "meetCourseId": meetCourseId,
        "uuid": uuid
    }
    res = MeetingClass.startMeetingCourseLiving(data=data,
                                                headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def saveMeetCourseLivingPcFlag(meetCourseId, courseId, uuid, cookies):
    """
    开启直播按钮 保存直播标识 -pc
    """

    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "meetCourseId": meetCourseId,
        "courseId": courseId,
        "uuid": uuid
    }
    res = MeetingClass.saveMeetCourseLivingPcFlag(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def endMeetingCourseLiving(meetCourseId, openLiveFromType, uuid, cookies):
    """
    关闭直播
    """

    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "meetCourseId": meetCourseId,
        "openLiveFromType": openLiveFromType,
        "uuid": uuid
    }
    res = MeetingClass.endMeetingCourseLiving(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def getMeetCourseLivingShareUrl(meetCourseId, teacherName, uuid, cookies):
    """
    查询直播分享链接
    """

    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "meetCourseId": meetCourseId,
        "teacherName": teacherName,
        "uuid": uuid
    }
    res = MeetingClass.getMeetCourseLivingShareUrl(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.json()["text"])
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def saveMeetCourseLivingShareUrl(shareUrl, isType, meetCourseId, dataId, id, uuid, cookies):
    """
    保存见面课直播分享链接
    """

    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "meetCourseId": meetCourseId,
        "shareUrl": shareUrl,
        "isType": isType,
        "dataId": dataId,
        "id": id,
        "uuid": uuid
    }
    res = MeetingClass.saveMeetCourseLivingShareUrl(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def isCloseBarrage(meetCourseId, uuid, cookies):
    """
    查询弹幕是否关闭
    """

    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "meetCourseId": meetCourseId,
        "uuid": uuid
    }
    res = MeetingClass.isCloseBarrage(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def openOrCloseBarrage(meetCourseId, status, uuid, cookies):
    """
    更改弹幕开始状态
    """

    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "meetCourseId": meetCourseId,
        "status": status,
        "uuid": uuid
    }
    res = MeetingClass.openOrCloseBarrage(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def isOpen(groupId, uuid, cookies):
    """
    查询是否开启讨论
    """

    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    res = MeetingClass.isOpen(groupId, uuid, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def openOrClose(groupId, status, uuid, cookies):
    """
    开启/关闭讨论
    """

    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "groupId": groupId,
        "status": status,
        "uuid": uuid
    }
    res = MeetingClass.openOrClose(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def findHistoryMsg(chatroomId, pageSize, uuid, cookies):
    """
    查询讨论的历史消息
    """

    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "chatroomId": chatroomId,
        "pageSize": pageSize,
        "uuid": uuid
    }
    res = MeetingClass.findHistoryMsg(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def screenCourseClassInteractionListV2(courseClassId, page, pageSize, uuid, cookies):
    """
    查询讨论的历史消息
    """

    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "courseClassId": courseClassId,
        "page": page,
        "pageSize": pageSize,
        "uuid": uuid
    }
    res = MeetingClass.screenCourseClassInteractionListV2(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def findMeetCourseStudentInfo(groupId, meetCourseId, courseId, uuid, cookies):
    """
    查询见面课下的学生相关信息
    """

    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    res = MeetingClass.findMeetCourseStudentInfo(groupId, meetCourseId, courseId, uuid, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def teacherQRCodeLink(uuid, cookies):
    """
    扫码进入课堂
    """

    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"uuid": uuid}
    res = MeetingClass.teacherQRCodeLink(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def raiseHandsUserIdList(meetCourseId, uuid, cookies):
    """
    查询举手的学生id列表
    """

    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    res = MeetingClass.raiseHandsUserIdList(meetCourseId, uuid, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def findOpenMikeList(meetCourseId, meetCourseLivingId, courseId, uuid, cookies):
    """
    查询打开麦克风的学生信息列表
    """

    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    res = MeetingClass.findOpenMikeList(meetCourseId, meetCourseLivingId, courseId, uuid, headers=header,
                                        cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def chatCreateCheck(groupId, checkType, checkDurationTime, checkGesture, locationName,
                    longitude, latitude, checkRangeMetre, uuid, cookies):
    """
    创建签到
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "groupId": groupId,
        "checkType": checkType,
        "checkDurationTime": checkDurationTime,
        "checkGesture": checkGesture,
        "locationName": locationName,
        "longitude": longitude,
        "latitude": latitude,
        "checkRangeMetre": checkRangeMetre,
        "uuid": uuid
    }
    res = MeetingClass.chatCreateCheck(data=data, headers=header,
                                       cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def signUserIdsHistory(checkId, checkType, userName, groupId, uuid, cookies):
    """
    查询已签未签学生的相关信息
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "checkId": checkId,
        "checkType": checkType,
        "userName": userName,
        "groupId": groupId,
        "uuid": uuid
    }
    res = MeetingClass.signUserIdsHistory(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def chatCheckInfo(checkId, uuid, cookies):
    """
    查询签到信息详情
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "checkId": checkId,
        "uuid": uuid
    }
    res = MeetingClass.chatCheckInfo(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def findUserInfoByUserIds(uuids, groupId, uuid, cookies):
    """
    通过学生uuids查询签到/未签的学生相关信息
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "uuids": uuids,
        "groupId": groupId,
        "uuid": uuid,
        "dateFormate": int(round(time.time() * 1000))

    }
    res = MeetingClass.findUserInfoByUserIds(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def chatCheckStatus(checkId, checkType, sUuid, signRemark, uuid, cookies):
    """
    更改学生签到状态
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "checkId": checkId,
        "checkType": checkType,
        "uuid": uuid,
        "sUuid": sUuid,
        "signRemark": signRemark
    }
    res = MeetingClass.chatCheckStatus(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def chatDeleteCheck(checkId, uuid, cookies):
    """
    删除签到
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "checkId": checkId,
        "uuid": uuid
    }
    res = MeetingClass.chatDeleteCheck(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["message"])
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result
