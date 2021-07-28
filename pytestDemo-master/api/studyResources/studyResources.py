import os
import time

from core.rest_client import RestClient
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
api_root_url = data.load_ini(data_file_path)["host"]["api_root_url"]


class studyResources(RestClient):

    def __init__(self, api_root_url, **kwargs):
        super(studyResources, self).__init__(api_root_url, **kwargs)

    def findFolderMenu(self, courseId, uuid, **kwargs):
        # 查询课程下学习资源目录
        return self.get(
            "https://studyresources.zhihuishu.com/studyResources/mcFile/findFolderMenu?courseId={}&uuid={}&dateFormate={}".format(
                courseId, uuid, int(round(time.time() * 1000))),
            **kwargs)

    def queryAllFileCount(self, **kwargs):
        # 查询课程下学习资源总数
        return self.post("https://studyresources.zhihuishu.com/studyResources/file/queryAllFileCount", **kwargs)

    def findLastOpenFile(self, courseId, uuid, **kwargs):
        # 查询见面课最后打开的文件
        return self.get(
            "https://studyresources.zhihuishu.com/studyResources/mcFile/findLastOpenFile?courseId={}&uuid={}&dateFormate={}".format(
                courseId, uuid, int(round(time.time() * 1000))),
            **kwargs)

    def findFilesByFolderId(self, courseId, folderId, uuid, **kwargs):
        # 根据FolderId查找目录下文件
        return self.get(
            "https://studyresources.zhihuishu.com/studyResources/mcFile/findFilesByFolderId?courseId={}&folderId={}&uuid={}&dateFormate={}".format(
                courseId, folderId, uuid, int(round(time.time() * 1000))),
            **kwargs)

    def importOneFileToMeetCourse(self, **kwargs):
        # 选择学习资源里的文件
        return self.post("https://app-hike.zhihuishu.com/appAidedteaching/meetCourse/importOneFileToMeetCourse",
                         **kwargs)

    def canUseFile(self, fileId, role, sourceId, courseId, uuid, **kwargs):
        # 查询见面课课件使用权限
        return self.get(
            "https://studyresources.zhihuishu.com/studyResources/mcFile/canUseFile?fileId={}&role={}&sourceId={}&courseId={}&uuid={}&dateFormate={}".format(
                fileId, role, sourceId, courseId, uuid, int(round(time.time() * 1000))), **kwargs)

    def findResourceData(self, rootFolderId, type, meetCourseId, uuid, **kwargs):
        # 学习资源筛选
        return self.get(
            "https://app-hike.zhihuishu.com/appAidedteaching/webMeetCourse/meetCourse/findResourceData?rootFolderId={}&fileName=&type={}&meetCourseId={}&stamp={}&uuid={}&dateFormate={}".format(
                rootFolderId, type, meetCourseId, int(round(time.time() * 1000)), uuid, int(round(time.time() * 1000))),
            **kwargs)

    def getMeetCourseFileList_app(self, **kwargs):
        # app查询投屏课件历史
        return self.post("https://app-hike.zhihuishu.com/appAidedteaching/meetCourse/getMeetCourseFileList",
                         **kwargs)

    def getMeetCourseFileInfo_app(self, **kwargs):
        # app查询当前投屏文件信息
        return self.post("https://app-hike.zhihuishu.com/appAidedteaching/meetCourse/getMeetCourseFileInfo",
                         **kwargs)

    def aidTeachingFolderId_app(self, **kwargs):
        # 获取学习资源根目录FolderId
        return self.post("https://app-hike.zhihuishu.com/appAidedteaching/teacher/course/aidTeachingFolderId",
                         **kwargs)

    def findResourceData_app(self, **kwargs):
        # app查询学习资源文件列表
        return self.post("https://app-hike.zhihuishu.com/appAidedteaching/meetCourse/findResourceData", **kwargs)


studyResources = studyResources(api_root_url)
