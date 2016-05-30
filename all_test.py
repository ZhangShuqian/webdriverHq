#coding:utf-8
import HTMLTestRunner
import sys, os
import time, datetime
import unittest
from Model.baseNumber import Config
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header

reload(sys)
sys.setdefaultencoding('utf-8')

#批量获取测试用例
def suite():
    dir_case = unittest.defaultTestLoader.discover(
        Config.testcase_dirs(),
        pattern= 'test_*.py',
        top_level_dir= None
    )
    return dir_case

#获取当前的时间
def getNowtime():
    return time.strftime('%Y-%m-%d %H_%M_%S', time.localtime(time.time()))

#执行测试用例，生成测试报告
def runautomation():
    filename = 'D:\\PycharmProjects\\webdriverHq\\report\\' + getNowtime() + 'WmsTestReport.html'
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title= u'自动化测试报告',
        description= u'用例执行情况'
    )
    runner.run(suite())

#定义发送邮件
def sendEmail(file_new):
    #发信邮箱
    mail_from = '1558781894@qq.com'
    #收信邮箱
    mail_to = 'shuqian.zhang@baozun.cn', '刘勋<xun.liu@baozun.cn>'
    #定义正文
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    msg['From'] = '1558781894@qq.com'
    to_list = [u'张树迁<shuqian.zhang@baozun.cn>', u'刘勋<xun.liu@baozun.cn>']
    msg['To'] = ','.join(to_list)
    #定义标题
    msg['Subject'] = u'WMS4.0测试报告'
    #定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
    msg['data'] = time.strftime('%a %d %b %Y %H:%M:%S %z')
    smtp = smtplib.SMTP()
    #连接smtp服务器
    smtp.connect('smtp.qq.com')
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.set_debuglevel(1)
    #用户名、密码
    smtp.login('1558781894@qq.com', 'viwkkmsoxujfbaej')
    smtp.sendmail(mail_from, mail_to, msg.as_string())
    smtp.quit()
    print 'email has send out!'

#查找测试报告，调用发送邮件功能
def sendReport():
    lists = os.listdir(Config.report_dirs())
    lists.sort(key=lambda fn: os.path.getmtime(Config.report_dirs() + '\\' + fn)
                if not os.path.isdir(Config.report_dirs() + '\\' + fn) else 0)
    print u'WMS4.0最新测试报告为：', lists[-1]
    file_new = os.path.join(Config.report_dirs() , lists[-1])
    print file_new
    sendEmail(file_new)

if __name__ == '__main__':
    runautomation()
    sendReport()