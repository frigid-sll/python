# class Person(object):
#     name='就不会'
#     age=18
#     def __init__(self):
#         pass
# p=Person()
# print(p.name,p.age)
# print('*'*30)
# print(Person.name,Person.age)

# class Person(object):
#     country='中国'
#     def __init__(self):
#         self.name='laowang'
#         self.country='日本'
#         self.age=18
#
# p=Person()
# print(p.name)
# print(p.age)
# print(Person.country)
# print(p.country)    #实例对象剋以访问实例属性
# #print(Person.age)   #类对象不能访问实例属性
# Person.country='美国'
# print(p.country)
# print(Person.country)





class A(object):
    __money=100
    def __init__(self):
        self.name='sll'
    def a(self):
        self.sex='man'
    def b(self):
        print(self.__money)
        self.__money=10
        print(self.__money)
    @classmethod
    def c(cls):
        print(cls.__money)
        cls.__money=200
        print(cls.__money)
    def d(self):
        print(self.__money)
    def e(self):
        print(self.sex)
x=A()
x.a()
print(x.sex)
x.b()
x.c()
x.d()







