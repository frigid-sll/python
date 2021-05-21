# class Hero(object):  # 新式类定义形式
#     """info 是一个实例方法，类对象可以调用实例方法，实例方法的第一个参数一定是self"""
#     def info(self):
#         """当对象调用实例方法时，Python会自动将对象本身的引用做为参数，
#             传递到实例方法的第一个参数self里"""
#         print(self)
#         print("self各不同，对象是出处。")
#
# # Hero这个类 实例化了一个对象  taidamier(泰达米尔)
# taidamier = Hero()
# # 对象调用实例方法info()，执行info()里的代码
# # . 表示选择属性或者方法
# taidamier.info()
# print(taidamier)  # 打印对象，则默认打印对象在内存的地址，结果等同于info里的print(self)
# print(id(taidamier))  # id(taidamier) 则是内存地址的十进制形式表示

# class lei(object):
#     def __init__(self,age):
#         self.name='师玲珑'
#         self.age=age
#     def __del__(self):
#         print('删除')
#     def add(self,sex):
#         self.sex=sex
#     def shu(self):
#         print(self.name,self.age,self.sex)
#     def __str__(self):
#         return self.name
# xiang=lei(18)
# del(xiang)
# print(xiang)
# print(xiang.__doc__)
# xiang.add('男')
# xiang.shu()
# print(xiang.sex,xiang.age)

# class Hero(object):
#     def __init__(self,name):
#         print('_init_方法被调用')
#         self.name=name
#     def shu(self):
#         print('123')
#     def __del__(self):
#         print('_del_方法被调用')
#         print("%s被干掉了..."%self.name)
# taidamier=Hero('泰达米尔')
# del self.name
# q=taidamier
# w=taidamier
# print('%d被删除1次'%id(taidamier))
# del(taidamier)
# q.shu()
# print('='*20)

# class Teacher(object):
#     __money=1
#     age=18
#     def __init__(self):
#         self.a=1
#     def study(self):
#         print('学习的方法')
#         self.age=2
#         print(self.__money,self.age)
#     def earn(self):
#         print('挣钱的方法')
#     @classmethod
#     def gai(cls):
#         cls.age=2
#         print(cls.__money)
#     def z(self):
#         self.n=2
#     def chu(self):
#         print(self.n)
# class Student(Teacher):
#     def __init__(self):
#         self.a=2
#     def earn(self):
#         '''12356'''
#         print('挣钱的方法2')
#     def q(self):
#         Teacher.earn(self)
#     def w(self):
#         Teacher.__init__(self)
#         print(self.a)
# student=Student()
# student.gai()
# print(Student.age)
# student.q()
# student.w()
# student.z()
# student.chu()
# print(student.earn())
# print(student.n)

# class Teacher(object):
#     __money=1
#     def __init__(self):
#         self.a=1
#     def study(self):
#         print('学习的方法')
#     def earn(self):
#         print('挣钱的方法')
#     @classmethod
#     def gai(cls):
#         cls.__money=2
#         print(cls.__money)
# class Student(Teacher):
#     def __init__(self):
#         self.a=2
#     def earn(self):
#         print('挣钱的方法2')
#     def q(self):
#         Teacher.earn(self)
#     def w(self):
#         Teacher.__init__(self)
#         print(self.a)
# student=Student()
# student.q()
# student.w()

# class Lol(object):
#     def __init__(self,hp):
#         self.hp=hp
#         self.fyl=50
#     def shu(self):
#         print(self.hp)
#     def dizhi(self):
#         print(id(self.fyl))
#     def dizhi2(self):
#         print(id(self.hp))
# jie=Lol(100)
# anqila=Lol(200)
# jie.dizhi()
# anqila.dizhi()
# jie.dizhi2()
# anqila.dizhi2()