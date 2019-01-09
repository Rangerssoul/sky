# coding:UTF-8
# DATE     ：2018/12/23
# TIME     ：17:01
# FILENAME ：tmp.py
# IDE      ：PyCharm
# AUTHOR   : puhaiming
# COPYRIGHT：Rangerssoul

for i in range(1, 10, 2):
    print(i)

str1 = "只能提供七位有效数字"
print(str1)

for i in str1:
    print(i)


d_name = {'罗纳尔多':'外星人', '博格坎普':'冰王子', '贝肯鲍尔':'足球皇帝', '克林斯曼':'金色轰炸机', '贝隆':'巫师', '伊卡尔迪':'二弟'}

name = "罗纳尔多"
if name in d_name.keys():
    print(d_name.get(name,'查询无结果'))


