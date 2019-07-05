#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

#获取图片
res = requests.get('https://res.pandateacher.com/2019-01-12-15-29-33.png')

pic = res.content

f = open('test.jpg', 'wb')
f.write(pic)
f.close()