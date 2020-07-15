#!/usr/bin/env python
#!-*- coding:utf-8 -*-
#@Time   :2020/7/1415:47
#@Email  :hercules583@163.com
#File    :lesson3.py
#software:PyCharm
import requests
import jsonpath
def register(url,data):
    headers_reg = {"X-Lemonban-Media-Type":"lemonban.v2","Content-Type":"application/json"}
    re=requests.post(url=url,json=data,headers=headers_reg)
    response=re.json()
    return response
# url_reg= "http://120.78.128.25:8766/futureloan/member/register"
# data_reg= {"mobile_phone":18204960966,"pwd":"naihe123456"}
# result=register(url_reg,data_reg)
# print(result)

# def login(url,data):
#     headers_reg = {"X-Lemonban-Media-Type":"lemonban.v2","Content-Type":"application/json"}
#     re=requests.post(url=url,json=data,headers=headers_reg)
#     response=re.json()
#     return response
# url_reg= "http://120.78.128.25:8766/futureloan/member/login"
# data_reg= {"mobile_phone":18204960966,"pwd":"naihe123456"}
# result=login(url_reg,data_reg)
# print(result)
# token=jsonpath.jsonpath(result,"$..token")[0]
# member_id=jsonpath.jsonpath(result,"$..id")[0]
# #token=result["data"]["token_info"]["token"]
# print(token)
# #member_id=result["data"]["id"]
# print(member_id)
#
# def recharge(url,data,headers):
#     re=requests.post(url=url,json=data,headers=headers)
#     response=re.json()
#     return response
# url_reg= "http://120.78.128.25:8766/futureloan/member/recharge"
# data_reg= {"member_id":member_id,"amount":100}
# headers_reg = {"X-Lemonban-Media-Type":"lemonban.v2","Content-Type":"application/json","Authorization":"Bearer"+" "+token}
# result=recharge(url_reg,data_reg,headers_reg)
# print(result)

#面试题，访问百度接口请求
url_baidu="https://www.baidu.com/"
headers_baidu={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
response=requests.get(url=url_baidu,headers=headers_baidu)
print(response.content.decode("utf8"))