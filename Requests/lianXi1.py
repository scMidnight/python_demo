#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

#获取响应码内容
res = requests.get("https://localprod.pandateacher.com/python-manuscript/crawler-html/exercise/HTTP%E5%93%8D%E5%BA%94%E7%8A%B6%E6%80%81%E7%A0%81.md")
cont = res.text
f = open('F:\\响应码内容.txt', 'w')
f.write(cont)
f.close()