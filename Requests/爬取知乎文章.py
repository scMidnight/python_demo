#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests, random, csv, openpyxl
from openpyxl.styles import Alignment

url = 'https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles'
agent_list = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400']
info_list = []
for i in range(0, 2):
    headers = {
        # "referer": "https://www.zhihu.com/people/zhang-jia-wei/posts/posts_by_votes?page=" + str(i),
        "user-agent": random.choice(agent_list)
        # 标记了请求从什么设备，什么浏览器上发出，来标识请求的浏览器身份
    }
    params = {
        "include": "data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics",
        "offset": str(i*20),
        "limit": "20",
        "sort_by": "voteups"
    }
    rep = requests.get(url, headers=headers, params=params)
    info_json = rep.json()
    info_data = info_json['data']
    for info in info_data:
        title = info['title']
        excerpt = info['excerpt']
        info_url = info['url']
        info_list.append([title, excerpt, info_url])

with open('G:\\知乎文章.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['标题', '摘要', '链接'])
    for row in info_list:
        writer.writerow(row)

align = Alignment(horizontal='center',vertical='center',wrap_text=False)
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = '知乎文章'
sheet.append(['标题', '摘要', '链接'])
for i in info_list:
    sheet.append(i)
for row in sheet.rows:
    for cell in row:
        cell.alignment = align
wb.save("G:\\知乎文章.xlsx")