
def w(func):
    print('装饰的函数')
    func(1,2)
    return 1

@w
def inside(a,b):
    print('被装饰的函数')
    print(a,b)
    return 2

inside
# s=inside
# print(s)

# def bracket(data):
#     return data
#
#
# if __name__ == '__main__':
#     # 不带括号调用的结果：<function bracket at 0x0000000004DD0B38>,a是整个函数体，是一个函数对象，不须等该函数执行完成
#     a = bracket
#     print(a)
#     # 带括号调用的结果：6 ,b是函数执行后返回的值6,须等该函数执行完成的结果
#     b = bracket(6)
#     print(b)




# def w1(func):
#     def inner():
#         print('--验证权限---')
#         func()   #这里是执行f1()函数
#     print('123')
#     return inner
#
# @w1    #相当于f1=wi(f1())
# def f1():
#     print('f1 called')
#
# # @w1
# # def f2():
# #     print('调用了该函数')
#
# f1()
# f2()

# 可变类型和不可变类型：
# 可变类型：列表，字典，集合
# 不可变类型：数字，字符串，元祖
#可变类型 两个变量同时赋值给一个时，修改了一个另一个也变了
#不可变类型：两个变量同时赋值给一个时，修改了一个另一个不变

# a,b=1,'啊'
# print(a,':',b)

# def func(*args):
#     def inner():
#         print(123456)
#     return inner
# func(1)()
# func()()
# func(1,2,3)()

'''闭包函数'''
# def f(a):
#     def f2(b):
#         return a+b
#     return f2
# print(f(1)(2))

# def w1(func):
# 	print('123')
# 	def inner():
# 		print('---1---')
# 		func()
# 	return inner
# @w1    #相当于f=w1(f)
# def fi():
# 	print('555')
# fi()

# def w1(func):
# 	print('123')
# 	def s():
# 		print('lalala')
# 	return s
# @w1    #相当于f1=w1(f1)
# def f1():
# 	print('555')



# def w1(func):
# 	print('123')
# 	def s():
# 		print('lalala')
# 	return s
# @w1    #相当于f1=w1(f1)
# def f1():
# 	print('555')
# f1()

#
# def w1(func):
# 	def inner():
# 		print('---1---')
# 		func()   #这里执行的是f1()函数
# 	print('123')
# 	return inner
# @w1    			#相当于f=w1(f)
# def f():
# 	print('555')
# f()
#
# '''
# 结果为：
# 123
# ---1---
# 555
# '''
#
# def func(a):
#     print('123')
#     def f(b):
#         print('--权限认证--',b)
#         a()
#     return f
# @func    #f2=func(f2)
# def f2():
#     print('lalala')
# f2(1)

# import os
# os.rename('修饰器.py','装饰器.py')

# def w(n):
#     def q(a,b):
#         print(a)
#         n(a)
#     return q
# @w
# def f(a):
#     print(2)
# f(1,2)

#当给装饰器有传参的时候，传的虽然是给装饰器的子函数传的参数，但也可以给调用函数传参，但传参名要一样，并且调用函数的参数个数要小于等于装饰器的子函数的传参个数，都有的形参名要相等 不然会报错


# def w(f):
# 	def a():
# 		print('a的函数')
# 		f()
# 	return a
# # @w 			#a1=w(a1)
# def a1():
# 	print('a1函数')
# @w			#a2=w(a2)
# def a2():
# 	a1()
# 	print('a2的函数')
# a2()


# def ooo(a):
#     print("1")
#     def qqq():
#         print("2")
#         a()    #执行rrr函数
#     return qqq
#
#
# def www(a):
#     print("3")
#     def rrr():
#         print("4")
#         a()    #执行pop函数
#     return rrr
#
# @ooo    #pop->相当于www(pop)->相当于rrr=ooo(pop->相当于www(pop)->相当于rrr)       执行ooo函数
# @www    #pop=www(pop)
#
# def ppp():
#     print("5")
#
# ppp()   #执行www()函数


# def w(func):
#     def f1():
#         print('01-----开始')
#         func()
#         print('01----结束')
#     return f1
# def w2(func):
#     def f2():
#         print('02-----开始')
#         func()
#         print('02----结束')
#     return f2
# @w
# @w2
# def f3():
#     print('修复漏洞')
# f3()




# def zhs(func):
#     print("第一个装饰器")
#     def haha():
#         print("1开始")
#         func()
#         print("1结束")
#     return haha
# def zhs1(func):
#     print("第二个装饰器")
#     def haha():
#         print("2开始")
#         func()
#         print("2结束")
#     return haha
# @zhs  # xixi = zhs(xixi)
# @zhs1
# def xixi():
#     print("我是嘻嘻")
#
# if __name__ == '__main__':
#     xixi()





