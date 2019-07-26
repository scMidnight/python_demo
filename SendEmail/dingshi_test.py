#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests,random,schedule,time
from bs4 import BeautifulSoup

def job():
    print("I'm working...")
#定义一个叫job的函数，函数的功能是打印'I'm working...'

schedule.every(10).seconds.do(job)        #每2s执行一次job()函数
# schedule.every(10).minutes.do(job)       #部署每10分钟执行一次job()函数的任务
# schedule.every().hour.do(job)            #部署每×小时执行一次job()函数的任务
# schedule.every().day.at("10:30").do(job) #部署在每天的10:30执行job()函数的任务
# schedule.every().monday.do(job)          #部署每个星期一执行job()函数的任务
# schedule.every().wednesday.at("13:15").do(job)#部署每周三的13：15执行函数的任务

while True:
    schedule.run_pending()
    time.sleep(1)
#检查上面的任务部署情况，如果任务已经准备就绪，就去启动执行。其中，第20行的time.sleep(1)是让程序按秒来检查，如果检查太快，会浪费计算机的资源