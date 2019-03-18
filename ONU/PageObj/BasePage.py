#coding:utf-8
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from Config.conf import *
from Methods import log,ReadExcel
from Methods.driver import MyDriver
import sys

log1 = log.Logger(__name__)
elementData = ReadExcel.ReadExcel()
#登录模块测试数据读取
loginData = ReadExcel.ReadExcel(fileName='elementData.xlsx',sheetName='userNamePw')
#修改密码数据读取
modifyData = ReadExcel.ReadExcel(fileName='elementData.xlsx',sheetName='modifyPw')
#
class BasePage(object):
    menuList = \
        [(elementData.readExcel(6,2), elementData.readExcel(6,3)),  #状态，infoPage
         (elementData.readExcel(7,2), elementData.readExcel(7,3)),  #WAN，WANPage
         (elementData.readExcel(8,2), elementData.readExcel(8, 3)), #LAN，LANPage
         (elementData.readExcel(9,2),elementData.readExcel(9, 3)), #IPv6，IPv6Page
         (elementData.readExcel(10,2), elementData.readExcel(10, 3)),#安全,
         (elementData.readExcel(11,2), elementData.readExcel(11, 3)),#路由
         (elementData.readExcel(12,2), elementData.readExcel(12, 3)),#转发规则
         (elementData.readExcel(13,2), elementData.readExcel(13, 3)),#网络应用
         (elementData.readExcel(14,2), elementData.readExcel(14, 3)),#系统工具
         ]
    def __init__(self,driver, url='http://192.168.100.1/'):
        self.driver = driver
        self.base_url = url

    def openUrl(self, url):  # 封装打开url
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(6)
        except Exception as e:
            log1.exception('can not open the url :%s' % url)
            raise e
        else:
            log1.info('%s is accessing address %s at line[46]' % (sys._getframe().f_code.co_name, url))

        # 封装查找单个元素
        # *loc 代表任意数量的位置参数

    def findElement(self, *loc):
        try:
            WebDriverWait(self.driver, 8).until(EC.visibility_of_element_located(loc))
        except Exception as e:
            log1.exception('finding element timeout!')
            raise e
        else:
            log1.info('the page %s has find the element %s' % (self, loc))
            return self.driver.find_element(*loc)

        # 封装查找多个元素

    def findElements(self, *loc):
        try:
            WebDriverWait(self.driver, 8).until(EC.visibility_of_element_located(loc))
        except Exception as e:
            log1.exception('finding element timeout!', 'details')
            raise e
        else:
            log1.info('the page %s has find the element %s' % (self, loc))
            return self.driver.find_elements(*loc)

        # 获取元素数据

    def getValue(self, loc):
        element = self.driver.find_element(*loc)
        try:
            value = element.text
        except Exception:
            value1 = element.get_attribute('value')
            log1.info('read the element %s value %s' % (*loc, value1))
            return value1
        except Exception as e:
            log1.exception('read value failed ')
            raise e
        else:
            log1.exception('read the element %s value %s' % (*loc, value))
            return value

        # 获取元素数据列表

    def getValues(self, *loc):
        value_list = []
        try:
            for element in self.findElements(*loc):
                value = element.text
                value_list.append(value)
        except Exception as e:
            log1.exception('read value failed ', exc_info=True)
            raise e
        else:
            log1.exception('read the element %s value %s' % (loc, value_list))
            return value_list

        # 执行js脚本

    def jScript(self, src):
        try:
            self.driver.execute_script(src)
        except Exception as e:
            log1.exception('excute js %s failed ! ' % src)
            raise e
        else:
            log1.info('exceute js %s successed !' % src)

        # 截图

    def ScreenShot(self, fileName):
        list_value = []
        list = fileName.split('.')
        for value in list:
            list_value.append(value)
        if list_value[1] == 'png' or list_value[1] == 'jpg' or list_value[1] == 'PNG' or list_value[1] == 'JPG':
            if 'fail' in list_value[0].split('_'):
                try:
                    self.driver.save_screenshot(os.path.join(failImagePath, fileName))

                except Exception:
                    log1.exception('save screenshot failed !', exc_info=True)
                else:
                    log1.info('save the screenshot sucessed under %s' % (failImagePath, fileName))
            else:
                log1.info('save screenshot failed due to [%s] format incorrect' % fileName)
        else:
            log1.info(
                'the file name of [%s] format incorrect cause save screenshot failed, please check!' % fileName)
        # 接受错误提示

    def accept(self, *loc):
        self.findElement(*loc).click()
        log1.info('closed the error information fram successed!')

        # 输入

    def inputValue(self, inputBox, value):
        inputB = self.findElement(*inputBox)
        try:
            inputB.clear()
            inputB.send_keys(value)
        except Exception as e:
            log1.exception('typing value error!', exc_info=True)
            raise e
        else:
            log1.info('inputValue:[%s] is receiveing value [%s]' % (inputBox, value))

    # 封装左侧小菜单的点击
    def clickMenu(self,menuName):
        element = self.findElement(*menuName)
        element.click()
        log1.info('%s ,clicking....!' % sys._getframe().f_code.co_name)

    #获取table的行数
    def getTableRows(self,tableBox):

        rows = self.driver.find_element(*tableBox).find_elements_by_tag_name("tr")
        return len(rows)-1




if __name__ == "__main__":
    url = "https://www.baidu.com"

    ele = ('id', 'kw')
    sub = ('id', 'su')
    value = '橙子'
    dri = webdriver.Firefox()
    run = BasePage(dri)

    run.openUrl(url)
    run.driver.get(url)
    run.inputValue(ele, value)
    run.findElement(*sub).click()
    run.ScreenShot('baidu_fail.png')
