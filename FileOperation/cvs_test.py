#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
#csv中文文档：https://yiyibooks.cn/xx/python_352/library/csv.html#module-csv

csv_file = open('demo.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(csv_file)
writer.writerow(['电影', '豆瓣评分'])
writer.writerow(['银河护卫队','8.0'])
writer.writerow(['复仇者联盟','8.1'])
csv_file.close()


with open('demo.csv', 'r', newline='', encoding='utf-8-sig') as f:
    ader = csv.reader(f)
    for row in ader:
        print(row)