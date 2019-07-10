#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
# 引用requests库
music_name = input("请输入歌曲名称")
for i in range(5):
    params = {
            'ct': '24',
            'qqmusic_ver': '1298',
            'new_json': '1',
            'remoteplace': 'txt.yqq.song',
            'searchid': '65537859516187558',
            't': '0',
            'aggr': '1',
            'cr': '1',
            'catZhida': '1',
            'lossless': '0',
            'flag_qc': '0',
            'p': str(i+1),
            'n': '10',
            'w': music_name,
            'g_tk': '5381',
            'loginUin': '0',
            'hostUin': '0',
            'format': 'json',
            'inCharset': 'utf8',
            'outCharset': 'utf-8',
            'notice': '0',
            'platform': 'yqq.json',
            'needNewCode': '0'
        }
    url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
    res = requests.get(url, params=params)
    # 调用get方法，下载这个字典
    json_music = res.json()
    for item in json_music['data']['song']['list']:
        print(item['name'])
        # 以name为键，查找歌曲名
        print('所属专辑：' + item['album']['name'])
        # 查找专辑名
        print('播放时长：' + str(item['interval']) + '秒')
        # 查找播放时长
        print('播放链接：https://y.qq.com/n/yqq/song/' + item['mid'] + '.html\n\n')
        # 查找播放链接