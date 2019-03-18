#coding:utf-8
#登录页面

from selenium.webdriver.common.by import By
from Config.conf import *
from Methods import log,ReadExcel
from Methods.driver import MyDriver
from ONU.PageObj.BasePage import *
import time
import sys

log1 = log.Logger(__name__)

class LoginPage(BasePage):

    userNameEle = (By.ID,elementData.readExcel(1,3))#用户名
    #print(userNameEle)
    passWordEle = (By.ID, elementData.readExcel(2, 3))#密码
    #print(passWordEle)
    loginBtnEle = (By.ID, elementData.readExcel(3, 3))#登录按钮
    #print(loginBtnEle)
    errorMessage = (By.ID,elementData.readExcel(4,3))#错误信息

    #用户名和密码
    unpwData = [
        [loginData.readExcel(1,0),loginData.readExcel(1,1)],
        [loginData.readExcel(2, 0), loginData.readExcel(2, 1)],
        [loginData.readExcel(3, 0), loginData.readExcel(3, 1)],
        [loginData.readExcel(4, 0), loginData.readExcel(4, 1)],
        [loginData.readExcel(5, 0), loginData.readExcel(5, 1)],
        [loginData.readExcel(6, 0), loginData.readExcel(6, 1)],
        [loginData.readExcel(7, 0), loginData.readExcel(7, 1)]
    ]

    # 封装登录按钮
    def clickBtn(self):
        element = self.findElement(*self.loginBtnEle)
        element.click()
        log1.info('%s ,logining....!' % sys._getframe().f_code.co_name)

    # 登录函数
    def loginFunc(self,username='telecomadmin',pwd='admintelecom'):
        #self.openUrl(self.base_url)
        self.inputValue(self.userNameEle, username)
        self.inputValue(self.passWordEle, pwd)
        self.clickBtn()
    #获取登录失败时的提示信息
    def getFailedText(self):
        failInfo = self.findElement(*self.errorMessage).text
        log1.info('login failed : %s'%failInfo)
        return failInfo

    def clearValue(self,element):#清空输入
        empty = self.findElement(*element)
        empty.clear()
        log1.info("empting value....")

if __name__ =="__main__":

    LoginPage().loginFunc()
