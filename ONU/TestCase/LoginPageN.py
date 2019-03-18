#coding:utf-8
import  unittest
from Config.conf import *
from Methods import log
from Methods.myunittest import MyUnittest
from ONU.PageObj.LoginPage import LoginPage
from selenium.webdriver.common.action_chains import ActionChains
import sys,time
log1 = log.Logger(__name__)

class login_TC(MyUnittest):

    def test01_LoginPage(self):
        """用户名正确,密码正确,登录成功"""
        self.login.loginFunc()
        curUrl = self.driver.current_url #获取当前的url地址
        try:
            self.assertIn('index',curUrl,'index is not in url')
        except Exception:
            self.login.ScreenShot('correct_username_pwd_fail.png')
            raise
        else:
            log1.exception(('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name)))

    @unittest.skip
    def test02_LoginPage(self):
        """用户名错误,密码正确,登录失败"""
        self.login.loginFunc(self.login.unpwData[1][0],self.login.unpwData[1][1])
        time.sleep(1)
        failText =self.login.getFailedText()
        self.assertEqual('用户名或密码错误，请重新登录。',failText,'提示信息错误!')
        log1.info('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name))

    @unittest.skip
    def test03_LoginPage(self):
        """用户名为空,密码正确,登录失败"""
        self.login.loginFunc(self.login.unpwData[2][0],self.login.unpwData[2][1])
        time.sleep(1)
        failText =self.login.getFailedText()
        self.assertEqual('用户名不能为空。',failText,'提示信息错误!')
        log1.info('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name))

    @unittest.skip
    def test04_LoginPage(self):
        """用户名错误,密码错误,登录失败"""
        self.login.loginFunc(self.login.unpwData[3][0], self.login.unpwData[3][1])
        time.sleep(1)
        failText = self.login.getFailedText()
        self.assertEqual('用户名或密码错误，请重新登录。', failText, '提示信息错误!')
        log1.info('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name))

    @unittest.skip
    def test05_LoginPage(self):
        """用户名正确,密码为空,登录失败"""
        self.login.loginFunc(self.login.unpwData[4][0],self.login.unpwData[4][1])
        time.sleep(1)
        failText =self.login.getFailedText()
        self.assertEqual('密码不能为空。',failText,'提示信息错误!')
        log1.info('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name))

    @unittest.skip
    def test06_LoginPage(self):
        """用户名正确,密码错误,登录失败"""
        self.login.loginFunc(self.login.unpwData[5][0],self.login.unpwData[5][1])
        time.sleep(1)
        failText =self.login.getFailedText()
        self.assertEqual('用户名或密码错误，请重新登录。',failText,'提示信息错误!')
        log1.info('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name))

    @unittest.skip
    def test07_LoginPage(self):
        """用户名为空,密码为空,登录失败"""
        self.login.loginFunc(self.login.unpwData[6][0],self.login.unpwData[6][1])
        time.sleep(1)
        failText =self.login.getFailedText()
        self.assertEqual('用户名不能为空。',failText,'提示信息错误!')
        log1.info('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name))

    @unittest.skip
    def test08_LoginPage(self):
        """用户名正确,密码为空,登录失败"""
        self.login.loginFunc(self.login.unpwData[7][0], self.login.unpwData[7][1])
        failText = self.login.getFailedText()
        self.assertEqual('用户名或密码错误，请重新登录。', failText, '提示信息错误!')
        log1.info('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name))


if __name__ =="__main__":
    suite = unittest.TestSuite()
    suite.addTest('test01')
