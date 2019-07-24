#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 本地Chrome浏览器设置方法
from selenium import webdriver#从selenium库中调用webdriver模块
import time

# driver = webdriver.Chrome()# 设置引擎为Chrome，真实地打开一个Chrome浏览器
driver = webdriver.Firefox()# 设置引擎为Firefox，真实地打开一个Firefox浏览器
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
time.sleep(2)
label = driver.find_elements_by_tag_name('label') # 解析网页并提取第一个<lable>标签
print(type(label))
print(driver.page_source)
teacher = driver.find_element_by_id('teacher')
teacher.send_keys('必须是吴枫呀')
assistant = driver.find_element_by_name('assistant')
assistant.send_keys('都喜欢')
time.sleep(1)
button = driver.find_element_by_class_name('sub')
time.sleep(1)
button.click()
time.sleep(1)
print(driver.page_source)
driver.close()

'''
find_element_by_tag_name：通过元素的名称选择
如<h1>你好，蜘蛛侠！</h1> 
可以使用find_element_by_tag_name('h1')

find_element_by_class_name：通过元素的class属性选择
如<h1 class="title">你好，蜘蛛侠！</h1>
可以使用find_element_by_class_name('title')

find_element_by_id：通过元素的id选择
如<h1 id="title">你好，蜘蛛侠！</h1> 
可以使用find_element_by_id('title')

find_element_by_name：通过元素的name属性选择
如<h1 name="hello">你好，蜘蛛侠！</h1> 
可以使用find_element_by_name('hello')

以下两个方法可以提取出超链接

find_element_by_link_text：通过链接文本获取超链接
如<a href="spidermen.html">你好，蜘蛛侠！</a>
可以使用find_element_by_link_text('你好，蜘蛛侠！')

find_element_by_partial_link_text：通过链接的部分文本获取超链接
如<a href="https://localprod.pandateacher.com/python-manuscript/hello-spiderman/">你好，蜘蛛侠！</a>
可以使用find_element_by_partial_link_text('你好')
'''