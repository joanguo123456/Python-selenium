#coding:utf-8
import  unittest
from Config.conf import *
from Methods import log
from Methods.myunittest import MyUnittest
from ONU.PageObj.InfoPage import InfoPage
from ONU.PageObj.LoginPage import LoginPage
from selenium.webdriver.common.action_chains import ActionChains
import sys,time
log1 = log.Logger(__name__)
class login_TC(MyUnittest):

    def test01_InfoPage(self):
        "wan信息"
        run = InfoPage(self.driver)
        time.sleep(1)
        run.clickMenu(InfoPage.waninfo)
        # 进入嵌套的iframe中
        run.driver.switch_to.frame('frameContent')
        message = self.driver.find_element_by_id('waninfo_content').text
        try:
            self.assertEqual('在本页面上，您可以查询WAN口的连接和线路状态。',message,'wan信息刷新失败')
        except Exception:
            self.login.ScreenShot('show_wan_fail.png')
            raise
        else:
            log1.exception(('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name)))
    def test02_InfoPage(self):
        "以太网接口信息"
        run = InfoPage(self.driver)
        time.sleep(1)
        run.clickMenu(InfoPage.ethinfo)
        # 进入嵌套的iframe中
        run.driver.switch_to.frame('frameContent')
        message = self.driver.find_element_by_id('amp_ethinfo_desc_content').text
        try:
            self.assertEqual('在本页面上，您可以查询用户侧以太网接口信息。',message,'以太网接口信息刷新失败')
        except Exception:
            self.login.ScreenShot('show_eth_fail.png')
            raise
        else:
            log1.exception(('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name)))

    def test03_InfoPage(self):
        "DHCP信息"
        run = InfoPage(self.driver)
        time.sleep(1)
        run.clickMenu(InfoPage.dhcpinfo)
        # 进入嵌套的iframe中
        run.driver.switch_to.frame('frameContent')
        message = self.driver.find_element_by_id('dhcpinfotitle_content').text
        try:
            self.assertEqual('在本页面上，您可以查询DHCP基本信息，包括地址总数、ETH口分配的IP数、剩余IP数、主机名、IP地址、MAC地址、租期剩余时间和设备类型。',message,'dhcp信息刷新失败')
        except Exception:
            self.login.ScreenShot('show_dhcp_fail.png')
            raise
        else:
            log1.exception(('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name)))

    def test04_InfoPage(self):
        "光模块信息"
        run = InfoPage(self.driver)
        time.sleep(1)
        run.clickMenu(InfoPage.opticinfo)
        # 进入嵌套的iframe中
        run.driver.switch_to.frame('frameContent')
        message = self.driver.find_element_by_id('amp_optinfo_title_content').text
        try:
            self.assertEqual('在本页面上，您可以查询光模块基本信息。',message,'光模块信息刷新失败')
        except Exception:
            self.login.ScreenShot('show_dhcp_fail.png')
            raise
        else:
            log1.exception(('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name)))

    def test05_InfoPage(self):
        "设备信息"
        run = InfoPage(self.driver)
        time.sleep(2)
        run.driver.find_element(*InfoPage.deviceinfo).click()
        run.driver.switch_to.frame("frameContent")
        message = run.driver.find_element_by_id("deviceinfoasp_content").text
        mac = run.driver.find_element_by_id("td3_2").text
        try:
            self.assertEqual('在本页面上，您可以查看设备的基本信息。',message,'设备基本信息刷新失败')
        except Exception:
            self.login.ScreenShot('show_dhcp_fail.png')
            raise
        else:
            log1.info('设备的mac地址为:%s'% mac)
            log1.exception(('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name)))

    def test06_InfoPage(self):
        "远程管理信息"
        run = InfoPage(self.driver)
        time.sleep(1)
        run.clickMenu(InfoPage.acsstatus)
        # 进入嵌套的iframe中
        run.driver.switch_to.frame('frameContent')
        message = self.driver.find_element_by_id('acsstatus_content').text
        try:
            self.assertEqual('在本页面上，您可以查看设备的远程连接建立状态和业务下发状态。',message,'远程管理刷新失败')
        except Exception:
            self.login.ScreenShot('show_acsstatus_fail.png')
            raise
        else:
            log1.exception(('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name)))

    def test07_InfoPage(self):
        "用户设备信息"
        run = InfoPage(self.driver)
        time.sleep(1)
        run.clickMenu(InfoPage.userdevinfo)
        # 进入嵌套的iframe中
        run.driver.switch_to.frame('frameContent')
        message = self.driver.find_element_by_id('userdevinfotitle_content').text
        try:
            self.assertEqual('在本页面上，您可以查询用户设备基本信息，包括主机名、设备类型、IP地址、MAC地址和上线状态。', message, '远程管理刷新失败')
        except Exception:
            self.login.ScreenShot('show_userdevinfo_fail.png')
            raise
        else:
            log1.exception(('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name)))

    def test08_InfoPage(self):
        "业务开通状态"
        run = InfoPage(self.driver)
        time.sleep(1)
        run.clickMenu(InfoPage.bssinfo)
        # 进入嵌套的iframe中
        run.driver.switch_to.frame('frameContent')
        message = self.driver.find_element_by_id('bssinfo_content').text
        try:
            self.assertEqual('在本页面上，您可以查询业务的开通状态。', message, '业务开通状态刷新失败')
        except Exception:
            self.login.ScreenShot('show_bssinfo_fail.png')
            raise
        else:
            log1.exception(('%s->run completed! please check the test report' % (sys._getframe().f_code.co_name)))
