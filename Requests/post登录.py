#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests, random, json

session = requests.session()
#用requests.session()创建session对象，相当于创建了一个特定的会话，帮我们自动保持了cookies。

agent_list = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400']

headers = {
    'user-agent': random.choice(agent_list)
    # 标记了请求从什么设备，什么浏览器上发出，来标识请求的浏览器身份
}
#加请求头，前面有说过加请求头是为了模拟浏览器正常的访问，避免被反爬虫。

#cookies读取
def cookies_read():
    cookies_txt = open('G:\\cookies.txt', 'r')
    cookies_dict = json.loads(cookies_txt.read())
    # 调用json模块的loads函数，把字符串转成字典。
    cookies_txt.close()
    cookies = requests.utils.cookiejar_from_dict(cookies_dict)
    # 把转成字典的cookies再转成cookies本来的格式。
    return (cookies)

#cookies存储。
def sign_in():
    url = ' https://wordpress-edu-3autumn.localprod.forc.work/wp-login.php'
    data = {'log': input('请输入你的账号'),
            'pwd': input('请输入你的密码'),
            'wp-submit': '登录',
            'redirect_to': 'https://wordpress-edu-3autumn.localprod.forc.work/wp-admin/',
            'testcookie': '1'}
    session.post(url, headers=headers, data=data)
    cookies_dict = requests.utils.dict_from_cookiejar(session.cookies)
    #把cookies转化成字典。
    cookies_str = json.dumps(cookies_dict)
    # 调用json模块的dumps函数，把cookies从字典再转成字符串。
    f = open('G:\\cookies.txt', 'w')
    f.write(cookies_str)
    f.close()

#发表评论。
def write_message():
    url = 'https://wordpress-edu-3autumn.localprod.forc.work/wp-comments-post.php'
    data = {
        'comment': input('请输入你要发表的评论：'),
        'submit': '发表评论',
        'comment_post_ID': '13',
        'comment_parent': '0'
    }
    return (session.post(url, headers=headers, data=data))

try:
    session.cookies = cookies_read()
except FileNotFoundError:
    sign_in()
    session.cookies = cookies_read()

def go():
    resp = write_message()
    print(resp.status_code)
    if resp.status_code == 200:
        print('评论成功')
    else:
        sign_in()
        session.cookies = cookies_read()
        go()

#spiderman,crawler334566
go()