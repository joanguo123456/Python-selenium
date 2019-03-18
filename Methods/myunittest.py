#coding:utf-8

import unittest
from Config.conf import *
from Methods import log
from Methods.driver import MyDriver
from ONU.PageObj.LoginPage import LoginPage

log1 = log.Logger(__name__)

class MyUnittest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):# 一个测试类(文件)执行一次打开浏览器, 节约每个用例打开一次浏览器的时间
        cls.driver = MyDriver.FireFoxDriver(cls)
        cls.driver.maximize_window()
        log1.info('open the browser successed .')
        cls.login = LoginPage(cls.driver)
        cls.login.openUrl(url='http://192.168.100.1')
        cls.login.loginFunc()

    #-----------------------------------------------
    def setUp(self):
        #self.login = LoginPage(self.driver)
        #self.login.openUrl(url='http://192.168.100.1')
        #self.login.loginFunc()
        #self.driver.refresh()
        log1.info('************************starting run test cases************************')


    def tearDown(self):
        self.driver.refresh()
        log1.info('************************test case run completed************************')

    #-----------------------------------------------
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        log1.info('quit the browser successed .')
