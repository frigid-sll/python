# class A(object):
#     def __init__(self):
#         self.num=10
#     def add(self):
#         self.num+=10
# class B(A):
#     pass
# a=B()
# print(a.num)
# a.add()
# print(a.num)

# import os
# os.rename('单继承.py','单继承和多继承.py')

class Master(object):
    def __init__(self):
        self.peifang='古法煎饼果子配方'
    def make_cake(self):
        print('按照%s制作了一份煎饼果子'%self.peifang)

class School(Master):
    def __init__(self):
        self.peifang='现代煎饼果子配方'
    def make_cake(self):
        print('按照%s制作了一份煎饼果子'%self.peifang)
        super(School, self).__init__()
        super(School, self).make_cake()
    def cook(self):
        print('鱼香肉丝')

class Prentice(School):    #多个父类实例方法重名时只继承第一个的方法，不重名的都继承
    def __init__(self):
        self.peifang='猫氏煎饼果子配方'
    def make_cake(self):
        print('按照%s制作了一份煎饼果子'%self.peifang)
    def make_all_cake(self):
        self.make_cake()
        super(Prentice, self).__init__()
        super(Prentice, self).make_cake()

# laoli=Master()
# laoli.make_cake()
damao=Prentice()
damao.make_all_cake()
# damao.make_cake()
# damao.cook()
# print(Prentice.__mro__)     #查看mro顺序表前缀名只能是类名  不能是  对象名！！！
