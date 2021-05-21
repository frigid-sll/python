# i,name=0,'laowang'
# while i<len(name):
#     print(name[i],end='')
#     i+=1
#
# i2,name2=0,'langwang'
# while i2<len(name2):
#     print(name2[i2],end=' ')
#     i2+=1


# class F(object):
#     def __init__(self,n):
#         self.n=n
#         self.num1=0
#         self.num2=1
#         self.current=0
#     def __next__(self):
#         if self.current<self.n:
#             num,self.num1,self.num2,self.current=self.num1,self.num2,self.num1+self.num2,self.current+1
#             return num
#         else:
#             raise StopIteration
#     def __iter__(self):
#         return self
# for x in F(5):
#     print(x,end=' ')
#
# print()
#
# def f(n):
#     num1,num2=0,1
#     for x in range(n):
#         num,num1,num2=num1,num2,num1+num2
#         yield num
# for x in f(5):
#     print(x,end=' ')


# def w(n):
#     print(1)
#     def f1():
#         print(2)
#         n()
#     return f1
# def w2(n):
#     print(3)
#     def f2():
#         print(4)
#     return f2
# @w
# @w2
# def s():
#     print(2)
#
# s()

# import timeit
# def t():
# 	for x in range(1001):
# 		for y in range(1001):
# 			z=1000-x-y
# 			if x**2+y**2==z**2:
# 				print(x,y,z)
#
# if __name__=='__main__':
# 	time66=timeit.Timer('t()','from __main__ import t')
# 	timer=time66.timeit(10)    #10表示要执行这个函数的次数
# 	print(timer)		#timer表示执行十次所需要的时间


def f1():
	l=list(range(1000))

def f2():
	l=[]
	for x in range(1000):
		l.append(x)

def f3():
	l=[x for x in range(1000)]

def f4():
	l=[]
	for x in range(1000):
		l=l+[x]

import timeit
if __name__ == '__main__':
	timer1=timeit.Timer('f1()','from __main__ import f1')
	t1=timer1.timeit(1000)
	print(t1)
	timer2=timeit.Timer('f2()','from __main__ import f2')
	t2=timer2.timeit(1000)
	print(t2)
	timer3=timeit.Timer('f3()','from __main__ import f3')
	t3=timer1.timeit(1000)
	print(t3)
	timer4=timeit.Timer('f4()','from __main__ import f4')
	t4=timer1.timeit(1000)
	print(t4)




