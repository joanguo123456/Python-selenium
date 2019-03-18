#coding:utf-8

from selenium.webdriver.common.by import By
from Config.conf import *
from Methods import log,ReadExcel
from Methods.driver import MyDriver
from ONU.PageObj.BasePage import *
import sys
log1 = log.Logger(__name__)
class WanPage(BasePage):
    #页面左侧小菜单
    wan = ( elementData.readExcel(23,2), elementData.readExcel(23,3))   #WAN配置
    wandhcpoption = ( elementData.readExcel(24,2), elementData.readExcel(24, 3))  # DHCP客户端Option配置
    wandhcppara = (elementData.readExcel(25,2), elementData.readExcel(25, 3))  # DHCP客户端请求参数配置
    frameID = "frameContent"
