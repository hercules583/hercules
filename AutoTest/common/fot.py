#!/usr/bin/env python
#!-*- coding:utf-8 -*-

# for (i,j) in zip(range(10), range(10)):
# 	print (i,j)

import requests

url = "http://zuowen.api.juhe.cn/zuowen/typeList?key=04adb605ebad26611e9c20059e900b1b&id=2"

payload = {}
headers = {
  'Cookie': 'aliyungf_tc=AQAAAO55mD9EkAcAJxWn362QvxuGgOI+'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.json())