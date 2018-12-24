# coding:UTF-8
# DATE     ：2018/12/23
# TIME     ：12:16
# FILENAME ：list_test.py
# IDE      ：PyCharm
# AUTHOR   : puhaiming
# COPYRIGHT：Rangerssoul

import random

gname = ["文明三", "warframe", "ghost", "辐射4", "黑魂3", "Witcher 3",
         "刺客信条4", "GTA V", "Heart's Medicine", "上古卷轴 5", "街霸4"]
ename = ["Chrome", "Firefox", "EDGE", "遨游", "IE"]
nname = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 序列测试
'''
print(gname)
print(gname[0])
print(gname[-1])
print(gname[:])
print(gname[0:11])
print(gname[0:11:3])

print(num)
print(num[0:3])     # 包括左边，不包括右边
print(num[1:])
print(num[-4:-1])   # 包括左边，不包括右边
print(num[:-1])

print(gname+ename)
print(gname+nname)
print(gname+num)

print(7 in num)
print("warframe" in gname)
print("王者" in gname)

print(len(gname))
print(max(gname))
print(len(nname))
print(max(nname), min(nname))
print(len(num))
print(max(num), min(num))

print(list(gname))
'''

# 列表测试
list_gname = list(gname)
list_num = [5, 0, -23, 89, 2134, 11]
list_lan = ['C', 'java', 'C++', 'python', 'vb']
list_all =[87,'98', "test", '列表', ["汽车", "火车", "飞机", "ship"]]
list_gen = list(range(1, 100, 4))

print(list_gname)
print(list_num)
print(list_lan)
print(list_all)
print(list_gen)
print(list_all[-1])

for index,item in enumerate(list_all):
    print(index,item)

print(len(list_lan))
list_lan.extend(list_num)
list_lan.insert(3,"insert")
list_lan.remove("vb")
print(len(list_lan))
print(list_lan)
print(list_lan.pop())
print(list_lan.index("insert"))
print(sum(list_num))


a1 = [random.randint(1, 1000) for i in range(20)]
print(a1)
a2 = [i*0.5 for i in a1]
print(a2)
a3 = [i*0.5 for i in a1 if i > 300]
print(a3)

print(list_lan)
print(list_lan.pop(-2))
print(list_lan)




s1 = [58, 12945, 391, 357, 728, 116, 21086]
a1 = [(i/sum(s1)) for i in s1]

s1.sort(reverse=True)
print(s1)
print(a1)