#coding:utf-8
#封装浏览器驱动：firefox浏览器
from selenium import webdriver
import sys
from selenium.webdriver.support.wait import WebDriverWait
from Methods import log

log1 = log.Logger(__name__)

class  MyDriver(object):
    def FireFoxDriver(self):
        try:
            self.driver = webdriver.Firefox()
        except Exception as e:
            log1.exception('FireFoxDriverServer.exe executable needs to be in PATH. Please download!')
            #Logger.exception()与Logger.error()的区别在于：
            # Logger.exception()将会输出堆栈追踪信息，
            # 另外通常只是在一个exception handler中调用该方法。
            raise e
        else:
            log1.info('%s:found the FireFx driver [%s]successed !'%(sys._getframe().f_code.co_name,self.driver))
        return self.driver

    def ChromeDriver(self):
        try:
            self.driver = webdriver.Chrome()
        except Exception as e:
            log1.exception('ChromeDriverServer.exe executable needs to be in PATH. Please download!')
            raise e
        else:
            log1.info('%s:found the chrome driver [%s]successed !' % (sys._getframe().f_code.co_name, self.mydriver))
        return self.driver
