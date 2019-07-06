#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

resp = requests.get("https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html")

html = resp.text

#第0个参数是要被解析的文本,必须是字符串
#第1个参数用来标识解析器,用的是一个Python内置库：html.parser（它不是唯一的解析器，但是比较简单的）
soup = BeautifulSoup(html, 'html.parser')#把网页解析为BeautifulSoup对象

'''BeautifulSoup中提取数据两大知识点：find()与find_all()，Tag对象
Tag对象的三种常用属性与方法
Tag.find(),Tag.find_all()  提取Tag中的Tag
Tag.text  提取Tag中的文字
Tag['属性名']  输入参数：属性名，可以提取Tag中这个属性的值
'''
items = soup.find_all(class_='books')
for item in items:
    print(item)
