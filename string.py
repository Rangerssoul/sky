# coding:UTF-8
# DATE     ：2018/12/23
# TIME     ：18:24
# FILENAME ：string.py
# IDE      ：PyCharm
# AUTHOR   : puhaiming
# COPYRIGHT：Rangerssoul

# str1 = "安检时，需要检查刀的长度，判断是否超过20厘米"
str1 = "knife_length = int(input())"
# str1 = "Kerchin 科尔沁 筋头巴脑"
l1 = len(str1)
l2 = len(str1.encode('utf-8'))
l3 = len(str1.encode('gbk'))
print(str1)
print(l1, l2, l3)
print("***********")
str2 = str1[:10]
print(str2)
#str3 = str1.split("，")
#print(str3)
print(str1.upper())
print(str1.strip())




