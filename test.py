#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time, os
# class jiqiren:
#     def __init__(self, jName, mName):
#         self.jName = jName
#         self.mName = mName
#         print("你好，%s。我是%s。遇见你，真好。" % (mName, jName))
#
#     def say_wish(self, yuanwang):
#         print("%s的愿望是：" % self.mName)
#         for i in range(3):
#             print(yuanwang)
# jiqiren = jiqiren('小机机', '爸爸')
# jiqiren.say_wish("挣够100万")
for i in range(10, 0, -1):
    info = '请专注任务，还要保持专注' + str(i) + '秒哦！'
    print(info, end='')
    time.sleep(1)
    print("\b"*(len(info)), end='', flush=True)
a = time.time()
# print(a)
# b = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(a))
# print(b)
print(os.getcwd())
print(os.listdir(os.getcwd()))
print(dir(os))