# coding:UTF-8
# DATE: 2019/1/8
# TIME: 13:00
# IDE : PyCharm
# NAME: class.py
# AUTHOR: Puhaiming
# COPYRIGHT: Rangerssoul
class Fruit:
    def __init__(self, color="green"):
        Fruit.color = color
    def harvest(self):
        print("水果原来是："+Fruit.color)

class Apple(Fruit):
    def __init__(self):
        print("i am apple")
        super(Apple, self).__init__()

apple = Apple()
apple.harvest()


class trans_list:
    def __init__(self):
        print("\nclass trans_list begin:\n")
