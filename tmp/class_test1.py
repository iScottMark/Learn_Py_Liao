"""
@Time:     2020/4/12 20:43
@Author:   Scott Mark
@File:     class_test1.py
@Software: PyCharm
"""
# -*- coding: utf-8 -*-


# 面向对象编程 - 访问限制
class Student(object):

    # 定义数据，且self.__xx的写法使得外部无法访问内部数据
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    # 定义一种操作数据的方法
    def print_score(self):
        print('{:s}: {:.1f}'.format(self.__name, self.__score))

    # 外部无法访问数据，我们可以定义获取数据的操作方法
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    # 同时还可以定义让外部允许对score修改的方法，同时还可以通过逻辑判断等方法，避免无效参数传入
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('Bad Score')


# 测试一下编写好的 Student 对象
Mark = Student('Mark', 95)
Mark.print_score()
Mark.set_score(100)
Mark.print_score()
print(type(Mark))
