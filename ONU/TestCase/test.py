#coding:utf-8
from selenium import webdriver
from time import sleep
from Methods.myunittest import MyUnittest
import unittest
from selenium.webdriver.support.select import Select
from ONU.PageObj.LanPage import LanPage
import sys
def wantest():
    driver = webdriver.Firefox()
    driver.get('http://192.168.100.1')
    sleep(1)
    driver.find_element_by_id('txt_Username').send_keys('telecomadmin')
    driver.find_element_by_id('txt_Password').send_keys('admintelecom')
    driver.find_element_by_id('button').click()

    sleep(1)
    title = driver.find_element_by_id('headerTitle').text
    print(title)

    sleep(1)

    run = LanPage(driver)
    run.clickMenu((run.menuList[1][0], run.menuList[1][1]))
    sleep(1)
    #run.clickMenu(LanPage.lanlayer)
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/ul/li[1]/div").click()
    sleep(3)  # 3s内刷出右侧详细信息
    run.driver.switch_to.frame('frameContent')
#
if __name__ =="__main__":
    wantest()