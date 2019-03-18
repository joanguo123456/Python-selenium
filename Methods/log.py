#coding:utf-8
import logging
import time
from Config.conf import *
def Logger(testlog): #测试的名称
    #1、创建log
    logg = logging.getLogger(testlog)
    logg.setLevel(logging.INFO)#log等级的总开关
    # 获取本地时间，转换成日志需要的格式
    curTime = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
    # 设置日志的文件名称
    LogFileName = logPath + curTime + '.log'

    #设置文件的内容,FileHandler是将日志信息输出到磁盘文件上；
    fh = logging.FileHandler(LogFileName,mode='w',encoding='utf-8')
    fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
    # 所有日志以时间-日志器名称-日志级别-日志内容的形式展示
    fmt = logging.Formatter('%(asctime)s - %(filename)s:[%(lineno)s]-[%(levelname)s] - %(message)s')
    fh.setFormatter(fmt)
    logg.addHandler(fh)
    return logg

# 日志
#log = Logger('this is a logger debug message')
#log1 = log.info("my name is joan")
#log2 = log.error("this is error message")
#log3 = log.warning("this is a warning")