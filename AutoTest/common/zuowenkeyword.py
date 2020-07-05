#!/usr/bin/env python
#!-*- coding:utf-8 -*-
import requests
import selenium
from selenium import webdriver
import time
# 作文大全
def zuowen(zuowen_ip,key,id):
	url="http://%s/zuowen/typeList"%(zuowen_ip)
	param={"key":key,"id":id}
	res=requests.get(url,param)
	re=res.json()
	return re['reason']

def OB(browser_url):
	global dr
	dr = webdriver.Chrome()
	dr.maximize_window()
	dr.get(browser_url)

def register(ip,port,mobile_phone,pwd,type,reg_name):
	url = "http://%s:%s/futureloan/member/register"%(ip,port)
	param = {"mobile_phone": mobile_phone, "pwd": pwd,"type":type,"reg_name":reg_name}
	headers = {"X-Lemonban-Media-Type": "lemonban.v2", "Content-Type": "application/json"}
	res = requests.post(url, param,headers=headers)
	re = res.json()
	return re['msg']

def login(ip,port,moblie_phone,pwd):
	url = "http://%s:%s/futureloan/member/login"%(ip,port)
	param = {"mobile_phone":moblie_phone, "pwd": pwd}
	headers = {"X-Lemonban-Media-Type": "lemonban.v2", "Content-Type": "application/json"}
	res = requests.post(url, param,headers=headers)
	re = res.json()
	return re

def recharge(ip,port,member_id,amount,token_id):
	url = "http://%s:%s/futureloan/member/recharge"%(ip,port)
	param = {"member_id":member_id, "amount": amount}
	Authorization='Bear' + ' '+token_id
	headers = {"X-Lemonban-Media-Type": "lemonban.v2", "Content-Type": "application/json","Authorization":Authorization}
	res = requests.post(url, param,headers=headers)
	re = res.json()
	return re['msg']


# def OB(browser_url):
# 	driver = webdriver.Chrome()
# 	driver.maximize_window()
# 	driver.get(browser_url)
# 	driver.find_element_by_id("kw").send_keys("中国")
# 	driver.find_element_by_id('su').submit()
# 	time.sleep(2)
if __name__ == '__main__':
	re=OB('https://www.baidu.com')
# r=zuowen("zuowen.api.juhe.cn","04adb605ebad26611e9c20059e900b1b",2)
# print (r)
# 	print (type(r))
# 	# print (re['result']['id'])