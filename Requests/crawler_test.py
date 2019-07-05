#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

res = requests.get('https://res.pandateacher.com/2018-12-18-10-43-07.png')
pic = res.content   #把Reponse对象的内容以二进制数据的形式返回
photo = open('F:\\one.jpg', 'wb')
photo.write(pic)
photo.close()

res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
#下载《三国演义》第一回，得到一个对象，它被命名为res
novel = res.text #把Response对象的内容以字符串的形式返回
print(novel[:100])