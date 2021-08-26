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
        # 更改弹幕开启状态
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

    def findUserInfoByUserIds(self, **kwargs):
        # 通过学生uuids查询签到/未签的学生相关信息
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/webMeetCourse/sign/findUserInfoByUserIds",
            **kwargs)

    def chatCheckStatus(self, **kwargs):
        # 更改学生签到状态
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/webMeetCourse/sign/chatCheckStatus",
            **kwargs)

    def chatDeleteCheck(self, **kwargs):
        # 删除签到
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/webMeetCourse/sign/chatDeleteCheck",
            **kwargs)

    def checkExistQuestion(self, **kwargs):
        # 查询是否存在进行中的提问
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/webMeetCourse/question/checkExistQuestion",
            **kwargs)

    def findMeetCourseHours(self, meetCourseId, uuid, **kwargs):
        # 查询是否存在进行中的提问
        return self.post(
            "https://app-hike.zhihuishu.com/appAidedteaching/webMeetCourse/meetCourse/findMeetCourseHours?meetCourseId={}&uuid={}&dateFormate={}".format(
                meetCourseId, uuid, int(round(time.time() * 1000))),
            **kwargs)

    def startQuestion(self, **kwargs):
        # 创建答疑
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/webMeetCourse/question/startQuestion", **kwargs)

    def countJoinNum(self, **kwargs):
        # 统计讨论参与人数
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/webMeetCourse/question/countJoinNum", **kwargs)

    def openQuestionDetail(self, **kwargs):
        # 查询答疑详情
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/webMeetCourse/question/openQuestionDetail",
            **kwargs)

    def checkQuestionAndJoinNum(self, **kwargs):
        # 查询问题总数量和参与人数
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/webMeetCourse/question/checkQuestionAndJoinNum",
            **kwargs)

    def questionListAll(self, **kwargs):
        # 提问下的问题列表
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/webMeetCourse/question/questionListAll",
            **kwargs)

    def closeQuestion(self, **kwargs):
        # 关闭答疑
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/webMeetCourse/question/closeQuestion",
            **kwargs)

    def getSimpleBrainStormList(self, groupId, type, pageSize, pageNum, uuid, **kwargs):
        # 查询头脑风暴列表
        return self.get(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/brainStorm/getSimpleBrainStormList?groupId={}&type={}&pageSize={}&pageNum={}&uuid={}&dateFormate={}".format(
                groupId, type, pageSize, pageNum, uuid, int(round(time.time() * 1000))),
            **kwargs)

    def startRollcall(self, **kwargs):
        # 开始点名
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/webMeetCourse/group/rollCall/startRollcall",
            **kwargs)

    def quryRollcallDetail(self, **kwargs):
        # 查询随机点名结果
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/webMeetCourse/group/rollCall/quryRollcallDetail",
            **kwargs)

    def changeRollcall(self, **kwargs):
        # 随机点名换一批
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/webMeetCourse/group/rollCall/changeRollcall",
            **kwargs)

    def chatVotePublishFastVote(self, **kwargs):
        # 快速创建投票
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/webMeetCourse/vote/chatVotePublishFastVote",
            **kwargs)

    def chatVoteDetail(self, **kwargs):
        # 查询投票详情
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/webMeetCourse/vote/chatVoteDetail",
            **kwargs)

    def getGroupMemberCount(self, **kwargs):
        # 查询群组数量
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/webMeetCourse/group/rollCall/getGroupMemberCount",
            **kwargs)

    def chatVoteDetailOptionCount(self, **kwargs):
        # 查询投票选项信息
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/webMeetCourse/vote/chatVoteDetailOptionCount",
            **kwargs)

    def chatVoteDetailOptionVotersList(self, **kwargs):
        # 查询投票选项对应的投票人信息情况
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/webMeetCourse/vote/chatVoteDetailOptionVotersList",
            **kwargs)

    def unpublishedChatVotesList(self, **kwargs):
        # 查询待发布投票列表
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/webMeetCourse/vote/unpublishedChatVotesList",
            **kwargs)

    def chatDeleteVote(self, **kwargs):
        # 删除投票
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/webMeetCourse/vote/chatDeleteVote",
            **kwargs)

    def chatVotePublishAnswers(self, **kwargs):
        # 发布投票答案
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/webMeetCourse/vote/chatVotePublishAnswers",
            **kwargs)

    def findRunningPreemptive(self, **kwargs):
        # 查询群下正在进行的抢答
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/webMeetCourse/group/preemptive/findRunningPreemptive",
            **kwargs)

    def startRushAnswer(self, **kwargs):
        # 创建抢答
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/webMeetCourse/group/preemptive/startRushAnswer",
            **kwargs)

    def quryRushAnswerDetail(self, **kwargs):
        # 查询抢答详细
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/webMeetCourse/group/preemptive/quryRushAnswerDetail",
            **kwargs)

    def endRushAnswer(self, **kwargs):
        # 结束抢答
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/webMeetCourse/group/preemptive/endRushAnswer",
            **kwargs)

    def findFilePreviewUrl(self, dataId, fileId, fileSource, meetCourseId, courseId, uuid, **kwargs):
        # 查询web端见面课投屏地址
        return self.get(
            "https://app-hike.zhihuishu.com/appAidedteaching/webMeetCourse/file/findFilePreviewUrl?dataId={}&fileId={}&fileSource={}&meetCourseId={}&courseId={}&stamp={}&uuid={}&dateFormate={}".format(
                dataId, fileId, fileSource, meetCourseId, courseId, int(round(time.time() * 1000)), uuid,
                int(round(time.time() * 1000))),
            **kwargs)

    def getOnline(self, gid, **kwargs):
        # 学生在线情况
        return self.get("https://hijk.zhihuishu.com/meeting/getOnline?gid={}".format(gid), **kwargs)

    def openOrCloseStudentMike(self, studentId, groupId, meetCourseLivingId, meetCourseId, type, uuid, **kwargs):
        # 邀请学生上/下麦
        return self.get(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/meetCourseLive/openOrCloseStudentMike?studentId={}&groupId={}&meetCourseLivingId={}&meetCourseId={}&type={}&uuid={}&dateFormate={}".format(
                studentId, groupId, meetCourseLivingId, meetCourseId, type, uuid, int(round(time.time() * 1000))),
            **kwargs)

    def getMeetCourseTeacherSetting_app(self, **kwargs):
        # app查询见面课审核状态
        return self.post("https://app-hike.zhihuishu.com/appAidedteaching/meetCourse/getMeetCourseTeacherSetting",
                         **kwargs)

    def updateMeetCourseTeacherSetting_app(self, **kwargs):
        # app更改见面课审核状态
        return self.post("https://app-hike.zhihuishu.com/appAidedteaching/meetCourse/updateMeetCourseTeacherSetting",
                         **kwargs)

    def createMeetCourse_app(self, **kwargs):
        # app创建见面课
        return self.post("https://app-hike.zhihuishu.com/appAidedteaching/meetCourse/createMeetCourse", **kwargs)

    def getMeetCourseInfo_app(self, **kwargs):
        # app查询正在进行中的见面课信息
        return self.post("https://app-hike.zhihuishu.com/appAidedteaching/meetCourse/getMeetCourseInfo", **kwargs)

    def saveOrGetBottomTypeRequest_app(self, **kwargs):
        # app查询/修改常用工具列表
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/meetScreen/saveOrGetBottomTypeRequest",
            **kwargs)

    def screenCourseClassInteractionListV2_app(self, **kwargs):
        # app获取互动列表
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/meetingCourse/screenCourseClassInteractionListV2",
            **kwargs)

    def chatGroupPersonalUserInfo_app(self, **kwargs):
        # app查询群聊信息
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/group/chatGroupPersonalUserInfo",
            **kwargs)

    def findMeetCourseLoginUrl_app(self, **kwargs):
        # app获取扫码投屏地址
        return self.post(
            "https://app-hike.zhihuishu.com/appAidedteaching/webMeetCourse/meetCourse/findMeetCourseLoginUrl",
            **kwargs)

    def checkExistQuestion_app(self, **kwargs):
        # app查询是否存在进行中的提问
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/question/checkExistQuestion",
            **kwargs)

    def startQuestion_app(self, **kwargs):
        # app创建答疑
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/question/startQuestion",
            **kwargs)

    def closeQuestion_app(self, **kwargs):
        # app关闭答疑
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/question/closeQuestion",
            **kwargs)

    def openQuestionDetail_app(self, **kwargs):
        # app查询答疑详情
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/question/openQuestionDetail",
            **kwargs)

    def saveBarrageOpenStatus_app(self, **kwargs):
        # app开/关答疑弹幕
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/meetingCourse/saveBarrageOpenStatus",
            **kwargs)

    def findBarrageOpenStatus_app(self, **kwargs):
        # app查询答疑弹幕开关状态
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/meetingCourse/findBarrageOpenStatus",
            **kwargs)

    def checkQuestionAndJoinNum_app(self, **kwargs):
        # app查询问题总数量和参与人数
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/question/checkQuestionAndJoinNum",
            **kwargs)

    def questionList_app(self, **kwargs):
        # app提问下的问题列表
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/question/questionList", **kwargs)

    def getAnswerOrTroubleNum_app(self, **kwargs):
        # app提问有疑惑/想回答人数
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/question/getAnswerOrTroubleNum",
            **kwargs)

    def questionDetail_app(self, **kwargs):
        # app提问下的问题详情
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/question/questionDetail",
            **kwargs)

    def answerOrTroubleMemberList_app(self, **kwargs):
        # app问题想回答/有疑问学生列表
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/question/answerOrTroubleMemberList",
            **kwargs)

    def updateQuestionToQa_app(self, **kwargs):
        # app同步问题至问答
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/question/updateQuestionToQa",
            **kwargs)

    def getGroupMemberCount_app(self, **kwargs):
        # app查询群组数量
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/group/rollCall/getGroupMemberCount",
            **kwargs)

    def startRollcall_app(self, **kwargs):
        # app开始随机点名
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/group/rollCall/startRollcall",
            **kwargs)

    def changeRollcall_app(self, **kwargs):
        # app随机点名换一换
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/group/rollCall/changeRollcall",
            **kwargs)

    def findRunningPreemptive_app(self, **kwargs):
        # app获取正在进行中的抢答
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/group/preemptive/findRunningPreemptive",
            **kwargs)

    def startRushAnswer_app(self, **kwargs):
        # app创建抢答
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/group/preemptive/startRushAnswer",
            **kwargs)

    def endRushAnswer_app(self, **kwargs):
        # app结束抢答
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/group/preemptive/endRushAnswer",
            **kwargs)

    def quryRushAnswerDetail_app(self, **kwargs):
        # app查询抢答详细
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/group/preemptive/quryRushAnswerDetail",
            **kwargs)

    def findCoursePrepareApp(self, **kwargs):
        # app查询备课计划
        return self.post(
            "https://hike-teaching.zhihuishu.com/coursePrepare/findCoursePrepareApp",
            **kwargs)

    def saveCoursePrepareOperater(self, **kwargs):
        # app查询备课计划
        return self.post(
            "https://hike-teaching.zhihuishu.com/coursePrepare/saveCoursePrepareOperater",
            **kwargs)

    def findMeetCourseAndPrepareData(self, **kwargs):
        # app查询当前见面课备课id
        return self.post(
            "https://app-hike.zhihuishu.com/appAidedteaching/meetCourse/findMeetCourseAndPrepareData",
            **kwargs)

    def updateMeetCourseAndPrepare(self, **kwargs):
        # app更新当前见面课备课id
        return self.post(
            "https://app-hike.zhihuishu.com/appAidedteaching/meetCourse/updateMeetCourseAndPrepare",
            **kwargs)

    def findCoursePrepareChildenApp(self, **kwargs):
        # app查询当前备课计划的所有子卡片
        return self.post(
            "https://hike-teaching.zhihuishu.com/coursePrepare/findCoursePrepareChildenApp", **kwargs)

    def findCoursePrepareDetail(self, **kwargs):
        # app查看备课卡片的详细信息
        return self.post(
            "https://hike-teaching.zhihuishu.com/coursePrepare/findCoursePrepareDetail", **kwargs)

    def chatVotePublishFastVote_app(self, **kwargs):
        # app开始快速投票
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/vote/chatVotePublishFastVote",
            **kwargs)

    def chatVoteDetail_app(self, **kwargs):
        # app获取投票详情
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/vote/chatVoteDetail", **kwargs)

    def chatVoteDetailOptionCount_app(self, **kwargs):
        # app获取各选项投票人数
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/vote/chatVoteDetailOptionCount",
            **kwargs)

    def chatVoteDetailOptionVotersList_app(self, **kwargs):
        # app获取投票各选项详情
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/vote/chatVoteDetailOptionVotersList",
            **kwargs)

    def chatVoteDetailSelectedOption_app(self, **kwargs):
        # app获取投票选项集合
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/vote/chatVoteDetailSelectedOption",
            **kwargs)

    def chatVoteFinish_app(self, **kwargs):
        # app结束投票
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/vote/chatVoteFinish", **kwargs)

    def chatCreateVote_app(self, **kwargs):
        # app创建投票
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/vote/chatCreateVote", **kwargs)

    def chatVotePublishAnswers_app(self, **kwargs):
        # app公布投票答案
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/vote/chatVotePublishAnswers",
            **kwargs)

    def chatDeleteVote_app(self, **kwargs):
        # app删除投票
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/vote/chatDeleteVote", **kwargs)

    def unSendActivityList_app(self, **kwargs):
        # app查询待发布活动列表
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/meetScreen/unSendActivityList",
            **kwargs)

    def unSendActivityPublish_app(self, **kwargs):
        # app查询待发布活动列表
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/meetScreen/unSendActivityPublish",
            **kwargs)

    def getBrainStormListV2_app(self, **kwargs):
        # app查询头脑风暴列表
        return self.post(
            "https://ctapp.zhihuishu.com/app-commonserv-classroomtools/commonChat/brainStorm/getBrainStormListV2",
            **kwargs)


MeetingClass = MeetingClass(api_root_url)
