#!/usr/bin/python3
# coding: utf-8

#Author:ymc023
#Mail: 
#Platform: python3
#Date:Wed 16 Sep 2020 02:11:35 PM CST


import smtplib
import datetime
import os
from email.mime.text import MIMEText

try:
    from borax.calendars.lunardate import LunarDate
except ImportError:
    os.system("pip install borax")


#计算当前日期
def calc_(nongli):
    if nongli == 1:
        today = LunarDate.today() 
        res = today.cn_month + today.cn_day
        return res
    if nongli == 0:
        cudate = datetime.datetime.now()
        res = cudate.strftime("%m-%d") 
        return res

#邮件发送
def mailex(mail_from,mail_dest,m_subject,passwd):
    msg = MIMEText(m_subject)
    msg['Subject'] = m_subject
    msg['From'] = mail_from
    msg['To'] = mail_dest
    try:
        
        s = smtplib.SMTP_SSL("smtp.qq.com",465)
        s.login(mail_from, passwd)
        s.sendmail(mail_from, mail_dest, msg.as_string())
        print("send ok")
    except Exception as  e:
        print("send failed")
    finally:
        s.quit()
#日志记录
def logg(data):
    cudate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("/root/notification.log",'a+') as fw:
        fw.write("%s | %s"%(cudate,data))
        fw.write("\n")
#提醒     
def notification():
    """
    用字典展示你需要提醒的日期
    如果你的提醒是阳历，需将nongli设置为0
    noti_date = {"三月初五或03-05":"需要提醒的事情",
                 "五月初十或05-10":"需要提醒的事情1"
                 } 
    """
    #通过设定的邮件地址，发送/接收提醒 
    mail_from = "929***@qq.com"
    mail_dest = "929***@qq.com"
    mail_pwd = "b********cfi"

    #默认使用用农历日期设置提醒,如果需要使用公历，请设置 nongli = 0
    nongli = 1
    noti_date = {"三月初十":"今天是***生日",
                 "六月十五":"今天是***生日，记得打电话",
                 "五月廿八":"今天是***生日,记得打电话",
                }
    for k,v in noti_date.items():
        if k == calc_(nongli):
            logg("%s,开始发信息通知"%(noti_date[k]))
            mailex(mail_from=mail_from,mail_dest=mail_dest,m_subject=noti_date[k],passwd=mail_pwd)
        else:
            logg("日期 %s 未命中提醒事件"%(calc_(nongli)))  


if __name__ == "__main__":
    notification()
