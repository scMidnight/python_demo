#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from urllib.request import quote
#quote()函数，可以帮我们把内容转为标准的url格式，作为网址的一部分打开

'''

用户输入喜欢的电影名字，
程序即可在电影天堂
https://www.ygdy8.com
爬取电影所对应的下载链接，
并将下载链接打印出来

'''

url = 'http://s.ygdy8.com/plus/so.php?typeid=1&keyword='
move_name = input("请输入要看的电影名称")
move_namea = move_name.encode('gbk')
move_namea = quote(move_namea)
url = url + move_namea
res = requests.get(url)
res.encoding = res.apparent_encoding
if(res.status_code == 200):
    bs = BeautifulSoup(res.text, "html.parser")
    bs = bs.find('div', class_='co_content8')
    table = bs.find('table')
    if(table != None):
        tr = table.find('tr')
        url = 'https://www.ygdy8.com' + tr.find('a')['href']
        donlRes = requests.get(url)
        donlRes.encoding = donlRes.apparent_encoding
        donlBs = BeautifulSoup(donlRes.text, 'html.parser')
        cili_link = donlBs.find('div', id='Zoom').find('p').find('a')['href']
        xl_link = donlBs.find('div', class_='co_content8').find('table').find('a')['href']
        print("电影《%s》\n磁力下载地址为：%s\n迅雷下载地址为：%s" % (move_name, cili_link, xl_link))
    else:
        print('无数据哦')
else:
    print('访问失败哦~~~')