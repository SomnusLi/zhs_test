import os
from core.rest_client import RestClient
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
api_root_url = data.load_ini(data_file_path)["host"]["api_root_url"]


class Course(RestClient):

    def __init__(self, api_root_url, **kwargs):
        super(Course, self).__init__(api_root_url, **kwargs)

    def getcourselist_student(self, uuid, date, **kwargs):
        # 获取学生端的课程列表
        # get方式url直接拼接 {}.format（）
        return self.get(
            "https://hikeservice.zhihuishu.com/student/course/aided/getMyCourseList?uuid={}&date={}".format(uuid,
                                                                                                            date),
            **kwargs)

    def getcourselist_teacher(self, uuid, date, **kwargs):
        # 获取老师端的课程列表
        return self.get(
            "https://hike-teaching.zhihuishu.com/teachingCourse/findTeacherCourses?pageSize=1000&uuid={}&date={}".format(
                uuid,
                date),
            **kwargs)

    def getRecruitIdByCourseId(self, courseId, **kwargs):
        # 获取课程的招生id
        return self.get(
            "https://hike.zhihuishu.com/aidedteaching/course/getRecruitIdByCourseId?courseId={}".format(courseId),
            **kwargs)


Course = Course(api_root_url)
