#coding:utf-8

import xlrd
import os
from Config.conf import *
from Methods import log

log1 = log.Logger(__name__)

class ReadExcel(object):
    def __init__(self,fileName='elementData.xlsx',sheetName='elementsInfo'):
        try:
            self.file = os.path.join(dataPath,fileName)
            self.workbook = xlrd.open_workbook(self.file)
            self.sheetName = self.workbook.sheet_by_name(sheetName)

        except Exception:
            log1.exception(" init class ReadExcel fail ! ")
            raise
        else:
            log1.info('initing class ReadExcel .')

    #读excel中的数据
    def readExcel(self,row,col):
        try:
            value = self.sheetName.cell(row,col).value
        except Exception:
            log1.exception('read excel value fail ！')
            raise
        else:
            log1.info('read value from excel : [%s]' %value)
            return value

if __name__ =="__main__":
    value = ReadExcel().readExcel(1,3)
    print(value)