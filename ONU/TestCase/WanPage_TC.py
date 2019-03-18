# coding:utf-8
import unittest
from Config.conf import *
from Methods import log
from Methods.myunittest import MyUnittest
from ONU.PageObj.WanPage import WanPage
import sys
from time import sleep
from selenium.webdriver.support.select import Select
log1 = log.Logger(__name__)


class WanPage_TC(MyUnittest):
    def test01_WanPage(self):
        "wan配置刷新"
        run = WanPage(self.driver)
        run.clickMenu((run.menuList[1][0], run.menuList[1][1]))
        sleep(1)
        run.clickMenu(WanPage.wan)
        sleep(3)  # 3s内刷出右侧详细信息
        run.driver.switch_to.frame('frameContent')
        try:
            message = self.driver.find_element_by_id("wan_content").text
            self.assertEqual('在本页面上，您可以配置WAN口参数。家庭网关通过WAN口与高层网络设备通信，在通信期间WAN口参数集必须和高层设备参数保持一致。', message, "WAN配置页面刷新失败")
        except Exception:
            self.login.ScreenShot('show_wanpeizhi_fail.png')
            raise
        else:
            log1.exception(('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name)))

    def test02_WanPage(self):
        "新建Wan连接"
        run = WanPage(self.driver)
        run.clickMenu((run.menuList[1][0], run.menuList[1][1]))
        sleep(1)
        run.clickMenu(WanPage.wan)
        sleep(3)  # 3s内刷出右侧详细信息
        run.driver.switch_to.frame('frameContent')
        try:
           run.clickMenu(('id',"Newbutton"))
           sleep(1)
           message = self.driver.find_element_by_id("BasicInfoBar").text
           self.assertEqual('基本信息',message,'新增wan配置失败。')
           rows = run.getTableRows(("id", "wanInstTable"))
           print("初始行数：%s"%rows)
           s1 = self.driver.find_element_by_id("ProtocolType")#选择协议类型为IPV6
           Select(s1).select_by_value("IPv6")
           s2 = self.driver.find_element_by_id("WanMode")#选择WAN类型
           Select(s2).select_by_value("IP_Routed") #选择“路由WAN”
           s3 = self.driver.find_element_by_id("ServiceList")#选择服务类型
           Select(s3).select_by_value("TR069_INTERNET")#"选择服务类型为TR069_INTERNET
           run.inputValue(("id","VlanId"),'100')
           run.inputValue(("id","IPv4MXU"),"1292")
           #应用按钮无法用click去处理，所以修改为使用js
           js = "return OnApply()"
           run.jScript(js)
           sleep(5)#3s内能刷新出来
           rows_new = run.getTableRows(("id", "wanInstTable"))
           print("新增后行数：%s"%rows_new)
           # self.assertEqual("1",rows_new-rows,"新增wan连接失败。")
        except Exception:
            self.login.ScreenShot('show_wanpeizhi_new_fail.png')
            raise
        else:
            log1.exception(('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name)))


    def test03_WanPage(self):
        #"删除Wan连接"
        run = WanPage(self.driver)
        run.clickMenu((run.menuList[1][0], run.menuList[1][1]))
        sleep(1)
        run.clickMenu(WanPage.wan)
        sleep(3)  # 3s内刷出右侧详细信息
        run.driver.switch_to.frame('frameContent')
        try:
            rows = run.getTableRows(("id", "wanInstTable"))
            run.clickMenu(('id',"wanInstTable_rml1"))
            run.clickMenu(('id',"DeleteButton"))
            sleep(3)
            rows_new = run.getTableRows(("id", "wanInstTable"))
            self.assertTrue(rows_new<rows,"删除wan连接失败")
        except Exception:
            self.login.ScreenShot('show_wanpeizhi_delete_fail.png')
            raise
        else:
            log1.exception(('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name)))

    def test04_WanPage(self):
        "DHCP客户端Option配置"
        run = WanPage(self.driver)
        run.clickMenu((run.menuList[1][0], run.menuList[1][1]))
        sleep(1)
        run.clickMenu(WanPage.wandhcpoption)
        sleep(3)  # 3s内刷出右侧详细信息
        run.driver.switch_to.frame('frameContent')
        try:
            message = self.driver.find_element_by_id("wandhcpoptiontitle_content").text
            self.assertEqual('在本页面上，您可以为路由WAN指定DHCP客户端携带的DHCPv4 Option。您可以输入十六进制或者Base64格式的Option内容。', message,
                             "DHCP客户端Option配置信息失败")
        except Exception:
            self.login.ScreenShot('show_wan_dhcpoption_fail.png')
            raise
        else:
            log1.exception(('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name)))

    def test05_WanPage(self):
        "DHCP客户端请求参数配置"
        run = WanPage(self.driver)
        run.clickMenu((run.menuList[1][0], run.menuList[1][1]))
        sleep(1)
        run.clickMenu(WanPage.wandhcppara)
        sleep(3)  # 3s内刷出右侧详细信息
        run.driver.switch_to.frame('frameContent')
        try:
            message = self.driver.find_element_by_id("wandhcpparatitle_content").text
            self.assertEqual('在本页面上，您可以为路由WAN指定DHCP客户端发出的请求参数列表，DHCP服务器根据指定的请求参数列表，返回对应参数的Option内容。', message,
                             "DHCP客户端请求参数配置失败")
        except Exception:
            self.login.ScreenShot('show_wan_dhcpoption_fail.png')
            raise
        else:
            log1.exception(('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name)))
