"""
@Time:     2020/4/12 21:19
@Author:   Scott Mark
@File:     class_test2.py
@Software: PyCharm
"""


# -*- coding: utf-8 -*-


# 定义父类(基类/超类) Animal
class Animal(object):
    def run(self):
        print('Animal is running...')


# 定义子类 Dog
class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')


def run_twice(animal):
    animal.run()
    animal.run()


# 继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，
# 子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。
# 动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。
run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
run_twice(Tortoise())

# 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：
