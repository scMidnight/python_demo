#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests, openpyxl
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
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = 'song'
    sheet['A1'] = '歌曲名'
    sheet['B1'] = '所属专辑'
    sheet['C1'] = '播放时长'
    sheet['D1'] = '播放链接'
    for item in json_music['data']['song']['list']:
        name = item['name']
        # 以name为键，查找歌曲名
        album = item['album']['name']
        # 查找专辑名
        time = item['interval']
        # 查找播放时长
        link = 'https://y.qq.com/n/yqq/song/' + str(item['mid']) + '.html\n\n'
        # 查找播放链接
        sheet.append([name, album, time, link])
wb.save('Jay.xlsx')