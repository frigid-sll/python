# 生成器
# def fib(n):
#     current=0
#     num1,num2=0,1
#     for x in range(n):
#         num=num1
#         num1,num2=num2,num1+num2
#         yield num
# F=fib(5)
# print(next(F))
# try:
#      for x in F:
#         print(x)
# except Exception as a:
#       print(a)

# def sheng(n):
#     num1=0
#     num2=1
#     for x in range(n):
#         num=num1
#         num1,num2=num2,num1+num2
#         yield num
# f=sheng(5)
# for x in f:
#     print(x)

#迭代器

# class F(object):
#     def __init__(self,n):
#         self.n=n
#         self.num1=0
#         self.num2=1
#         self.current=0
#     def __next__(self):
#         if self.current<self.n:
#             num=self.num1
#             self.num1,self.num2=self.num2,self.num1+self.num2
#             self.current+=1
#             return num
#         else:
#             raise StopIteration
#     def __iter__(self):
#         return self
# f=F(5)
# for x in f:
#     print(x)

# class F(object):
#     def __init__(self,n):
#         self.n=n
#         self.current=0
#         self.num1=0
#         self.num2=1
#     def __next__(self):
#         if self.current<self.n:
#             num=self.num1
#             self.num1,self.num2=self.num2,self.num1+self.num2
#             self.current+=1
#             return num
#         else:
#             raise StopIteration
#     def __iter__(self):
#         return self
# f=F(5)
# for x in f:
#     print(x)

# from collections import Iterable
# print(isinstance([1,2],Iterable))

# class func(object):
#     def __init__(self):
#         self.list=[]
#         self.n=0
#     def add(self,item):
#         self.list.append(item)
#     def __next__(self):
#         if self.n<len(self.list):
#             self.n+=1
#             return self.list[self.n-1]
#         else:
#             raise StopIteration
#     def __iter__(self):
#         return self
# f=func()
# f.add(1)
# f.add(2)
# f.add(3)
# from collections import Iterable,Iterator
# print(isinstance(f,Iterable))
# for x in f:
#     print(x)

# list=[1,2,3]
# f=iter(list)
# print(next(f))    #1
# print(next(f))    #2
# print(next(f))    #3
# print(next(f))    #报错

# from collections import Iterable,Iterator
# print(isinstance([],Iterable))
# print(isinstance([],Iterator))
# print(isinstance(iter([]),Iterator))

# def func(s):
#     for x in range(len(s)):
#         yield s[x]
# s=[1,2,3,4]
# f=func(s)
# for x in f:
#     print(x)

# class func(object):
#     def __init__(self,n):
#         self.n=n
#         self.current=0
#     def __next__(self):
#         if self.current<len(self.n):
#             self.current+=1
#             return self.n[self.current-1]
#         else:
#             raise StopIteration
#     def __iter__(self):
#         return self
# s=[1,2,3,4]
# f=func(s)
# for x in f:
#     print(x)

# class func1(object):
#     def __init__(self):
#         self.item=[]
#     def add(self,a):
#         self.item.append(a)
#     def __iter__(self):
#         f=F(self)
#         return f
# class F(object):
#     def __init__(self,list):
#         self.current=0
#         self.list=list
#     def __next__(self):
#         if self.current<len(self.list.item):
#             i=self.list.item[self.current]
#             self.current+=1
#             return i
#         else:
#             raise StopIteration
#     def __iter__(self):
#         return self
# s=func1()
# s.add(1)
# s.add(2)
# s.add(3)
# for x in s:
#     print(x)

# a=[1,2,3,45]
# q=iter(a)
# for x in q:
#     print(x)

# class f1(object):
#     def __init__(self):
#         self.item=[]
#     def add(self,a):
#         self.item.append(a)
#     def __iter__(self):
#         f2=F(self)
#         return f2
# class F(object):
#     def __init__(self,f):
#         self.f=f
#         self.current=0
#     def __next__(self):
#         if self.current<len(self.f.item):
#             s=self.f.item[self.current]
#             self.current+=1
#             return s
#         else:
#             raise StopIteration
#     def __iter__(self):
#         return self
# w=f1()
# w.add(1)
# w.add(2)
# w.add(3)
# for x in w:
#     print(x)

# class F1(object):        #定义一个可迭代对象的类
#     def __init__(self):
#         self.list=[]
#     def add(self,a):
#         self.list.append(a)
#     def __iter__(self):
#         iterator=F2(self)
#         return iterator     #返回一个迭代器  是下面的那个类，向这个提供了_next_
# class F2(object):     #定义一个迭代器的类
#     def __init__(self,f):
#         self.f=f
#         self.current=0
#     def __next__(self):
#         if self.current<len(self.f.list):
#             s=self.f.list[self.current]
#             self.current+=1
#             return s
#         else:
#             raise StopIteration
#     def __iter__(self):
#         return self
# f=F1()
# f.add(1)
# f.add(2)
# for x in f:
#     print(x)


# class F1(object):
#     def __init__(self,n):
#         self.n=n
#         self.list=[]
#     def __iter__(self):
#         f=F2(self)
#         return f
# class F2(object):
#     def __init__(self,q):
#         self.q=q
#         self.current=0
#         self.num1=0
#         self.num2=1
#     def __next__(self):
#         if self.current<self.q.n:
#             num=self.num1
#             self.num1,self.num2=self.num2,self.num1+self.num2
#             self.current+=1
#             return num
#         else:
#             raise StopIteration
#     def __iter__(self):
#         return self
# f=F1(5)
# for x in f:
#     print(x)


# class F(object):
#     def __init__(self,n):
#         self.n=n
#         self.current=0
#         self.num1=0
#         self.num2=1
#     def __next__(self):
#         if self.current<self.n:
#             num=self.num1
#             self.num1,self.num2=self.num2,self.num1+self.num2
#             self.current+=1
#             return num
#         else:
#             raise StopIteration
#     def __iter__(self):
#         return self
#
# f=F(5)
# for x in f:
#     print(x)


def f(n):
    num1,num2=0,1
    for x in range(n):
        num,num1,num2=num1,num2,num1+num2
        yield num
for x in f(5):
    print(x)

# f=[x for x in range(3)]
# print(f)
#
# f2=(x for x in range(3))
# print(f2)   #返回的是一个生成器
#
# for x in f2:
#     print(x)

# def q(n):
#     num1,num2=0,1
#     for x in range(n):
#         num,num1,num2=num1,num2,num1+num2
#         yield num
# f=q(5)
# for x in f:
#     print(x)

# from collections import Iterable,Iterator
# from collections import Iterable,Iterator
# from collections import Iterable,Iterator


