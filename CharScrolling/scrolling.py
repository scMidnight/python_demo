#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os,time

def main():  # 用函数封装，可复用性会高一些（可在其他的.py文件里调用该函数。）
    content = '广告滚动效果'  # 广告词可自定义。
    while True:
        os.system('cls')  # linux/os x系统；windows 系统中，这个命令是 os.system('cls')，效果：清屏。
        print(content)
        content = content[1:] + content[0]  # 这行代码相当于：将字符串中第一个元素移到了最后一个。
        time.sleep(1)  # 你可以改下时间，体会“循环周期”和“滚动速度”之间的关联。


if __name__ == '__main__':  # 类里面学到的检测方法，在函数中其实也可以用。
    main()