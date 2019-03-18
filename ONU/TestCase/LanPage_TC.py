# coding:utf-8
import unittest
from Config.conf import *
from Methods import log
from Methods.myunittest import MyUnittest
from ONU.PageObj.LanPage import LanPage
import sys
from time import sleep
from selenium.webdriver.support.select import Select

log1 = log.Logger(__name__)

class LanPage_TC(MyUnittest):
    def test01_LanPage(self):
        " LAN口工作模式刷新"
        run = LanPage(self.driver)
        run.clickMenu((run.menuList[2][0], run.menuList[2][1]))
        sleep(1)
        run.clickMenu(LanPage.lanlayer)
        sleep(3)  # 3s内刷出右侧详细信息
        run.driver.switch_to.frame('frameContent')
        try:
            message = self.driver.find_element_by_id("layer3_content").text
            self.assertEqual('在本页面上，您可以通过选择相应的复选框设置LAN口为三层口(HG端口)。', message, "LAN口工作模式页面信息错误")
        except Exception:
            self.login.ScreenShot('show_lanlayer3_fail.png')
            raise
        else:
            log1.exception(('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name)))

    def test02_LanPage(self):
        " LAN主机配置"
        run = LanPage(self.driver)
        run.clickMenu((run.menuList[2][0], run.menuList[2][1]))
        sleep(1)
        run.clickMenu(LanPage.lanhover)
        sleep(3)  # 3s内刷出右侧详细信息
        run.driver.switch_to.frame('frameContent')
        try:
            message = self.driver.find_element_by_id("dhcptitle_content").text
            self.assertEqual('在本页面上，您可以设置LAN侧管理IP地址。 改变LAN侧主机IP地址后，确保DHCP主地址池和新LAN侧IP地址的在同一子网。否则，DHCP服务不能正常工作。使能向LAN侧发送免费ARP后，在PC连接上设备以太口或PC IP地址与LAN主机IP地址冲突时，设备会向LAN侧发送免费ARP报文。', message, "LAN口工作模式页面信息错误")
        except Exception:
            self.login.ScreenShot('show_lanhover_fail.png')
            raise
        else:
            log1.exception(('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name)))

    def test03_LanPage(self):
        "  DHCP服务配置"
        run = LanPage(self.driver)
        run.clickMenu((run.menuList[2][0], run.menuList[2][1]))
        sleep(1)
        run.clickMenu(LanPage.landhcp)
        sleep(3)  # 3s内刷出右侧详细信息
        run.driver.switch_to.frame('frameContent')
        try:
            message = self.driver.find_element_by_id("dhcp2_content").text
            self.assertEqual('在本页面上，您可以为LAN侧设备获取IP地址配置DHCP服务器参数。', message, "DHCP服务配置页面信息错误")
        except Exception:
            self.login.ScreenShot('show_landhcp_fail.png')
            raise
        else:
            log1.exception(('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name)))

    def test04_LanPage(self):
        " DHCP服务器Option配置"
        run = LanPage(self.driver)
        run.clickMenu((run.menuList[2][0], run.menuList[2][1]))
        sleep(1)
        run.clickMenu(LanPage.landhcpoption)
        sleep(3)  # 3s内刷出右侧详细信息
        run.driver.switch_to.frame('frameContent')
        try:
            message = self.driver.find_element_by_id("landhcpoptiontitle_content").text
            self.assertEqual('在本页面上，您可以为LAN侧DHCP服务器配置Option参数。', message, "DHCP服务配置页面信息错误")
        except Exception:
            self.login.ScreenShot('show_landhcpoption_fail.png')
            raise
        else:
            log1.exception(('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name)))

    def test05_LanPage(self):
        " DHCP静态IP配置"
        run = LanPage(self.driver)
        run.clickMenu((run.menuList[2][0], run.menuList[2][1]))
        sleep(1)
        run.clickMenu(LanPage.dhcpstatic)
        sleep(3)  # 3s内刷出右侧详细信息
        run.driver.switch_to.frame('frameContent')
        try:
            message = self.driver.find_element_by_id("dhcpstatic_content").text
            self.assertEqual('在本页面上，您可以对指定MAC地址配置DHCP分配的预留IP地址。', message, "DHCP服务配置页面信息错误")
        except Exception:
            self.login.ScreenShot('show_dhcpstatic_fail.png')
            raise
        else:
            log1.exception(('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name)))
