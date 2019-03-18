#coding:utf-8

from selenium.webdriver.common.by import By
from Config.conf import *
from Methods import log,ReadExcel
from Methods.driver import MyDriver
from ONU.PageObj.BasePage import *
import time
import sys

log1 = log.Logger(__name__)
class InfoPage(BasePage):
    #页面左侧小菜单
    waninfo = ( elementData.readExcel(15,2), elementData.readExcel(15,3))   #WAN信息
    ethinfo = ( elementData.readExcel(16,2), elementData.readExcel(16, 3))  # 以太网接口信息
    dhcpinfo = (elementData.readExcel(17,2), elementData.readExcel(17, 3))  # DHCP信息
    opticinfo = (elementData.readExcel(18,2), elementData.readExcel(18, 3))  # 光模块信息
    deviceinfo = (elementData.readExcel(19,2), elementData.readExcel(19, 3))  # 设备信息
    acsstatus = (elementData.readExcel(20,2), elementData.readExcel(20, 3))  # 远程管理
    userdevinfo = (elementData.readExcel(21,2), elementData.readExcel(21, 3))  # 用户设备信息
    bssinfo = (elementData.readExcel(22,2), elementData.readExcel(22, 3))  # 业务开通状态

    # # 封装左侧小菜单的点击
    # def clickMenu(self,menuName):
    #     element = self.findElement(*menuName)
    #     element.click()
    #     log1.info('%s ,clicking....!' % sys._getframe().f_code.co_name)

    def ReadHtmlTable(self,htmltable,row,col):
        table = self.findElement(*htmltable)
        table_rows = table.find_element_by_tag_name('tr')
