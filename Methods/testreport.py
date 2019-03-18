#coding:utf-8
from Config.conf import *
from Methods import log
from Package import HTMLTestReportCN

import  time

log1 = log.Logger(__name__)
# 用HTMLTestRunner 实现的测试报告
def testreport():
    curTime = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    fileName = reportPath + curTime + '.html'
    try:
        fp = open(fileName,'wb')
    except Exception:
        log1.exception('[%s] open error cause Failed to generate test report' %fileName)
    else:
        run = HTMLTestReportCN.HTMLTestRunner(
            stream=fp,
            title="ONU WEB-A 测试报告",
            description="v1.0 ",
            tester="Joan"
        )
        log1.info('successed to generate test report : [%s]' %fileName)
        return fileName,run,fp

if __name__=="__main__":
    testreport()