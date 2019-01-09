# coding:UTF-8
# DATE: 2019/1/7
# TIME: 12:43
# IDE : PyCharm
# NAME: func.py
# AUTHOR: Puhaiming
# COPYRIGHT: Rangerssoul

def filchar(string):
    '''
    过滤字符串
    test
    '''
    import re
    fil_char = r'(黑客)|(方案)|(协议)|(报告)'
    sub = re.sub(fil_char, '@_@', string)
    print(sub)


# astring = "金融服务方案"
# filchar(astring)


def bmi_func(name=None, weight=None, height=None):
    if (name==None or weight==None or height==None):
        print("输入参数有误")
        return

    bmi = weight/(height*height)
    print(name+"的BMI是："+str(bmi))

#bmi_func("张三",65,1.68)
#bmi_func("张三",height=1.68)

d_name = {'罗纳尔多':'外星人', '博格坎普':'冰王子', '贝肯鲍尔':'足球皇帝', '克林斯曼':'金色轰炸机', '贝隆':'巫师', '伊卡尔迪':'二弟'}

def soccerstar(**name):
    print()
    for key,value in name.items():
        print("["+key+"]"+"的外号是："+value)

#soccerstar(**d_name)

def starcheck(**name):
    print()
    t_name = input('请输入名字:')
    check_result = name.get(t_name)
    if check_result != None:
        print(check_result)
    else:
        print("查询无结果")

#starcheck(**d_name)

