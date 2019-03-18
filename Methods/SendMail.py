#coding:utf-8
#设置邮箱发送
from exchangelib import DELEGATE, Account, Credentials, Configuration, NTLM, Message, Mailbox, HTMLBody
from exchangelib.protocol import BaseProtocol, NoVerifyHTTPAdapter
from time import sleep
from Methods import log
from Methods.ReadIni import ReadIni
from Config.conf import *

log1 = log.Logger(__name__)
class SendMail(object):
    def __init__(self):
    # #def __init__(self,EmailServer = "mail.cvnchina.com",
    #              EmailUser = "gjunjuan",Password = "Guojunjuan1902",
    #              sender="gjunjuan@cvnchina.com",addresser ="gjunjuan@cvnchina.com"):
        self.EmailServer = ReadIni().get_Ini("mailServer","server")
        self.EmailUser = ReadIni().get_Ini("sender","username")
        self.Password = ReadIni().get_Ini("sender","password")
        self.sender = ReadIni().get_Ini("sender","email")
        users = ReadIni().get_Ini_options("addressed")
        self.addresser = ReadIni().get_addkey(users)
    def sendmail(self,filename):
        # 此句用来消除ssl证书错误，exchange使用自签证书需加上
        BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter
        cred = Credentials(self.EmailUser, self.Password)

        mailconfig = Configuration(
            server=self.EmailServer,
            credentials=cred,
            auth_type=NTLM)
        account = Account(
            primary_smtp_address=self.sender,
            config=mailconfig,
            autodiscover=False,
            access_type=DELEGATE)
        sleep(1)
        #打开测试报告，读取报告内容
        try:
            with open(os.path.join(reportPath,filename),'rb') as f:
                fileMsg = f.read().decode('utf-8')

        except Exception as e:
            log1.exception('open or read file [%s] failed,No such file or directory: %s' %(filename, reportPath))
            raise e
        else:
            log1.info('open and read file [%s] successed!' % filename)

        #登录服务器，连接邮箱，设置邮件
        try:
            m = Message(
                account=account,
                subject="测试邮件",  # 邮件主题
                body=HTMLBody(fileMsg),
                to_recipients=self.addresser
            )
        except Exception:
            log1.exception('connect [%s] server failed or username and password incorrect!' %self.EmailServer)
        else:
            log1.info('connect [%s] server successed ！' %self.EmailServer)

        #发送邮件
        try:
            m.send()
        except Exception:
            log1.exception('send mail failed ！')
        else:
            log1.info('send mail successed ！')

if __name__ =="__main__":
    SendMail().sendmail('report1.txt')