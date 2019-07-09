#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests, random, bs4

#方式一
for x in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
    res = requests.get(url)
    bs = bs4.BeautifulSoup(res.text, 'html.parser')
    bs = bs.find('ol', class_="grid_view")
    for titles in bs.find_all('li'):
        num = titles.find('em',class_="").text
        #查找序号
        title = titles.find('span', class_="title").text
        #查找电影名
        tes = titles.find('span',class_="inq").text
        #查找推荐语
        comment = titles.find('span',class_="rating_num").text
        #查找评分
        url_movie = titles.find('a')['href']
        print(num + '.' + title + '——' + comment + '\n' + '推荐语：' + tes +'\n' + url_movie)

