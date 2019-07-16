#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests,random
from bs4 import BeautifulSoup

agent_list = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400']

kddh = input('请输入快递单号：')

comCode_res = requests.get('https://www.kuaidi100.com/autonumber/autoComNum?resultv2=1&text=' + kddh)

com_code_json = comCode_res.json()
com_code = com_code_json['auto'][0]['comCode']

temp = random.uniform(0, 1)

params = {
'type': com_code,
'postid': kddh,
'temp': temp,
'phone': '5288'
}
headers = {
            'referer': 'https://www.kuaidi100.com/',
            # 请求来源，携带的信息比“origin”更丰富，记录浏览器上次访问的URL
            'user-agent': random.choice(agent_list)
            # 标记了请求从什么设备，什么浏览器上发出，来标识请求的浏览器身份
        }
url = 'https://www.kuaidi100.com/query'
res = requests.get(url, headers=headers, params=params)

res_json = res.json()

res_dict = res_json['data']

for info in res_dict:
    print('在 %s，包裹信息为：%s' % (info['time'], info['context']))