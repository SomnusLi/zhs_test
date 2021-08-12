import time

from core.result_base import ResultBase
from api.meetingclass.meetingclass import MeetingClass
from common.logger import logger
from common.filedValueGenerate import randomRangeNum, get_current_time


def getUserRoleByCourseId(uuid, courseId, cookies):
    """
    根据用户uuid，返回课程权限信息 教师端

    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json"
    }

    res = MeetingClass.getUserRoleByCourseId(uuid, courseId, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def getStartingMeetCourseList(uuid, courseId, cookies):
    """
    根据用户uuid，返回正在进行中的见面课信息 教师端

    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "courseId": courseId,
        "uuid": uuid,
        "role": 1
        # 调用来源，0：学生(知到)，1：老师（教师圈）
    }

    res = MeetingClass.getStartingMeetCourseList(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
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
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def getMeetCourseTeacherSetting(uuid, courseId, cookies):
    """
    根据用户uuid，返回见面课时是否需要审核的默认设置 教师端

    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    json = {
        "courseId": courseId,
        "uuid": uuid,
        "role": 1
        # 调用来源，0：学生(知到)，1：老师（教师圈）
    }

    res = MeetingClass.getMeetCourseTeacherSetting(data=json, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
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
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
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
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def endMeetCourse(meetCourseId, uuid, cookies=None, access_token=None):
    """
    结束见面课

    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_token": access_token
    }

    res = MeetingClass.endMeetCourse(meetCourseId, uuid, headers=header,
                                     cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
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
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def findMeetCourseLiveStatus(meetCourseId, role, fromType, uuid, cookies=None, access_token=None):
    """
    查询见面课直播信息

    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_token": access_token
    }
    data = {
        "meetCourseId": meetCourseId,
        "role": role,  # 用户角色 1 老师 2 学生
        "fromType": fromType,  # 设备 1 pc 2 app 3 h5 非必填 默认2
        "uuid": uuid
    }
    res = MeetingClass.findMeetCourseLiveStatus(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
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
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
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
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
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
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
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
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
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
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
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
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
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
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
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
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
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
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
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
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
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
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
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
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
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
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def openOrCloseBarrage(meetCourseId, status, uuid, cookies):
    """
    更改弹幕开启状态
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
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
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
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
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
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
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
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
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
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
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
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def teacherQRCodeLink(uuid, cookies=None, access_token=None):
    """
    扫码进入课堂
    """

    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_token": access_token
    }
    data = {"uuid": uuid}
    res = MeetingClass.teacherQRCodeLink(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
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
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
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
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
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
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
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
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
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
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
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
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
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
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
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
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def checkExistQuestion(groupId, uuid=None, cookies=None, access_token=None):
    """
    查询是否存在进行中的提问
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_token": access_token
    }
    data = {
        "groupId": groupId,
        "uuid": uuid
    }
    res = MeetingClass.checkExistQuestion(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def findMeetCourseHours(meetCourseId, uuid, cookies):
    """
    查询见面课时长
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    res = MeetingClass.findMeetCourseHours(meetCourseId, uuid, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def startQuestion(anonymous, groupId, courseClassId, uuid, recruitId, cookies):
    """
    创建答疑
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "anonymous": anonymous,
        "groupId": groupId,
        "courseClassId": courseClassId,
        "uuid": uuid,
        "recruitId": recruitId
    }
    res = MeetingClass.startQuestion(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def countJoinNum(rushQuestionId, uuid, cookies):
    """
    统计讨论参与人数
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "rushQuestionId": rushQuestionId,
        "uuid": uuid
    }
    res = MeetingClass.countJoinNum(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def openQuestionDetail(rushQuestionId, uuid, cookies):
    """
    查询答疑详情
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "rushQuestionId": rushQuestionId,
        "uuid": uuid
    }
    res = MeetingClass.openQuestionDetail(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def checkQuestionAndJoinNum(rushQuestionId, uuid, cookies):
    """
    查询问题总数量和参与人数
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "rushQuestionId": rushQuestionId,
        "uuid": uuid
    }
    res = MeetingClass.checkQuestionAndJoinNum(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def questionListAll(pageSize, pageNum, rushQuestionId, uuid, sequenceType=None, cookies=None, access_token=None):
    """
    提问下的问题列表
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_token": access_token
    }
    data = {
        "pageSize": pageSize,
        "pageNum": pageNum,
        "sequenceType": sequenceType,
        "rushQuestionId": rushQuestionId,
        "uuid": uuid
    }
    res = MeetingClass.questionListAll(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def closeQuestion(rushQuestionId, groupId, uuid, cookies):
    """
    关闭答疑
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "groupId": groupId,
        "rushQuestionId": rushQuestionId,
        "uuid": uuid
    }
    res = MeetingClass.closeQuestion(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def getSimpleBrainStormList(groupId, type, pageSize, pageNum, uuid, cookies):
    """
    查询头脑风暴列表
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    res = MeetingClass.getSimpleBrainStormList(groupId, type, pageSize, pageNum, uuid, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def startRollcall(groupId, count, uuid, cookies):
    """
    开始点名
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "groupId": groupId,
        "count": count,
        "uuid": uuid
    }
    res = MeetingClass.startRollcall(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def quryRollcallDetail(rollcallId, uuid, cookies):
    """
    查询随机点名结果
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "rollcallId": rollcallId,
        "uuid": uuid
    }
    res = MeetingClass.quryRollcallDetail(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def changeRollcall(rollcallId, uuid, cookies):
    """
    随机点名换一批
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "rollcallId": rollcallId,
        "uuid": uuid
    }
    res = MeetingClass.changeRollcall(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def chatVotePublishFastVote(groupId, type, optionCount, limitTime, uuid, cookies):
    """
    快速创建投票
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "groupIds": groupId,
        "type": type,
        "optionCount": optionCount,
        "limitTime": limitTime,
        "uuid": uuid
    }
    res = MeetingClass.chatVotePublishFastVote(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def chatVoteDetail(voteId, uuid, cookies):
    """
    查询投票详情
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "voteId": voteId,
        "uuid": uuid
    }
    res = MeetingClass.chatVoteDetail(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def getGroupMemberCount(groupId, uuid, cookies):
    """
    查询群组数量
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "groupId": groupId,
        "uuid": uuid
    }
    res = MeetingClass.getGroupMemberCount(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def chatVoteDetailOptionCount(groupId, voteId, uuid, cookies):
    """
    查询投票选项信息
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "groupId": groupId,
        "voteId": voteId,
        "uuid": uuid
    }
    res = MeetingClass.chatVoteDetailOptionCount(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def chatVoteDetailOptionVotersList(optionId, voteId, uuid, cookies):
    """
    查询投票选项对应的投票人信息情况
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "optionIds": optionId,
        "voteId": voteId,
        "uuid": uuid
    }
    res = MeetingClass.chatVoteDetailOptionVotersList(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def unpublishedChatVotesList(groupId, uuid, cookies):
    """
    查询待发布投票列表
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "groupId": groupId,
        "uuid": uuid
    }
    res = MeetingClass.unpublishedChatVotesList(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def chatDeleteVote(voteId, uuid, cookies):
    """
    删除投票
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "voteId": voteId,
        "uuid": uuid
    }
    res = MeetingClass.chatDeleteVote(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def findRunningPreemptive(groupId, uuid, cookies):
    """
    查询群下正在进行的抢答
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "groupId": groupId,
        "uuid": uuid
    }
    res = MeetingClass.findRunningPreemptive(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def startRushAnswer(groupId, count, uuid, cookies):
    """
    创建抢答
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "groupId": groupId,
        "count": count,
        "uuid": uuid
    }
    res = MeetingClass.startRushAnswer(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def quryRushAnswerDetail(groupId, rushAnswerId, uuid, cookies):
    """
    查询抢答详细
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "groupId": groupId,
        "rushAnswerId": rushAnswerId,
        "uuid": uuid
    }
    res = MeetingClass.quryRushAnswerDetail(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def endRushAnswer(groupId, rushAnswerId, uuid, cookies):
    """
    结束抢答
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "groupId": groupId,
        "rushAnswerId": rushAnswerId,
        "uuid": uuid
    }
    res = MeetingClass.endRushAnswer(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def findFilePreviewUrl(dataId, fileId, fileSource, meetCourseId, courseId, uuid, cookies):
    """
    查询web端见面课投屏地址
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    res = MeetingClass.findFilePreviewUrl(dataId, fileId, fileSource, meetCourseId, courseId, uuid, headers=header,
                                          cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def getOnline(groupId, cookies):
    """
    学生在线情况
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    res = MeetingClass.getOnline(groupId, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def openOrCloseStudentMike(studentId, groupId, meetCourseLivingId, meetCourseId, type, uuid, cookies):
    """
    邀请学生上/下麦
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    res = MeetingClass.openOrCloseStudentMike(studentId, groupId, meetCourseLivingId, meetCourseId, type, uuid,
                                              headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def getStartingMeetCourseList_app(access_token, uuid):
    """
    返回正在进行中的见面课信息 教师app端

    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_token": access_token
    }
    data = {
        "uuid": uuid,
        "role": 1
        # 调用来源，0：学生(知到)，1：老师（教师圈）
    }
    res = MeetingClass.getStartingMeetCourseList(data=data, headers=header)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def getMeetCourseTeacherSetting_app(access_token, courseId, uuid):
    """
    app查询见面课审核状态
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_token": access_token
    }
    data = {
        "uuid": uuid,
        "courseId": courseId

    }
    res = MeetingClass.getMeetCourseTeacherSetting_app(data=data, headers=header)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def updateMeetCourseTeacherSetting_app(access_token, courseId, isAuditMeetingCourse, uuid):
    """
    app更改见面课审核状态
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_token": access_token
    }
    data = {
        "uuid": uuid,
        "courseId": courseId,
        "isAuditMeetingCourse": 1 if isAuditMeetingCourse == 0 else 0

    }
    res = MeetingClass.updateMeetCourseTeacherSetting_app(data=data, headers=header)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def createMeetCourse_app(access_token, classIds, courseId, hours, recruitId, uuid):
    """
    app创建见面课
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_token": access_token
    }
    data = {
        "uuid": uuid,
        "courseId": courseId,
        "classIds": classIds,
        "hours": hours,
        "recruitId": recruitId

    }
    res = MeetingClass.createMeetCourse_app(data=data, headers=header)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def getMeetCourseInfo_app(access_token, meetCourseId, role, uuid):
    """
    app查询正在进行中的见面课信息
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_token": access_token
    }
    data = {
        "uuid": uuid,
        "meetCourseId": meetCourseId,
        "role": role
    }
    res = MeetingClass.getMeetCourseInfo_app(data=data, headers=header)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def saveOrGetBottomTypeRequest_app(access_token, type, uuid, typeStr=None):
    """
    app查询/修改常用工具列表
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_token": access_token
    }
    data = {
        "uuid": uuid,
        "type": type,
        "typeStr": typeStr
    }
    res = MeetingClass.saveOrGetBottomTypeRequest_app(data=data, headers=header)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def screenCourseClassInteractionListV2_app(access_token, courseClassId, page, pageSize, showClassType, uuid):
    """
    app获取互动列表
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_token": access_token
    }
    data = {
        "uuid": uuid,
        "courseClassId": courseClassId,
        "page": page,
        "pageSize": pageSize,
        "showClassType": showClassType
    }
    res = MeetingClass.screenCourseClassInteractionListV2_app(data=data, headers=header)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def chatGroupPersonalUserInfo_app(access_token, groupId, uuid):
    """
    app查询群聊信息
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_token": access_token
    }
    data = {
        "uuid": uuid,
        "groupId": groupId
    }
    res = MeetingClass.chatGroupPersonalUserInfo_app(data=data, headers=header)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def findMeetCourseLoginUrl_app(access_token):
    """
    app获取扫码投屏地址
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_token": access_token
    }
    res = MeetingClass.findMeetCourseLoginUrl_app(headers=header)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def checkExistQuestion_app(groupId, uuid=None, cookies=None, access_token=None):
    """
    app查询是否存在进行中的提问
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_token": access_token
    }
    data = {
        "groupId": groupId,
        "uuid": uuid
    }
    res = MeetingClass.checkExistQuestion_app(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def startQuestion_app(anonymous, groupId, recruitId, uuid, access_token):
    """
    app创建答疑
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_token": access_token
    }
    data = {
        "anonymous": anonymous,
        "groupId": groupId,
        "uuid": uuid,
        "recruitId": recruitId
    }
    res = MeetingClass.startQuestion_app(data=data, headers=header)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def closeQuestion_app(rushQuestionId, uuid, access_token):
    """
    app关闭答疑
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_token": access_token
    }
    data = {
        "rushQuestionId": rushQuestionId,
        "uuid": uuid
    }
    res = MeetingClass.closeQuestion_app(data=data, headers=header)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def openQuestionDetail_app(rushQuestionId, access_token):
    """
    app查询答疑详情
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_token": access_token
    }
    data = {
        "rushQuestionId": rushQuestionId
    }
    res = MeetingClass.openQuestionDetail_app(data=data, headers=header)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def saveBarrageOpenStatus_app(rushQuestionId, openStatus, access_token):
    """
    app开/关答疑弹幕
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_token": access_token
    }
    data = {
        "rushQuestionId": rushQuestionId,
        "openStatus": openStatus
    }
    res = MeetingClass.saveBarrageOpenStatus_app(data=data, headers=header)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def questionList_app(pageSize, pageNum, rushQuestionId, sequenceType, access_token=None):
    """
    app提问下的问题列表
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_token": access_token
    }
    data = {
        "pageSize": pageSize,
        "pageNum": pageNum,
        "rushQuestionId": rushQuestionId,
        "sequenceType": sequenceType
    }
    res = MeetingClass.questionList_app(data=data, headers=header)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def findBarrageOpenStatus_app(rushQuestionId, cookies=None, access_token=None):
    """
    app查询答疑弹幕开关状态
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_token": access_token
    }
    data = {
        "rushQuestionId": rushQuestionId
    }
    res = MeetingClass.findBarrageOpenStatus_app(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def checkQuestionAndJoinNum_app(rushQuestionId, cookies=None, access_token=None):
    """
    app查询问题总数量和参与人数
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_token": access_token
    }
    data = {
        "rushQuestionId": rushQuestionId
    }
    res = MeetingClass.checkQuestionAndJoinNum_app(data=data, headers=header, cookies=cookies)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def getAnswerOrTroubleNum_app(questionId, access_token):
    """
    app提问有疑惑/想回答人数
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_token": access_token
    }
    data = {
        "questionId": questionId
    }
    res = MeetingClass.getAnswerOrTroubleNum_app(data=data, headers=header)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def questionDetail_app(groupId, questionId, recruitId, uuid, access_token):
    """
    app提问下的问题详情
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_token": access_token
    }
    data = {
        "questionId": questionId,
        "groupId": groupId,
        "recruitId": recruitId,
        "uuid": uuid
    }
    res = MeetingClass.questionDetail_app(data=data, headers=header)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def answerOrTroubleMemberList_app(groupId, pageNum, pageSize, questionId, type, access_token):
    """
    app问题想回答/有疑问学生列表
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_token": access_token
    }
    data = {
        "questionId": questionId,
        "pageNum": pageNum,
        "pageSize": pageSize,
        "type": type,
        "groupId": groupId
    }
    res = MeetingClass.answerOrTroubleMemberList_app(data=data, headers=header)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def updateQuestionToQa_app(groupId, questionId, recruitId, rushQuestionId, uuid, access_token):
    """
    app同步问题至问答
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_token": access_token
    }
    data = {
        "questionId": questionId,
        "groupId": groupId,
        "recruitId": recruitId,
        "rushQuestionId": rushQuestionId,
        "uuid": uuid
    }
    res = MeetingClass.updateQuestionToQa_app(data=data, headers=header)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def getGroupMemberCount_app(groupId, uuid, access_token):
    """
    app查询群组数量
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_token": access_token
    }
    data = {
        "groupId": groupId,
        "uuid": uuid
    }
    res = MeetingClass.getGroupMemberCount_app(data=data, headers=header)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def startRollcall_app(count, groupId, uuid, access_token):
    """
    app开始随机点名
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_token": access_token
    }
    data = {
        "groupId": groupId,
        "uuid": uuid,
        "count": count
    }
    res = MeetingClass.startRollcall_app(data=data, headers=header)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def changeRollcall_app(rollcallId, uuid, access_token):
    """
    app随机点名换一换
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_token": access_token
    }
    data = {
        "rollcallId": rollcallId,
        "uuid": uuid
    }
    res = MeetingClass.changeRollcall_app(data=data, headers=header)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def findRunningPreemptive_app(groupId, uuid, access_token):
    """
    app获取正在进行中的抢答
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_token": access_token
    }
    data = {
        "groupId": groupId,
        "uuid": uuid
    }
    res = MeetingClass.findRunningPreemptive_app(data=data, headers=header)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def startRushAnswer_app(count, groupId, uuid, access_token):
    """
    app创建抢答
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_token": access_token
    }
    data = {
        "groupId": groupId,
        "uuid": uuid,
        "count": count
    }
    res = MeetingClass.startRushAnswer_app(data=data, headers=header)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def endRushAnswer_app(rushAnswerId, groupId, uuid, access_token):
    """
    app结束抢答
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_token": access_token
    }
    data = {
        "groupId": groupId,
        "uuid": uuid,
        "rushAnswerId": rushAnswerId
    }
    res = MeetingClass.endRushAnswer_app(data=data, headers=header)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def quryRushAnswerDetail_app(rushAnswerId, groupId, uuid, access_token):
    """
    app查询抢答详细
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_token": access_token
    }
    data = {
        "groupId": groupId,
        "uuid": uuid,
        "rushAnswerId": rushAnswerId
    }
    res = MeetingClass.quryRushAnswerDetail_app(data=data, headers=header)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def findCoursePrepareApp(uuid, access_token):
    """
    app查询备课计划
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_token": access_token
    }
    data = {
        "uuid": uuid
    }
    res = MeetingClass.findCoursePrepareApp(data=data, headers=header)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def saveCoursePrepareOperater(coursePreparId, intervalTime, publishStatus, operateTime, uuid, meetCourseId,
                              access_token):
    """
    app保存备课状态
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_token": access_token
    }
    data = {
        "uuid": uuid,
        "coursePreparId": coursePreparId,
        "intervalTime": intervalTime,
        "publishStatus": publishStatus,
        "operateTime": operateTime,
        "meetCourseId": meetCourseId
    }
    res = MeetingClass.saveCoursePrepareOperater(data=data, headers=header)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def findMeetCourseAndPrepareData(meetCourseId, access_token):
    """
    app查询当前见面课备课id
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_token": access_token
    }
    data = {
        "meetCourseId": meetCourseId
    }
    res = MeetingClass.findMeetCourseAndPrepareData(data=data, headers=header)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def updateMeetCourseAndPrepare(coursePreparId, meetCourseId, access_token):
    """
    app更新当前见面课备课id
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_token": access_token
    }
    data = {
        "meetCourseId": meetCourseId,
        "coursePreparId": coursePreparId
    }
    res = MeetingClass.updateMeetCourseAndPrepare(data=data, headers=header)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def findCoursePrepareChildenApp(parentId, uuid, access_token):
    """
    app查询当前备课计划的所有子卡片
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_token": access_token
    }
    data = {
        "parentId": parentId,
        "uuid": uuid
    }
    res = MeetingClass.findCoursePrepareChildenApp(data=data, headers=header)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def findCoursePrepareDetail(coursePreparId, meetCourseId, uuid, access_token):
    """
    app查看备课卡片的详细信息
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "access_token": access_token
    }
    data = {
        "coursePreparId": coursePreparId,
        "meetCourseId": meetCourseId,
        "uuid": uuid
    }
    res = MeetingClass.findCoursePrepareDetail(data=data, headers=header)
    result.success = False
    if res.status_code == 200:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.text)
    result.msg = res.json()
    result.response = res
    logger.info("查询结果 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result
