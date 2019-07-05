#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

res = requests.get("https://static.pandateacher.com/Over%20The%20Rainbow.mp3")

resContent = res.content

musicF = open('F:\\resContent.mp3', 'wb')

musicF.write(resContent)

musicF.close()