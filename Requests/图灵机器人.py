#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests,json,random

session = requests.session()

agent_list = [
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400']

headers = {
            'origin': 'http://openapi.tuling123.com/',
            'referer': 'http://openapi.tuling123.com/',
            'user-agent': random.choice(agent_list)
            # 标记了请求从什么设备，什么浏览器上发出，来标识请求的浏览器身份
        }

data = {
    "reqType":0,
    "perception": {
        "inputText": {
                "text": "你好啊"
            }
    },
    "userInfo": {
        "apiKey": "3c2d7a3296804aeeaa764fc393e04dde",
        "userId": "374137689"
    }
}
url = 'http://openapi.tuling123.com/openapi/api/v2'
res = session.post(url, data=json.dumps(data), headers=headers)
res_dict = res.json()
print(res_dict['results'][0]['values']['text'])