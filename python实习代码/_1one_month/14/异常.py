# def func1():
#      print('1')
#      print(num)
#      print('2')
#
# def func2():
#      print('2-1')
#      func1()
#      print('2-2')
#
# def func3():
#      try:
#           print('3-1')
#           func1()
#           print('3-2')
#      except Exception as result:
#           print('有错误')
#      print('3-2')
#
# func3()

# class ShortInputException(Exception):
#     '''自定义的异常类'''
#     def __init__(self, length, atleast):
#         #super().__init__()
#         self.length = length
#         self.atleast = atleast
#
# def main():
#     try:
#         s = input('请输入 --> ')
#         if len(s) < 3:
#             # raise引发一个你定义的异常
#             raise ShortInputException(len(s), 3)
#     except ShortInputException as result:#x这个变量被绑定到了错误的实例
#         print('ShortInputException: 输入的长度是 %d,长度至少应是 %d'% (result.length, result.atleast))
#     else:
#         print('没有异常发生.')

# main()



# list1=[1,2,3,4,5]
# list2=[]
# for x in list1:
#     list2.append(x)
# for x in range(len(list1)):
#     if x%2==0:
#         if x==len(list1)-1:
#             pass
#         else:
#             list1[x]=list2[x+1]
#     else:
#         list1[x]=list2[x-1]
# print(list1)

# class yichang(Exception):
#     def __init__(self,length,atleast):
#         self.length=length
#         self.atleast=atleast
#
# a=int(input("请输入："))
# try:
#     if a<30:
#         raise yichang(a,30)
# except yichang as result:
#     print('你输入的数为%d,至少应该为%s'%(result.length,result.atleast))
# else:
#     print('没有异常发生')

# class error(Exception):
#     def __init__(self,IDD,minn,maxx):
#         self.IDD=IDD
#         self.minn=minn
#         self.maxx=maxx
# def new():
#     ID=input("请输入你要注册的账号：")
#     try:
#         if len(ID)<8 or len(ID)>11:
#             raise error(len(ID),8,11)
#     except error as result:
#         print('你输入的账号长度为%d,注册的账号范围为%d位-%d位'%(result.IDD,result.minn,result.maxx))
#     else:
#         print('注册成功')
#
# new()


# class a(object):
#     w=0
#     def __init__(self,age):
#         self.age=age
#     def b(self):
#         print(self)
#     def __new__(cls, age):
#         if cls.w==0:
#             cls.w=object.__new__(cls)
#         return cls.w
# c=a(1)
# c.b()
# print(c.age)
# d=a(1)
# d.b()

# try:
#     print(o)
# except Exception as result:
#     print('有错误')
#     print(result)
# finally:
#     print('你是个大傻瓜')

# class error(Exception):
#     def __init__(self,year):
#         self.year=year
# year=int(input("请输入年份："))
# try:
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         print('%d是闰年'%year)
#     else:
#         raise error(year)
# except Exception as s:
#     print("你输入的年份%d不是闰年"%s.year)

# import os,time

# print('\n'.join(['*'*x for x in range(5,0,-1)]))

# class error(Exception):
#     def __init__(self,age,age2):
#         self.age=age
#         self.age2=age2
# s=int(input("请输入你的年龄："))
# try:
#     if s < 18:
#         raise error(s, 18)
# except error as result:
#     print('你的年龄是%d岁,不足%d岁'%(result.age,result.age2))
# else:
#     print('已满%d岁'%s)

class hot(object):
    def __init__(self):
        self.time=0
        self.tiao=[]
        self.cond=''
    def hottime(self,n):
        self.time+=n
        if self.time>8:
            self.cond='焦的'
        elif self.time>5:
            self.cond='熟的'
        elif self.time>3:
            self.cond='半生不熟的'
        else:
            self.cond='生的'
    def add(self,liao):
        self.tiao.append(liao)
        name=self.cond+'地瓜'+'('
        for z,x in enumerate(self.tiao):
            if z==len(self.tiao)-1:
                name=name+x
            else:
                name=name+x+','
        name=name+')'
        print(name)
h=hot()
h.hottime(1)
h.add('番茄味')
h.hottime(5)
h.add('咸的')

# str='I am a student'
# list=str.split(" ")
# a=''
# for x in list:
#     if len(a)<len(x):
#         a=x
# print(a)