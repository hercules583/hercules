#!/usr/bin/env python
#!-*- coding:utf-8 -*-
#@Time   :2020/7/1316:02
#@Email  :hercules583@163.com
#File    :lesson2.py
#software:PyCharm
#list0=[1,3.14,True,"naihe",[1,2,3]]
# print(list0)
# 取值
# print(list0[3])#索引取第四个值
# print(list0[0:3])#取出前三个
# print(list0[:len(list0)])#取出全部
# print(list0[-1][2])#取出嵌套的列表的3
# list0=[1,3.14,True,"naihe",[1,2,3]]
# #增加值
# list0.append('nihao')#在列表后面增加元素，每次只能增加一个
# list0.insert(3,"tudou")#在列表指定位置增加元素
# print(list0)
#list0=[1,3.14,True,"naihe",[1,2,3]]
# #删除值
# list0.pop(1)#删除指定位置的值，不写索引默认删除最后一个
# print(list0)
# del list0[1] #删除指定位置的值
# print(list0)
# list0.clear()#删除全部的值
# print(list0)
# list0=[1,3.14,True,"naihe",[1,2,3]]
# #改值
# list0[3]="tudou"
# print(list0)
# tuple1=(1,3.14,True,"naihe",[1,2,3])
# tuple2=("增加",)
# print(tuple1*2)
# print(tuple1[3])
#dict_1={"name":"leihou","age":18,"money":99.99,"score":(88,99,100)}
# print(dict_1)
# #取值
# print(dict_1["name"])#通过key取值
# print(dict_1.get("age"))#通过get方法取值
# print(dict_1.items())#以列表形式取出字典的值
# print(dict_1.keys())#取出所有key，以列表形式，这样我们可以用for循环遍历字典
# print(dict_1.values())#取出所有的value
#dict_1={"name":"leihou","age":18,"money":99.99,"score":(88,99,100)}
#增加
# dict_1["weight"]="100"#key不存在就是增加，key存在就是修改
# print(dict_1)
# dict_1.update({"weight":120,"bobby":"girl"})#update方法增加多个
# print(dict_1)
# dict_1={"name":"leihou","age":18,"money":99.99,"score":(88,99,100)}
# #改
# dict_1["money"]="100"#key不存在就是增加，key存在就是修改
# print(dict_1)
# dict_1.update({"money":120,"age":"19"})#一次改多个
# print(dict_1)
# dict_1={"name":"leihou","age":18,"money":99.99,"score":(88,99,100)}
# #删
# dict_1.pop("score")#删除字典元素
# print(dict_1)
# del dict_1["name"]#删除
# print(dict_1)
# dict_1.popitem()#随机删除一组数据
# print(dict_1)
# dict_1.clear()#清空字典
# print(dict_1)
# money=int(input("请输入你的存款余额："))
# if money >=100:
#     print("国外游")
# elif money >=50:
#     print("省内游")
# elif money >=10:
#     print("楼下游")
# else:
#     print("好好学习挣钱吧!，骚年")
# str1="速成14期的每一个学生都能拿高薪!"
# count=0
# for i in str1:
#     print(i)
#     if i =="拿":
#         #break
#         continue
#     count += 1  # 计数器
# print(count)
#print(len(str1))
# a=[1,2,"6","summer"]
# def if_1(b):
#     for i in range(len(a)):
#         if b in str(a[i]):
#             return a[i]
# re=if_1("i")
# print(re)

# dict_1={"class_id":45,"num":20}
# def count(i):
#     if dict_1["num"]>i:
#         print(dict_1["num"])
#     else:
#         print("课堂人数小于{}".format(i))
# re=count(5)


# list3=["先森","小米椒","lucia"]
# a={}
# b=[]
# def member():
#     for i in range(len(list3)):
#         name=input("name:")
#         sex=input("sex:")
#         age=input("age:")
#         city=input("city:")
#         a.update({"name":name,"sex":sex,"age":age,"city":city})
#         b.append(dict(a))
#     return b
# re=member()
# print(re)

# def good_job(bouns,subsidy,salary=9000,*args,**kwargs):#定义函数，传入形参
#     print("bonus:{}".format(bouns))
#     print("subsidy：{}".format(subsidy))
#     print("salary:{}".format(salary))
#     print("args:{}".format(args))
#     print("kwargs{}".format(kwargs))
#     sum1=bouns+subsidy+salary#薪资总和
#     for i in args:#使用for循环加上不定长参数元祖的值
#         sum1+=i
#     for j in kwargs:#使用for循环加上关键字不定长字典的值
#         sum1+=kwargs.get(j)
#     if sum1 > 10000:
#         print("还不错，加油干!")
#     else:
#         print("提升自己，跳槽吧.")
#     return sum1#定义多个返回值
# re=good_job(1000,500,8000,200,100,a=10,b=100)#调用函数，并传参
# print(re)

# def change():
#     str_1 = input("请输入一个字符串：")
#     a=[]
#     for i in str_1:
#         a.append(i)
#     return a
# re=change()
# print(re)
# def sum_1(start=0,stop=100):
# #求任意整数序列的和
#     sum=0
#     for i in range(start,stop):
#         sum+=i
#     return sum
# re=sum_1(50,100)
# print(re)
# def judge():
# #判断对象长度是否大于5
#     t=input("请输入一个对象:")
#     if len(t)>5:
#         print(True)
#     else:
#         print(False)
# re=judge()

# a=input("请输入：")
# print(a)
# print("hello,world!")
# list_1=[]
# list_1.append(1)
# list_1.pop(0)
# list_1.insert(0,"a")
# print(list_1)

# for i in range(0,10,2):
#     print(i)