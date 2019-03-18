#coding:utf-8

from selenium.webdriver.common.by import By
from Config.conf import *
from Methods import log,ReadExcel
from Methods.driver import MyDriver
from ONU.PageObj.BasePage import *
log1 = log.Logger(__name__)
class LanPage(BasePage):
    #页面左侧小菜单
    lanlayer = ( elementData.readExcel(26,2), elementData.readExcel(26,3))   # LAN口工作模式
    lanhover = ( elementData.readExcel(27,2), elementData.readExcel(27, 3))  #  LAN主机配置
    landhcp = (elementData.readExcel(28,2), elementData.readExcel(28, 3))  # DHCP服务配置
    landhcpoption = (elementData.readExcel(29,2), elementData.readExcel(29, 3))  #  DHCP服务器Option配置
    dhcpstatic = (elementData.readExcel(30, 2), elementData.readExcel(30, 3))  # DHCP静态IP配置

    frameID = "frameContent"
