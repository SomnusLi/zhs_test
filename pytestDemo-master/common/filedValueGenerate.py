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
from ruamel import yaml
from common.read_data import data
import pytest
from selenium.webdriver.common.action_chains import ActionChains

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def get_data(yaml_file_name):
    try:
        data_file_path = os.path.join(BASE_PATH, "data", yaml_file_name)
        yaml_data = data.load_yaml(data_file_path)
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        return yaml_data


base_data = get_data("base_data.yml")
api_data = get_data("api_test_data.yml")
scenario_data = get_data("scenario_test_data.yml")


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


def add_cookies(cookie=None):
    cookies_data = get_data("cookies_test_data.yml")
    logger.info(cookies_data)
    is_cookies_expired = False
    if cookies_data == None:
        logger.info("文件无内容")
        is_cookies_expired = True
    else:
        cookies_time = cookies_data["datatime"]
        now_time = int(round(time.time()))
        if cookies_time != None:
            logger.info("cookies_time:{},now_time:{}".format(cookies_time, now_time))
            # logger.info(
            #     "保存的cookies中时间为：{}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(cookies_time))))
            # logger.info("现在的时间：{}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now_time))))
            now_time_change = time.strftime("%Y-%m-%d", time.localtime(now_time))
            cookies_time_change = time.strftime("%Y-%m-%d", time.localtime(cookies_time))
            logger.info(
                "保存的cookies中时间为：{}".format(cookies_time_change))
            logger.info("现在的时间：{}".format(now_time_change))
            days_diff = (now_time - cookies_time) / 3600 / 24
            logger.info("相差天数{}".format(days_diff))
            if now_time_change > cookies_time_change:
                is_cookies_expired = True
            elif cookies_data["cookies"] == None:
                is_cookies_expired = True
            else:
                cookies = {}
                for key in cookies_data["cookies"]:
                    cookies[key] = cookies_data["cookies"][key]
        else:
            is_cookies_expired = True
    if is_cookies_expired:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chromedriver_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
                                         "config\chromedriver.exe")
        logger.info(chromedriver_path)
        logger.info(chrome_options)
        browser = webdriver.Chrome(chromedriver_path, options=chrome_options)
        browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
            Object.defineProperty(navigator, 'webdriver', {
              get: () => undefined
            })
          """
        })
        browser.get(
            "https://passport.zhihuishu.com/login?service=https://onlineservice.zhihuishu.com/login/gologin")
        try:
            t = browser.find_element_by_class_name("waf-nc-title").get_attribute("textContent")
            logger.info(t)
            if t == "安全验证":
                logger.info("需要安全验证")
                move_element = browser.find_element_by_xpath("//*[@id='nc_1_n1z']")
                logger.info("按住滑块")
                ActionChains(browser).click_and_hold(on_element=move_element).perform()
                time.sleep(3)
                # 滑块x轴距离根据屏幕分辨率调整
                ActionChains(browser).move_to_element_with_offset(to_element=move_element, xoffset=300,
                                                                  yoffset=0).perform()
                logger.info("滑块滑到最右侧")
                ActionChains(browser).release(on_element=move_element).perform()
            else:
                logger.info("没有找到登录验证元素，无需登录验证")
        except:
            logger.info("无需登录验证")
        time.sleep(3)
        browser.find_element_by_xpath("//*[@id='lUsername']").clear()
        browser.find_element_by_xpath("//*[@id='lUsername']").send_keys("13122285260")
        time.sleep(1)
        browser.find_element_by_xpath("//*[@id='lPassword']").clear()
        browser.find_element_by_xpath("//*[@id='lPassword']").send_keys("Aa111111")
        time.sleep(1)
        browser.find_element_by_xpath("//*[@id='f_sign_up']/div[1]/span").click()
        try:
            t = browser.find_element_by_class_name("waf-nc-title").get_attribute("textContent")
            logger.info(t)
            if t == "安全验证":
                logger.info("需要安全验证")
                move_element = browser.find_element_by_xpath("//*[@id='nc_1_n1z']")
                ActionChains(browser).click_and_hold(on_element=move_element).perform()
                logger.info("按住滑块")
                time.sleep(3)
                # 滑块x轴距离根据屏幕分辨率调整
                ActionChains(browser).move_to_element_with_offset(to_element=move_element, xoffset=300,
                                                                  yoffset=0).perform()
                logger.info("滑块滑到最右侧")
                ActionChains(browser).release(on_element=move_element).perform()
            else:
                logger.info("没有找到登录验证元素，无需登录验证")
        except:
            logger.info("无需登录验证")
        time.sleep(10)
        list_cookies = browser.get_cookies()
        cookies = {}
        for s in list_cookies:
            cookies[s["name"]] = s["value"]
        browser.quit()
        cookies_data = {
            "cookies": cookies,
            "account": 13122285260,
            "datatime": int(round(time.time()))
        }
        yamlpath = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
                                "data\\cookies_test_data.yml")
        with open(yamlpath, "w", encoding="utf-8") as f:
            yaml.dump(cookies_data, f, Dumper=yaml.RoundTripDumper)
    logger.info(cookies)
    return cookies


def getRandomCheckGesture(num):
    list = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
    randomListNum = random.randint(num, len(list))
    randomList = random.sample(list, randomListNum)
    checkGesture = ""
    checkGesture = checkGesture.join(randomList)
    return checkGesture


def getRandomList(num):
    list = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"}
    randomList = random.sample(list, num)
    return randomList
