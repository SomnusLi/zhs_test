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

    def getMeetCourseTeacherSetting(self, **kwargs):
        # 获取正在进行中的见面课
        return self.post(
            "https://app-hike.zhihuishu.com/appAidedteaching/meetCourse/getMeetCourseTeacherSetting",
            **kwargs)


MeetingClass = MeetingClass(api_root_url)
