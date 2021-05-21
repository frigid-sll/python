class F(object):
    __money=1
    n=333
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.sex='男性'
    def classid(self):
        return '1809A'
    @classmethod
    def secret(cls):
        return cls.__money
    @classmethod
    def change(cls):
        cls.__money=10

class F2(F):
    __money = 2
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.sex='女性'
    def classid(self):
        return '1809B'
    def father(self):
        print(self.classid())
        print(super().classid())
        print(self.name)
        F.__init__(self,'张三',18)
        print(self.name)

    @classmethod
    def secret(cls):
        return cls.__money
    @classmethod
    def change(cls):
        cls.__money=20

class F3(F2):
    __money = 3
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.sex='中性'
    def classid(self):
        return '1811A'
    @classmethod
    def secret(cls):
        return cls.__money
    @classmethod
    def change(cls):
        cls.__money=30

f=F('张三',18)
f2=F2('李四',20)
f3=F3('王五',16)

print(f.n)

# f2.father()
# print(f2.secret())
# print(F3.__mro__)


# class Person(object):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def show_my_info(self):
#         print("我是%s,今年%d岁"%(self.name,self.age))
#     def show_my_birth(self):
#         self.year=2018-self.age
#         print("我是%d年出生，今年%d岁"%(self.year,self.age))
#     def show_my_life(self):
#         for x in range(self.age+1):
#             if x==0:
#                 print("%d年出生"%(2018-self.age))
#             else:
#                 print("%d年%d岁"%((2018-self.age+x),x))
#     def show_leap_year(self):
#         self.list=[]
#         for x in range(self.age+1):
#             self.y=2018-x
#             if self.y%4==0 and self.y%100!=0 or self.y%400==0:
#                 self.list.append(self.y)
#         if self.list==[]:
#             print("没有闰年")
#         else:
#             print(self.list[::-1])
#             print('\t'.join([str(x) for x in self.list]))
#     def can_recite(self):
#         for x in range(1,10):
#             for y in range(1,x+1):
#                 print("%d*%d=%d"%(x,y,x*y),end=' ')
#             print()
# name=input("请输入姓名：")
# age=int(input("请输入年龄："))
# p=Person(name,age)
# p.show_my_info()
# p.show_my_birth()
# p.show_my_life()
# p.show_leap_year()
# p.can_recite()



# class cirlc(object):
#     def __init__(self,r):
#         self.r=r
#     def c(self):
#         print("周长为%.1f"%(2*self.r*3.14))
#     def s(self):
#         print("面积为%.2f"%(3.14*self.r*self.r))
#
# r=int(input("请输入半径:"))
# c=cirlc(r)
# c.c()
# c.s()










