# -*- coding: UTF-8 -*-

# !/usr/bin/python3

import smtplib
from pathlib import Path

from public import params as p
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


def send_email(content, rfile):

    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = Header(p.sender)
    message['To'] = ",".join(p.receivers)
    subject = 'AioCloud接口测试报告：' + content
    message['Subject'] = Header(subject)

    # 邮件正文内容
    message.attach(MIMEText('详细内容见附件。', 'plain', 'utf-8'))

    # 构造附件1，传送当前目录下的 test.txt 文件
    att1 = MIMEText(Path.open(rfile, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename=report.html'
    message.attach(att1)

    # 构造附件2，传送当前目录下的 runoob.txt 文件
    # att2 = MIMEText(open('runoob.txt', 'rb').read(), 'base64', 'utf-8')
    # att2["Content-Type"] = 'application/octet-stream'
    # att2["Content-Disposition"] = 'attachment; filename="runoob.txt"'
    # message.attach(att2)

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(p.smtp_host, 25)  # 25 为 SMTP 端口号
        # smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(p.sender, 'qzj23478')
        smtpObj.sendmail(p.sender, p.receivers, message.as_string())
        print("邮件发送成功")
        smtpObj.quit()
    except smtplib.SMTPException as e:
        print(e)


if __name__ == '__main__':
    rfile = Path('C:/Users/齐振鋆\PycharmProjects/NeuSoftEEP_API_Test/report/IME接口测试报告_2018-08-06 15-35-39.html')
    content = 'IME接口测试报告_2018-08-06 15-35-39'
    send_email(content, rfile)
