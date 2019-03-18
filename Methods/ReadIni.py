#coding:utf-8
import configparser #用于读写配置文件
from Methods import log
from Config.conf import *

log1 = log.Logger(__name__)

class ReadIni(object):

    def get_Ini(self, section, key):
        '''读取配置文件字段的值并返回'''
        config = configparser.ConfigParser()
        config.read(mailInfoPath, encoding="utf-8-sig")
        value = config.get(section, key)
        return value

    def get_Ini_options(self, section):
        '''读取配置文件某section下所有键'''
        config = configparser.ConfigParser()
        config.read(mailInfoPath, encoding="utf-8-sig")
        opt = config.options(section)
        return opt

    def get_addkey(self, user):
        '''遍历获得配置文件收件人email'''
        sum = 0
        L = []
        for i in user:
            if sum < len(user):
                emails = self.get_Ini('addressed',i)
                L.append(emails)
                sum += 1
        return L

if __name__ =="__main__":
    users = ReadIni().get_Ini_options("addressed")
    addresser = ReadIni().get_addkey(users)
    print(addresser)