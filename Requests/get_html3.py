#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

resp = requests.get("https://spidermen.cn/")

html = resp.text

soup = BeautifulSoup(html, 'html.parser')

items = soup.find_all('header', class_='entry-header')

for item in items:
    times = item.find('div', class_='entry-meta').find('a').find('time').text
    title = item.find('h2').find('a').text
    a = item.find('h2').find('a')['href']
    print('文章标题：%s，发布时间：%s，文章连接：%s' % (title, times, a))