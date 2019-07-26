#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests,random,schedule,time
from bs4 import BeautifulSoup
import smtplib as smtp
from email.header import Header
from email.mime.text import MIMEText

def weather_spider():
    agent_list = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400']
    url = 'http://www.weather.com.cn/weather/101010100.shtml'
    headers = {
        'user-agent': random.choice(agent_list)
    }
    res = requests.get(url, headers=headers)
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, "html.parser")
    one = soup.find('ul', class_='t clearfix').find('li')
    tq = one.find('p', class_='wea')
    wd = one.find('p', class_='tem')

    return tq.text, wd.text

def send_email(weather, tem):
    # 发信方的信息：发信邮箱，QQ邮箱授权码）
    from_addr = "374137689@qq.com"
    password = "gmbhselbogaccbdd"
    # 收信方邮箱
    to_addr = '374137689@qq.com'
    # 发信服务器
    smtp_server = 'smtp.qq.com'
    qq_mail = smtp.SMTP_SSL(smtp_server, 465)
    # 登录发信邮箱
    qq_mail.login(from_addr, password)
    content = '亲爱的，今天的天气是：' + weather + tem
    message = MIMEText(content, 'plain', 'utf-8')
    message['Subject'] = Header('今日天气预报', 'utf-8')
    try:
        qq_mail.sendmail(from_addr, to_addr, message.as_string())
        print('邮件发送成功')
    except:
        print('邮件发送失败')
    qq_mail.quit()

def job():
    print('开始一次任务')
    weather,tem = weather_spider()
    send_email(weather,tem)
    print('任务完成')

schedule.every().day.at("20:15").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)