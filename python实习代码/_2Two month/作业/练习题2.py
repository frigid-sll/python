"""
01--存在my_list = [99,79,89,59,69,49,59,39,29,19,9],分别使用冒泡排序和选择排序给 my_list中的元素排序，并输出最终的排序结果。     
"""
# my_list = [99,79,89,59,69,49,59,39,29,19,9]
# def Bubble_sort(a):
#     for x in range(len(a)-1):
#         for i in range(len(a)-x-1):
#             if a[i]>a[i+1]:
#                 a[i],a[i+1]=a[i+1],a[i]
# def Select_sort(a):
#     for x in range(len(a)-1):
#         minn=x
#         for i in range(x+1,len(a)):
#             if a[minn]>a[i]:
#                 minn=i
#         if minn!=x:
#             a[minn],a[x]=a[x],a[minn]3

# Select_sort(my_list)
# Bubble_sort(my_list)
# print(my_list)





"""
02--键盘录入一个手机号，利用正则表达式判断是否是一个符合要求的手机号
（要求格式：13051115177，号码只能为11位的数字，以1开头，号段为3-9，并不能以4和7结尾）
"""
# import re
# f=re.match('^1[3-9]\d{8}[^47]$','13051115177')
# if f:
#     print(f.group())
# else:
#     print('匹配失败')


"""

03--键盘录入一个字符串，利用正则表达式判断是否是一个sina邮箱（要求格式：hellojiyun@sina.com，邮箱号只能为4-20位的字符，不能以数字（0-9）开头）
"""
# import re
# str=input('请输入一个字符串：')
# f=re.match('^[^\d]\w{3,19}@(sina\.com)$',str)
# if f:
#     print(f.group())
# else:
#     print('匹配失败')


"""
04--存在如下需求，使用进程池完成快速批量创建进程，要求 进程池最大进程数为3，使用for循环，循环演示至少3次批量创建进程，
并完成并行执行输出，注意需要设置主进程阻塞，等待子进程退出。
"""
# import multiprocessing,time
# def func():
#     print('进程池哦')
#     time.sleep(1)
# if __name__ == '__main__':
#     pool=multiprocessing.Pool(3)
#     for x in range(12):
#         pool.apply_async(func)
#     pool.close()
#     pool.join()
#     print('主进程结束')


"""
05--使用线程模块的互斥锁解决多线程间恶意竞争资源的问题，模拟情景存在全局变量num = 0,分别创建执行函数work1和work2，并分别完成对全局变量num的修改，
要求修改一次num值加1，循环修改1000000次，并分别输出最终的num的输出结果。
"""
# import threading,time
# def work1():
#     lock.acquire()
#     global num
#     for x in range(1000000):
#         num+=1
#     print(num)
#     lock.release()
# def work2():
#     lock.acquire()
#     global num
#     for x in range(1000000):
#         num += 1
#     print(num)
#     lock.release()
# if __name__ == '__main__':
#     lock=threading.Lock()
#     num=0
#     f1=threading.Thread(target=work1)
#     f2=threading.Thread(target=work2)
#     f1.start()
#     f2.start()


"""
06--键盘录入一个字符串，利用正则表达式判断是否是一个163邮箱（要求格式：hellojiyun@163.com，邮箱帐号只能为4-20位的字符，以.com结尾）
"""
# import re
# str=input('请输入一个字符串：')
# f=re.match('^\w{4,20}@163(\.com)$',str)
# if f:
#     print(f.group())
# else:
#     print('匹配失败')


"""
07--模拟场景当前有如下函数function(),一日老板突发奇想，想要在实现函数原有功能之前，实现附加验证功能A和B，要求分别实现并给函数添加具有模拟实现附加验证功能A和附加验证功能B的两个装饰器函数，并给function()添加并调用，显示输出效果。
def  function():
Print(“执行程序原有功能”)
"""
# def w1(func):
#     def f():
#         print('验证A')
#         func()
#     return f
#
# def w2(func):
#     def f():
#         print('验证B')
#         func()
#     return f
#
# @w1
# @w2
#
# def function():
#     print('执行程序原有功能')
#
# if __name__ == '__main__':
#     function()


"""
08--使用迭代器实现斐波那契数列的输出，要求输出内容满足如下规律：（0 1 1 2 3 5 8 13 21 34 55...），并要求使用两种方法展示输出效果（在展示输出效果时对数据类型无限制）。
"""
# class Fib(object):
#     def __init__(self,n):
#         self.n=n
#         self.current=0
#         self.num1=0
#         self.num2=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.n>self.current:
#             num=self.num1
#             self.num1,self.num2=self.num2,self.num1+self.num2
#             self.current+=1
#             return num
#         else:
#             raise StopIteration
# f=Fib(10)
# print(list(f))
# f2=Fib(10)
# for x in f2:
#     print(x)



