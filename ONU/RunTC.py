#coding：utf-8
import unittest
from Methods import testreport,log,SendMail
from Methods import log
from Config.conf import *

log1 = log.Logger(__name__)

if __name__ =="__main__":
    test_suite = unittest.defaultTestLoader.discover(casePath,pattern='*TC.py')
    fileName, runner, fp = testreport.testreport()
    runner.run(test_suite)
    fp.close()
    SendMail.SendMail().sendmail(fileName)



