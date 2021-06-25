import os
import time

from core.rest_client import RestClient
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
api_root_url = data.load_ini(data_file_path)["host"]["api_root_url"]


class MeetingClass(RestClient):

    def __init__(self, api_root_url, **kwargs):
        super(MeetingClass, self).__init__(api_root_url, **kwargs)

    def getUserRoleByCourseId(self, uuid, courseId, **kwargs):
        # 获取开启见面课权限
        # get方式url直接拼接 {}.format（）
        return self.get(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/webMeetCourse/atUser/getUserRoleByCourseId?courseId={}&uuid={}&dateFormate={}".format(
                courseId, uuid, int(round(time.time() * 1000))),
            **kwargs)

    def getStartingMeetCourseList(self, **kwargs):
        # 获取正在进行中的见面课
        return self.post(
            "https://app-hike.zhihuishu.com/appAidedteaching/webMeetCourse/meetCourse/getStartingMeetCourseList",
            **kwargs)

    def onlineservice_getStartingMeetCourseList(self, **kwargs):
        # 获取正在进行中的见面课
        return self.post(
            "https://onlineservice.zhihuishu.com/teacherMeetCourse/getStartingMeetCourseList",
            **kwargs)

    def getMeetCourseTeacherSetting(self, **kwargs):
        # 获取见面课是否需要审核设置
        return self.post(
            "https://app-hike.zhihuishu.com/appAidedteaching/meetCourse/getMeetCourseTeacherSetting",
            **kwargs)

    def getSelectClassInfo(self, recruitId, uuid, **kwargs):
        # 获取选择课程的信息
        # get方式url直接拼接 {}.format（）
        return self.get(
            "https://app-hike.zhihuishu.com/appAidedteaching/webMeetCourse/meetCourse/getSelectClassInfo?recruitId={}&uuid={}&dateFormate={}".format(
                recruitId, uuid, int(round(time.time() * 1000))),
            **kwargs)

    def creatMeetCourse(self, courseId, classIds, recruitId, hours, uuid, **kwargs):
        # 创建见面课
        return self.get(
            "https://app-hike.zhihuishu.com/appAidedteaching/webMeetCourse/meetCourse/createMeetCourse?courseId={}&classIds={}&recruitId={}&hours={}&uuid={}&dateFormate={}".format(
                courseId, classIds, recruitId, hours, uuid, int(round(time.time() * 1000))),
            **kwargs)

    def endMeetCourse(self, meetCourseId, uuid, **kwargs):
        # 结束见面课
        return self.get(
            "https://app-hike.zhihuishu.com/appAidedteaching/webMeetCourse/meetCourse/endMeetCourseClass?meetCourseId={}&uuid={}&dateFormate={}".format(
                meetCourseId, uuid, int(round(time.time() * 1000))),
            **kwargs)

    def findMeetCourseMsg(self, meetCourseId, uuid, **kwargs):
        # 查询见面课基本信息
        return self.get(
            "https://app-hike.zhihuishu.com/appAidedteaching/webMeetCourse/meetCourse/findMeetCourseMsg?meetCourseId={}&uuid={}&dateFormate={}".format(
                meetCourseId, uuid, int(round(time.time() * 1000))),
            **kwargs)

    def findMeetCourseLiveStatus(self, **kwargs):
        # 查询见面课直播
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/meetingCourse/findMeetCourseLiveStatus",
            **kwargs)

    def findMeetcourseUserAuthData(self, **kwargs):
        # 查询见面课直播
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/meetingCourse/findMeetcourseUserAuthData",
            **kwargs)

    def findOnGoingSignIdsAndRushQuestionId(self, groupId, uuid, **kwargs):
        # 查询见面课下进行的签到和提问
        return self.get(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/webMeetCourse/common/findOnGoingSignIdsAndRushQuestionId?groupId={}&uuid={}&dateFormate={}".format(
                groupId, uuid, int(round(time.time() * 1000))),
            **kwargs)

    def findRecentViewFile(self, meetCourseId, uuid, **kwargs):
        # 查询见面课最近打开的课堂文件
        return self.get(
            "https://app-hike.zhihuishu.com/appAidedteaching/webMeetCourse/meetCourse/findRecentViewFile?meetCourseId={}&uuid={}&dateFormate={}".format(
                meetCourseId, uuid, int(round(time.time() * 1000))),
            **kwargs)

    def getHuanxinUserMessage(self, uuid, **kwargs):
        # 获取环信用户信息
        return self.get(
            "https://app-hike.zhihuishu.com/appAidedteaching/meetCourse/getHuanxinUserMessage?uuid={}&dateFormate={}".format(
                uuid, int(round(time.time() * 1000))),
            **kwargs)

    def getChatroomIdByGroupId(self, groupId, **kwargs):
        # 根据群组id获取群聊id
        return self.get(
            "https://app-hike.zhihuishu.com/appAidedteaching/meetCourse/getChatroomIdByGroupId?groupId={}".format(
                groupId), **kwargs)

    def upIsHandAndSpeechByMeetingCourseId(self, **kwargs):
        # 更新直播是否允许举手和发言
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/meetingCourse/upIsHandAndSpeechByMeetingCourseId",
            **kwargs)

    def checkMeetCourseLivingAuthByUuid(self, **kwargs):
        # 查询老师是否进行了直播认证
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/webMeetCourse/common/checkMeetCourseLivingAuthByUuid",
            **kwargs)

    def verifyMembershipFunctionPermissions(self, type, uuid, **kwargs):
        # 校验用户的功能权限
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/meetingCourse/verifyMembershipFunctionPermissions?functionType={}&uuid={}&dateFormate={}".format(
                type, uuid, int(round(time.time() * 1000))),
            **kwargs)

    def startMeetingCourseLiving(self, **kwargs):
        # 开启直播
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/webMeetCourse/common/startMeetingCourseLiving",
            **kwargs)

    def saveMeetCourseLivingPcFlag(self, **kwargs):
        # 开启直播按钮 保存直播标识 -pc
        return self.post(
            "https://hike.zhihuishu.com/aidedteaching/meetCourse/saveMeetCourseLivingPcFlag", **kwargs)

    def endMeetingCourseLiving(self, **kwargs):
        # 关闭直播
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/webMeetCourse/common/endMeetingCourseLiving",
            **kwargs)

    def getMeetCourseLivingShareUrl(self, **kwargs):
        # 查询直播分享链接
        return self.post(
            "https://ct.zhihuishu.com/classroomTools/live/getMeetCourseLivingShareUrl", **kwargs)

    def saveMeetCourseLivingShareUrl(self, **kwargs):
        # 保存见面课直播分享链接
        return self.post(
            "https://ct.zhihuishu.com/classroomTools/live/saveMeetCourseLivingShareUrl", **kwargs)

    def isCloseBarrage(self, **kwargs):
        # 查询弹幕是否关闭
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/barrage/isCloseBarrage", **kwargs)

    def openOrCloseBarrage(self, **kwargs):
        # 更改弹幕开始状态
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/barrage/openOrCloseBarrage", **kwargs)

    def isOpen(self, groupId, uuid, **kwargs):
        # 查询是否开启讨论
        return self.get(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/discuss/isOpen?groupId={}&uuid={}&dateFormate={}".format(
                groupId, uuid, int(round(time.time() * 1000))), **kwargs)

    def openOrClose(self, **kwargs):
        # 开启/关闭讨论
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/discuss/openOrClose", **kwargs)

    def findHistoryMsg(self, **kwargs):
        # 查询讨论的历史消息
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/discuss/findHistoryMsg", **kwargs)

    def screenCourseClassInteractionListV2(self, **kwargs):
        # 查询见面课互动列表
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/meetingCourse/screenCourseClassInteractionListV2",
            **kwargs)

    def findMeetCourseStudentInfo(self, groupId, meetCourseId, courseId, uuid, **kwargs):
        # 查询见面课下的学生相关信息
        return self.get(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/webMeetCourse/common/findMeetCourseStudentInfo?groupId={}&meetCourseId={}&courseId={}&uuid={}&dateFormate={}".format(
                groupId, meetCourseId, courseId, uuid, int(round(time.time() * 1000))),
            **kwargs)

    def teacherQRCodeLink(self, **kwargs):
        # 扫码进入课堂
        return self.post(
            "https://app-hike.zhihuishu.com/appAidedteaching/meetCourse/teacherQRCodeLink",
            **kwargs)

    def raiseHandsUserIdList(self, meetCourseId, uuid, **kwargs):
        # 查询举手的学生id列表
        return self.get(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/raiseHands/raiseHandsUserIdList?meetCourseId={}&uuid={}&dateFormate={}".format(
                meetCourseId, uuid, int(round(time.time() * 1000))),
            **kwargs)

    def findOpenMikeList(self, meetCourseId, meetCourseLivingId, courseId, uuid, **kwargs):
        # 查询打开麦克风的学生信息列表
        return self.get(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/meetCourseLive/findOpenMikeList?meetCourseId={}&meetCourseLivingId={}&courseId={}&uuid={}&dateFormate={}".format(
                meetCourseId, meetCourseLivingId, courseId, uuid, int(round(time.time() * 1000))),
            **kwargs)

    def chatCreateCheck(self, **kwargs):
        # 创建签到
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/webMeetCourse/sign/chatCreateCheck",
            **kwargs)

    def signUserIdsHistory(self, **kwargs):
        # 查询已签未签学生的相关信息
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/webMeetCourse/sign/signUserIdsHistory",
            **kwargs)

    def chatCheckInfo(self, **kwargs):
        # 查询签到信息详情
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/webMeetCourse/sign/chatCheckInfo",
            **kwargs)


MeetingClass = MeetingClass(api_root_url)
