import random
import string
import socket
import time
import timeit
import datetime
import os
from common.logger import logger
import time
from selenium import webdriver


def getAutoEmail():
    """自动生成电子邮箱"""
    Fist_email = "".join(random.sample(string.ascii_letters + string.digits, 9))
    last_emailList = ['@hotmail.com', '@msn.com', '@yahoo.com', '@gmail.com', '@aim.com', '@aol.com', '@mail.com',
                      '@walla.com', '@inbox.com', '@126.com', '@163.com', '@sina.com', '@21cn.com', '@sohu.com',
                      '@yahoo.com.cn', '@tom.com', '@qq.com', '@etang.com', '@eyou.com', '@56.com', '@x.cn',
                      '@chinaren.com', '@sogou.com', '@citiz.com']
    rad = random.randrange(len(last_emailList))
    last_email = last_emailList[rad]
    EMAIL = '%s%s' % (Fist_email, last_email)
    return EMAIL


def getNumberId():
    """自动生成不重复id数字"""
    HOSTNAME = socket.gethostname()
    IP = socket.gethostbyname(HOSTNAME)
    SERIAL_NUMBER = 0
    TIMESTAMP = int(time.time() * 1000)
    MACHINE_ID = int(IP.split('.')[3])

    now = int(time.time() * 1e3)
    if now == TIMESTAMP:
        SERIAL_NUMBER += 1
    else:
        SERIAL_NUMBER = 0
    return (MACHINE_ID << 22) + (MACHINE_ID << 12) + SERIAL_NUMBER


def randomRangeNum(start, end):
    return random.randint(start, end)


def getAutoStr(num):
    """自动生成字符串"""
    str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    salt = ''
    for i in range(num):
        salt += random.choice(str)
    return salt


def getAutoNum(num=None):
    """自动生成不字符串"""
    if num is None:
        num = 5
    str = '0123456789'
    salt = ''
    for i in range(num):
        salt += random.choice(str)
    return salt


# 该函数随机生成未来一个月内的日期
def generatorDatetime():
    dateTime_s = time.time()  # 获取当前时间戳
    dateTime_s = datetime.datetime.fromtimestamp(dateTime_s)  # 将时间戳转换为日期
    # print(dateTime_s)
    str_p = datetime.datetime.strftime(dateTime_s, '%Y-%m-%d %H:%M:%S')  # 将日期转换为字符串
    # print(str_p)
    # 当前日期加一个月
    month = datetime.timedelta(days=30)
    dateTime_end = dateTime_s + month
    # print(dateTime_end)
    dateTime_end = datetime.datetime.strftime(dateTime_end, '%Y-%m-%d %H:%M:%S')  # 将日期转换为字符串
    # print(dateTime_end)

    # 将字符串转换为时间戳
    dateTime_s_stamp = time.mktime(time.strptime(str_p, '%Y-%m-%d %H:%M:%S'))
    # print(dateTime_s_stamp)

    dateTime_e_stamp = time.mktime(time.strptime(dateTime_end, '%Y-%m-%d %H:%M:%S'))
    # print(dateTime_e_stamp)

    t = random.randint(dateTime_s_stamp, dateTime_e_stamp)
    date_touple = time.localtime(t)  # 将时间戳生成时间元组
    date = time.strftime("%Y-%m-%d", date_touple)  # 将时间元组转成格式化字符串（1976-05-21）
    # date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    # print(date)
    return date


# 获取当前日期
def generatorNowDatetime():
    dateTime_now = time.time()  # 获取当前时间戳
    date_now = time.localtime(dateTime_now)  # 将时间戳生成时间元组
    date = time.strftime("%Y-%m-%d", date_now)  # 将时间元组转成格式化字符串（1976-05-21）
    return date


# 获取TZ格式的UTC时间
def get_current_time():
    """[summary] 获取当前时间

    [description] 用time.localtime()+time.strftime()实现
    :returns: [description] 返回str类型
    """
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y-%m-%dT%H:%M:%S", local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "%s.%03dZ" % (data_head, data_secs)
    return time_stamp


def add_cookies(cookie):
    # cookies[
    #     "CASLOGC"] = "%7B%22realName%22%3A%22%E5%88%98%E6%96%87%E5%8A%9B%22%2C%22myuniRole%22%3A1%2C%22myinstRole%22%3A0%2C%22userId%22%3A802042381%2C%22headPic%22%3A%22https%3A%2F%2Fimage.zhihuishu.com%2Fzhs%2Fablecommons%2Fcutimage%2F202009%2F72f45aa91cae4160af342c114ece5ced_s3.jpg%22%2C%22uuid%22%3A%22Vv45Mker%22%2C%22mycuRole%22%3A0%2C%22username%22%3A%224428ee860c5949a28ede8907e7a3bce7%22%7D"
    # cookies["CASTGC"] = "TGT-363027-0ufZ5LXYfRra5NnfaFrPtcree4HCHmNWrBWWXZltbBjLYuRR34-passport.zhihuishu.com"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--incognito")
    chromedriver_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
                                     "config\chromedriver.exe")
    logger.info(chromedriver_path)
    logger.info(chrome_options)
    browser = webdriver.Chrome(chromedriver_path, options=chrome_options)
    browser.get("https://passport.zhihuishu.com/login?service=https://onlineservice.zhihuishu.com/login/gologin")
    time.sleep(3)
    browser.find_element_by_xpath("//*[@id='lUsername']").send_keys("13122285260")
    time.sleep(1)
    browser.find_element_by_xpath("//*[@id='lPassword']").send_keys("Aa111111")
    time.sleep(1)
    browser.find_element_by_xpath("//*[@id='f_sign_up']/div[1]/span").click()
    time.sleep(3)
    list_cookies = browser.get_cookies()
    cookies = {}
    for s in list_cookies:
        cookies[s["name"]] = s["value"]
    browser.quit()
    return cookies


def getRandomCheckGesture():
    list = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
    randomListNum = random.randint(4, 9)
    randomList = random.sample(list, randomListNum)
    checkGesture = ""
    checkGesture = checkGesture.join(randomList)
    return checkGesture
