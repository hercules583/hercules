#!/usr/bin/env python
#!-*- coding:utf-8 -*-
import requests


# 作文大全
def zuowen(ip_name,key_1,id_1):
	url="http://%s/zuowen/typeList"%(ip_name)
	param={"key":key_1,"id":id_1}
	res=requests.get(url,param)
	return res

if __name__ == '__main__':
	re=zuowen("zuowen.api.juhe.cn","04adb605ebad26611e9c20059e900b1b",2)
	print("作文大全请求的结果是：",re.json())