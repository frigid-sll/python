# import os
# os.rename('堕胎.py','多态.py')


#有继承关系
#子类重写父类同名的属性和方法
#子类调用父类重名的属性和方法

class F1(object):
    def show(self):
        print('F1.show')

class S1(F1):
    def show(self):
        super().show()
        print('S1.show')

class S2(F1):
    def show(self):
        print('S2.show')

s1=S1()
s1.show()
s2=S2()
s2.show()