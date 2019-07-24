#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options # 从options模块中调用Options类
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import time

firefox_option = Options()# 实例化Option对象
firefox_option.add_argument('--headless') # 把浏览器设置为静默模式

driver = webdriver.Firefox(options=firefox_option)# 设置引擎为Firefox，在后台默默运行
driver.get('https://y.qq.com/n/yqq/song/000xdZuV2LcQ19.html')
time.sleep(3)
pageSource = driver.page_source # 获取Elements中渲染完成的网页源代码
soup = BeautifulSoup(pageSource,'html.parser')  # 使用bs解析网页
comments = soup.find('ul', class_='js_hot_list').find_all('li', class_='js_cmt_li')
# loadAllBtn = driver.find_element_by_class_name('comment__show_all_link')
# loadAllBtn.click()
# time.sleep(2)
# comments = driver.find_element_by_class_name('js_hot_list').find_elements_by_class_name('js_cmt_li') # 使用class_name找到评论
print(len(comments)) # 打印获取到的评论个数
for comment in comments:
    # p = comment.find_element_by_tag_name("p")
    p = comment.find('p')
    print(p)

driver.close()