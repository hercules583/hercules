#!/usr/bin/env python
#!-*- coding:utf-8 -*-
#@Time   :2020/7/1016:42
#@Email  :hercules583@163.com
#File    :lesson1.py
#software:PyCharm

# number_1=10
# number_2=3.1415926
# name="奈何"
# name_1=True
# print(type(name_1))
# aaa=input("魔镜魔镜谁最美？")
# print(aaa)
# a='lemon'
# print(a[2])#正序索引从0开始
# print(a[-1])#反序索引从-1开始

# a='lemon\nbest'#加R,r或者/转意换行符/n（换行），制表符/r(数据之间空格)等，转意成普通字符含义
# print(a)

# a='1'
# print(type(a))#加成对的双引号单引号三引号里面的内容都是字符串类型
# # print('''
#       '奈何'
#       是大佬
#       ''')

# a='le'
# b="mon"
# print(a+b)#字符串的运算+，拼接字符串
# a="我是谁，我在那？"
# print("在" in a)


# a='lemon'
# # print(a*2)#字符串的运算*，重复输出字符串
# # a="hello"
#
# # print("o" in a)#判断字符串in not in成员运算符，返回布尔值（True，False）
#
# a="hello"
# b=666
# print(a+str(b))#不同类型的数据不可以拼接，可以转换成相同类型的再拼接
#
# a="lemon"
# res=a[0:5:2]
# print(res)#字符串切片：字符串名[m:n:k],m字符串索引开始的地方，n字符串索引结束的地方+1，k步长,如果不写k则k默认为1；
# a="lemon"
# res=a[:]#res=a[0:]默认从头取到尾,res=[1:]默认从1取到尾
# print(res)
# str_1="hello lemon class"
# res=str_1[1:17:2]
# print(res)#取出字符串中所有的奇数位，空格也算一个字符
#
# age=18
# name="小猴子"
# score=99.99
# print(name+"今年"+str(age)+"岁")#如果字符串很长，转换格式很不便捷，固需要用到格式化输出%d整数,f%浮点数,s%字符串
# print("%s今年%d岁"%(name,age))
# print("%s今年%d岁数学考了%.2f分"%(name,age,score))
# #前面是占坑，后面是给坑赋值，前面是%d的话后面只能整数，%f可以整数也可以浮点数，%s都可以，%.2f表示浮点数保留两位小数
# print("{2}今年{0}岁，数学考了{1}分".format(age,name,score))#{}里面不取值则按顺序取值，里面取值则按索引取值

# str_1="hello"
# res=str_1.upper()
# print("转换后的结果是：{}".format(res))#大小写转换用upper(),lower()
#
# str_1="Hello"
# res=str_1.find("o")
# print("查找后的结果是：{}".format(res))
# 字符串的查找函数是find（），找到返回单个字符索引，查找子字符串找到返回第一个字符的索引，没找到返回-1
#
# str_1="Hello"
# res=str_1.index("l")
# print("查找后的结果是：{}".format(res))

# str_1="Hello"
# res=str_1.replace("H","h")
# print("替换后的结果是：{}".format(res))
#字符串的替换函数replace（"","",1）前面是你要替换的字符，后面是要替换的字符，如果有两个后面的1表示替换一次
#
# str_1="Hello"
# res=str_1.split("l")
# print("切割后的结果是：{}".format(res))
#字符串的切割函数split("")，将切割后的片段存在列表里，类型还是字符串
#
# str_1="@@@He@llo@@"
# res=str_1.strip("@")
# print("切割后的结果是：{}".format(res))
# #字符串头尾处理函数strip（），只去掉头尾制定的字符，不能处理中间的

# re_1=input("请输入姓名：")
# re_2=input("请输入年龄：")
# re_3=input("请输入性别：")
# print("*"*20)
# print("姓名:"+re_1)
# print("性别:"+re_3)
# print("年龄:"+re_2)
# print("*"*20)

# re_1=input("请输入姓名：")
# re_2=input("请输入年龄：")
# re_3=input("请输入性别：")
# print("*"*20  + "\n姓名："+re_1+"\n性别："+re_3+"\n年龄："+re_2+"\n"+"*"*20)

# str1="python hello aaa 123123aabb"
# print(str1[:6])
# print("o a"in str1)
# print("he"in str1)
# print("ab"in str1)
# print(str1.replace("python","lemon"))
# print(str1.find("aaa"))

# fo = open("C:\\Users\\Administrator\\Desktop\\p\\1.py","r+", encoding='gbk')
# # fo.write("你最帅！")
# str = fo.read(10)
# print ("读取的字符串是 : ", str)
# print ("文件名",fo.name)
# print ("是否已关闭 : ",fo.closed)
# print ("访问模式 : ", fo.mode)
# fo.close()
# print ("是否已关闭 : ",fo.closed)
# 打开一个文件
fo = open("C:\\Users\\Administrator\\Desktop\\p\\1.py","r+",encoding='gbk')
str = fo.read(10)
print("读取的字符串是 : ", str)
#
# # 查找当前位置
position = fo.tell()
print("当前文件位置 : ", position)
#
# # 把指针再次重新定位到文件开头
position = fo.seek(0, 0)
str = fo.read(2)
print("重新读取字符串 : ", str)
# 关闭打开的文件
fo.close()
