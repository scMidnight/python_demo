#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from bs4 import Tag

resp = requests.get("http://books.toscrape.com/catalogue/category/books/travel_2/index.html")

html = resp.text

soup = BeautifulSoup(html, 'html.parser')

parents = soup.find('ol', class_='row')

for li in parents:
    if(isinstance(li, Tag)):
        book_name = li.find('h3').find('a')['title']
        price = li.find('div', class_='product_price').find('p').text
        p = li.find('p', class_='star-rating')
        pf = 0
        p_n = p['class']
        if('One' in p_n):
            pf = 1
        elif('Two' in p_n):
            pf = 2
        elif('Three' in p_n):
            pf = 3
        elif('Four' in p_n):
            pf = 4
        elif('Five' in p_n):
            pf = 5
        print('书名：%s，价格：%s，评分：%s分' % (book_name, price, pf))