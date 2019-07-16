#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests,random
agent_list = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400']
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
        'w': '周杰伦',
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
    music_json = res.json()
    music_dict = music_json['data']['song']['list']
    lyric_url = 'https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg'
    for music in music_dict:
        print(music['name'])
        lyric_referer = 'https://y.qq.com/n/yqq/song/' + music['mid'] + '.html'
        lyric_headers = {
            'origin': 'https://y.qq.com',
            # 请求来源
            'referer': lyric_referer,
            # 请求来源，携带的信息比“origin”更丰富，记录浏览器上次访问的URL
            'user-agent': random.choice(agent_list)
            # 标记了请求从什么设备，什么浏览器上发出，来标识请求的浏览器身份
        }
        lyric_params = {
            'nobase64': '1',
            'musicid': music['id'],
            '-': 'jsonp1',
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
        lyric_res = requests.get(lyric_url, headers=lyric_headers, params=lyric_params)
        lyric_json = lyric_res.json()
        # data = gzip.decompress(lyric_json['lyric'])
        # data = gzip.decompress(lyric_res.content)
        print(lyric_json['lyric'])