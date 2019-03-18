#coding:utf-8
#存储各文件路径

import os


#描述项目路径:项目绝对路径
proPath = 'E:/20181213基础/ONU WEB-A Ver1.0/'
#获取当前路径
curPath = os.path.split(os.path.realpath(__file__))[0]
#拼接Log路径
logPath = os.path.join(proPath,'Reports/Logs/')

#元素数据路径(数据驱动)
dataPath = os.path.join(proPath,'ONU/Data/')
#邮件信息配置文件路径
mailInfoPath = os.path.join(curPath,'mail.ini')

#获取测试报告的路径
reportPath = os.path.join(proPath,'Reports/TestReport/')

#测试用例的路径
casePath = os.path.join(proPath,'ONU/TestCase/')


#保存截图的路径
    #错误截图
failImagePath = os.path.join(proPath,'Reports/Image-fail/')
    #成功截图
#passImagePath = os.path.join(proPath,'Reports/Image/pass/')