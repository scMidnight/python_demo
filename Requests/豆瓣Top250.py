#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests, random, bs4, csv, openpyxl
from openpyxl.styles import Alignment

agent_list = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400']
file_titles = ['排名', '电影名','评分','推荐语','链接']
contents = []
for x in range(10):
    params = {
        "start": str(x*25),
        "filter": ''
    }
    headers = {
        'user-agent': random.choice(agent_list),
        # 标记了请求从什么设备，什么浏览器上发出，来标识请求的浏览器身份
        'Host': 'movie.douban.com'
    }
    url = 'https://movie.douban.com/top250'
    res = requests.get(url, headers=headers, params=params)
    bs = bs4.BeautifulSoup(res.text, 'html.parser')
    bs = bs.find('ol', class_="grid_view")
    for titles in bs.find_all('li'):
        num = titles.find('em',class_="").text
        #查找序号
        title = titles.find('span', class_="title").text
        #查找电影名
        tes = ''
        if titles.find('span',class_="inq") != None:
            tes = titles.find('span',class_="inq").text
        else:
            tes = '无'
        #查找推荐语
        comment = titles.find('span',class_="rating_num").text
        #查找评分
        url_movie = titles.find('a')['href']
        contents.append([num, title, comment, tes, url_movie])

#csv
with open('G:\\豆瓣Top250.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(file_titles)
    for i in contents:
        writer.writerow(i)

#Excel
align = Alignment(horizontal='center',vertical='center',wrap_text=False)
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = '豆瓣Top250'
sheet.append(file_titles)
for i in contents:
    sheet.append(i)
for row in sheet.rows:
    for cell in row:
        cell.alignment = align
wb.save('G:\\豆瓣Top250.xlsx')