#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import smtplib as smtp
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# 发信方的信息：发信邮箱，QQ邮箱授权码）
from_addr = "374137689@qq.com"
password = "gmbhselbogaccbdd"

# 收信方邮箱
to_addr = '374137689@qq.com'

# 发信服务器
smtp_server = 'smtp.qq.com'

# 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
text = '''亲爱的ao li fer，你好！

​    我是per pa，我们能够相爱很感谢上天。

I LOVE YOU
'''
msg = MIMEText(text, "plain", "utf-8")

# 邮件头信息
msg['From'] = Header("per pa")
msg['To'] = Header(to_addr)
# msg['Subject'] = Header("I LOVE YOU")
msg['Subject'] = Header("爱你哟", 'utf-8')

#如果端口是用SSL加密，请这样写代码，否则一般是smtp.SMTP()
# server = smtp.SMTP(smtp_server, 465)
server = smtp.SMTP_SSL(smtp_server, 465)
# server.connect(smtp_server, 465)
#如果出现编码错误UnicodeDecodeError，可以这样写：server.connect('smtp.qq.com', 465,'utf-8')
# server.set_debuglevel(1)
# 登录发信邮箱
server.login(from_addr, password)
# 发送邮件
server.sendmail(from_addr, to_addr, msg.as_string())
# 关闭服务器
server.quit()