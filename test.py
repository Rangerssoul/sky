# coding: UTF-8
# 作者    ：蒲海铭
# 版权所有：Rangerssoul
# 开发时间：2018/12/21 22:12
# 文件名称：test.py
# 开发工具：PyCharm



import datetime
import random

fp = open(r'E:\develope\pyproject\sky\a.txt', 'a+')
#a = 10
#b = 5

print('当前年份是：', datetime.datetime.now().year)
print('时间是：', datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
print('当前日期是：', datetime.datetime.now().date())
print('当前年份是：', datetime.datetime.now().time())

#ia = input("输入内容：")
#print(ia, "的ASCII码是：", ord(ia))
#print(id(ia))

a1 = [random.randint(1, 1000) for i in range(20)]
print(a1)


#print('a is:', a, 'b is:', b, 'a*b is:', a*b, file=fp)
#print(chr(66))