"""
09--使用队列模拟演示进程间通信
"""
# import multiprocessing
# def write(q):
#     for x in range(10):
#         if q.full():
#             print('满啦')
#             break
#         else:
#             print('写了：',x)
#             q.put(x)
#
#
# def read(q):
#     while True:
#         if q.empty():
#             print('没有啦')
#             break
#         else:
#             print('取出：',q.get())
#
#
# if __name__ == '__main__':
#     q=multiprocessing.Queue(5)
#     f1=multiprocessing.Process(target=write,args=(q,))
#     f2=multiprocessing.Process(target=read,args=(q,))
#     f1.start()
#     f1.join()
#     f2.start()



"""
10--借助线程队列模拟演示生产者消费者模式
"""
# import threading,time,queue
# def produce(q):
#     for x in range(6000):
#         lock.acquire()
#         print('生产了:',x)
#         q.put(x)
#         lock.release()
#         time.sleep(0.1)
# def consumer(q):
#     while True:
#         lock.acquire()
#         if q.empty():
#             break
#         else:
#             print('消费了：',q.get())
#             lock.release()
#             time.sleep(0.1)
# if __name__ == '__main__':
#     lock=threading.Lock()
#     q=queue.Queue()
#     f1=threading.Thread(target=produce,args=(q,))
#     f2=threading.Thread(target=consumer,args=(q,))
#     f1.start()
#     time.sleep(0.01)
#     f2.start()


# import queue,threading,timeit
# def produce(q):
#     lock.acquire()
#     q.put(1)
#     lock.release()
# def consumer(q):
#     lock.acquire()
#     print('取出:',q.get())
#     lock.release()
#
# if __name__ == '__main__':
#     lock=threading.Lock()
#     q=queue.Queue()
#     f1=threading.Thread(target=produce,args=(q,))
#     f2=threading.Thread(target=consumer,args=(q,))
#     t=timeit.Timer('f1.start()','from __main__ import f1')
#     t2=timeit.Timer('f2.start()','from __main__ import f2')
#     print(t.timeit(1))
#     print(t2.timeit(1))




# import threading,queue,time
# def produce(q):
#     for x in range(2000000):
#         q.put(x)
#         print('放入:',x)
#         f2 = threading.Thread(target=consumer, args=(q,))
#         f2.start()
#         time.sleep(0.0001)
#
# def consumer(q):
#     print('取出：',q.get())
# if __name__ == '__main__':
#     q=queue.Queue()
#     f1=threading.Thread(target=produce,args=(q,))
#     f1.start()


#
# from greenlet import greenlet
# def produce():
#     for x in range(1000):
#         print('生产了:',x)
#         f2.switch(x)
# def consumer():
#     while True:
#         n=f1.switch()
#         print('消费了:',n)
#
# if __name__ == '__main__':
#     f1=greenlet(produce)
#     f2=greenlet(consumer)
#     f2.switch()

# from greenlet import greenlet
# def work1():
#     f2.switch(1)
#
# def work2():
#     n=f1.switch()
#     print(n)
#
# if __name__ == '__main__':
#     f1=greenlet(work1)
#     f2=greenlet(work2)
#     f2.switch()

# def work1():
#     r=''
#     while True:
#         n=yield r
#         print(n)
# def work2(c):
#     c.send(None)
#     for x in range(100):
#         print('生产：',x)
#         c.send(x)
#
# work2(work1())




# a.func2()()




# def func(x):
#     list=[1,2,3,4,5]
#     lock.acquire()
#     if x>len(list)-1:
#         print('下标越界')
#         lock.release()
#     else:
#         print(list[x])
#         lock.release()
# import threading
# if __name__ == '__main__':
#     lock=threading.Lock()
#     for i in range(10):
#         f = threading.Thread(target=func, args=(i,))
#         f.start()


# class F(object):
#     def __init__(self):
#         pass
#     def a(self,n):
#         if n==0:
#             return 0
#         elif n==1:
#             return 1
#         else:
#             return n*self.a(n-1)
#
# f=F()
# print(f.a(5))

# class F(object):
#     def __init__(self,alist):
#         self.alist=alist
#     def erfen(self,n):
#         if len(self.alist)==0:
#             return False
#         else:
#             x=len(self.alist)//2
#             if self.alist[x]==n:
#                 return True
#             elif n>self.alist[x]:
#                 self.alist=self.alist[x+1:]
#                 return self.erfen(n)
#             else:
#                 self.alist=self.alist[:x]
#                 return self.erfen(n)
# f=F([1,2,3,4,5])
# print(f.erfen(3))
# print(f.erfen(6))

import queue,threading,time,timeit

def i():
    q = queue.Queue()
    def write(q):
        for x in range(100):
            print('写入：', x)
            q.put(x)
            f2 = threading.Thread(target=read, args=(q,))
            f2.start()
            time.sleep(0.05)
    write(q)

def read(q):
    print('取出：',q.get())

if __name__ == '__main__':
    t=timeit.Timer('i()','from __main__ import i')
    print(t.timeit(1))























