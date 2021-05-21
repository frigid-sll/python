"""
1、功能描述：
  使用代码定义一个数组，
  并且用选择排序方法对数组就行排序，
  正序或者倒序用参数来控制，
  用自己的语言将整个排序过程进行注释（20分）
"""
# a=[1,3,2,5,4]
# for x in range(len(a)-1):
#     minn=x
#     for i in range(x+1,len(a)):
#         if a[minn]>a[i]:
#             minn=i
#     if minn!=x:
#         a[minn],a[x]=a[x],a[minn]
# print(a)



"""
2、功能描述：（10分）
自定义一个迭代器，并且重写iter()和next()方法，
对一个数组进行迭代
"""
# class F(object):
#     def __init__(self,n):
#         self.n=n
#         self.current=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.current < len(self.n):
#             num = self.n[self.current]
#             self.current += 1
#             return num
#         else:
#             raise StopIteration
# a=[1,2,3,4,5]
# f=F(a)
# for x in f:
#     print(x)

"""
3、功能描述：（10分）

使用代码定义装饰器函数嵌套，并用语言描述执行细节
要求（按完成的功能量给与相应条件的分数，未实现该条件功能效果不给分）：
1)正确使用装饰器引用
2)正确使用函数嵌套的逻辑
3)正确用注释语言描述整个过程，并且没有遗漏
"""

# def w(func):
#     def f():
#         print('装饰器...')
#         func()
#     return f
#
# @w
# def x():
#     print('被装饰的函数...')
#
# if __name__ == '__main__':
#     x()

"""
4、使用filter过滤器和lambda表达式得到1-20之间能被2整除的数（10分）
"""
# print(list(filter(lambda x:x%2==0,[x for x in range(1,21)])))

"""
5、功能描述：（10分）

请用生成器实现斐波那契数列（长度小于20）

要求（按完成的功能量给与相应条件的分数，未实现该条件功能效果不给分）：
1)正确使用yield关键字
2)正确用代码实现斐波那契逻辑（两值相加等于第三）
正确打印出斐波那契数列，列表元素个数小于20

"""

# def Fib(n):
#     num1,num2=0,1
#     for x in range(n):
#         num,num1,num2=num1,num2,num1+num2
#         yield num
# f=Fib(5)
# for x in f:
#     print(x)


"""
6、定义函数，使用isinstance方法判断列表、元组、数字、集合、字符串、字典中的可迭代对象（10分）

要求（按完成的功能量给与相应条件的分数，未实现该条件功能效果不给分）：
1) 正确引入isinstance需要导入的python库
2) 正确用代码判断并且打印方法返回的对象
3) 正确判断所有对象的返回值，并无遗漏

"""
# from collections import Iterable
# def pan():
#     a=isinstance([1,2,3],Iterable)
#     b=isinstance((1,2,3),Iterable)
#     c=isinstance(1,Iterable)
#     d=isinstance({1,2,3},Iterable)
#     e=isinstance('asd',Iterable)
#     f=isinstance({'name':1},Iterable)
#     return a,b,c,d,e,f
# print(pan())

"""
7、使用迭代器实现一个斐波那契数列（10分）
"""
# class F(object):
#     def __init__(self,n):
#         self.n=n
#         self.num1=0
#         self.num2=1
#         self.current=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.current<self.n:
#             num=self.num1
#             self.num1,self.num2=self.num2,self.num1+self.num2
#             self.current+=1
#             return num
#         else:
#             raise StopIteration
#
# f=F(5)
# for x in f:
#     print(x)

"""
8、自定义列表使用冒泡排序对该无序列表排序（20分）
"""
# a=[1,3,2,5,4]
# for x in range(len(a)-1):
#     for i in range(len(a)-1-x):
#         if a[i]>a[i+1]:
#             a[i],a[i+1]=a[i+1],a[i]
# print(a)

"""
9、功能描述：（10分）
给定两个列表，list1 = [[3,2,63],100],list2 =[(1,2),[“I”,”love”,”woman”]],
分别对两个列表完成浅拷贝、深拷贝操作，并描述最外层和里面的列表元素发生什么样变化。
要求（按完成的功能量给与相应条件的分数，未实现该条件功能效果不给分）：
1)实现浅拷贝操作
2)实现深拷贝操作
3)成功描述最外层和里面的元素具体发生了什么变化
"""



"""
10、功能描述：（10分）

请用代码实现变量名解析LEGB原则，并用语言描述清楚
要求（按完成的功能量给与相应条件的分数，未实现该条件功能效果不给分）：
1) 正确用代码声明全局变量
2) 正确用代码声明嵌套作用域以及局部作用域
3) 正确用注释语言描述清晰
"""




"""
11、分别使用常规方法和递归函数两种方法，
在有序序列alist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
中搜索8和88两个元素。(20分)
"""
alist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
'''递归'''
# def cha(a,item):
#     if len(a)==0:
#         return False
#     else:
#         x=len(a)//2
#         if a[x]==item:
#             return True
#         elif item>a[x]:
#             return cha(a[x+1:],item)
#         else:
#             return cha(a[:x],item)
# print(cha(alist,8))
# print(cha(alist,88))
'''常规'''
# def cha2(a,item):
#     first=0
#     last=len(a)-1
#     while first<=last:
#         x=(first+last)//2
#         if item==a[x]:
#             return True
#         elif item>a[x]:
#             first=x+1
#         else:
#             last=x-1
#     return False
#
# print(cha2(alist,8))
# print(cha2(alist,88))


"""
12、使用递归实现0--100和，偶数和，奇数和（30分）
"""
'''0-100的和'''
# def sum1(n):
#     if n==0:
#         return 0
#     else:
#         return sum1(n-1)+n
#
# print(sum1(100))

'''偶数和'''
# def sum2(n):
#     if n==0:
#         return 0
#     else:
#         if n%2==0:
#             return n+sum2(n-2)
#         else:
#             return sum2(n-1)
# print(sum2(100))

'''奇数和'''
# def sum3(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         if n%2==1:
#             return n+sum3(n-2)
#         else:
#             return sum3(n-1)
# print(sum3(100))

"""
13.构造一个栈，模拟实现以下方法：（10分）

Stack() 创建一个新的空栈
push(item) 添加一个新的元素item到栈顶
pop() 弹出栈顶元素
peek() 返回栈顶元素
is_empty() 判断栈是否为空
size() 返回栈的元素个数
"""
# class Stack(object):
#     def __init__(self):
#         self.stack=[]
#
#     def push(self,item):
#         self.stack.append(item)
#
#     def pop(self):
#         return self.stack.pop()
#
#     def peek(self):
#         return self.stack[-1]
#
#     def is_empty(self):
#         if len(self.stack)==0:
#             return True
#         else:
#             return False
#
#     def size(self):
#         return len(self.stack)
#
# f=Stack()
# f.push(1)
# f.push(2)
# print(f.pop())
# print(f.size())


"""
14.构造一个队列，模拟实现以下功能：（10分）
Queue() 创建一个空的队列
enqueue(item) 往队列中添加一个item元素
dequeue() 从队列头部删除一个元素
is_empty() 判断一个队列是否为空
size() 返回队列的大小
"""
# class Queue(object):
#     def __init__(self):
#         self.queue=[]
#
#     def enqueue(self,item):
#         self.queue.append(item)
#
#     def dequeue(self):
#         return self.queue.pop(0)
#
#     def is_empty(self):
#         if len(self.queue)==0:
#             return True
#         else:
#             return False
#
#     def size(self):
#         return len(self.queue)
#
# f=Queue()
# f.enqueue(1)
# f.enqueue(2)
# print(f.size())
# f.dequeue()
# print(f.size())



"""
15.请用多任务思想完成对变量g_num各完成100次相加的操作
要求：主线程须等待子线程执行完成后退出
"""
# import threading
# def work1():
#     global g_num
#     for x in range(100):
#         g_num+=1
#     print(g_num)
#
# def work2():
#     global g_num
#     for x in range(100):
#         g_num+=1
#     print(g_num)
#
# g_num=0
# if __name__ == '__main__':
#     f1=threading.Thread(target=work1)
#     f2=threading.Thread(target=work2)
#     f1.start()
#     f1.join()
#     f2.start()

"""
定义两个任务，定义全局变量，使用互斥锁机制，完成两个任务各自相加100000次操作
"""
# import threading,time
# def work1():
#     global num
#     lock.acquire()
#     for x in range(10000):
#         num+=1
#     print(num)
#     lock.release()
#
# def work2():
#     global num
#     lock.acquire()
#     for x in range(10000):
#         num+=1
#     print(num)
#     lock.release()
#
# num=0
# lock=threading.Lock()
# if __name__ == '__main__':
#     f1=threading.Thread(target=work1)
#     f2=threading.Thread(target=work2)
#     f1.start()
#     f2.start()



"""
使用进程池创建3个进程，使用这3个进程随意对操作任务work，在work中进行并做出随意耗时操作
"""
# import multiprocessing,time
# def work():
#     print(1)
#     time.sleep(1)
# if __name__ == '__main__':
#     pool=multiprocessing.Pool(3)
#     for x in range(9):
#         pool.apply_async(work)
#         # pool.apply(work)
#     pool.close()
#     # time.sleep(1)
#     # pool.terminate()
#     pool.join()



"""
实现进程间通信，定义两个函数，分别在两个函数中作如下操作：
（1）正确导入通信使用到的模块
（2）在两个任务中分别做0.1秒耗时操作
"""
# import multiprocessing
# def write(q):
#     for x in range(10):
#         if q.full():
#             print('满了')
#             break
#         else:
#             print('添加：',x)
#             q.put(x)
# def read(q):
#     while True:
#         if q.empty():
#             print('没饿了')
#             break
#         else:
#             print('取出：',q.get())
#
# if __name__ == '__main__':
#     q=multiprocessing.Queue(5)
#     f1=multiprocessing.Process(target=write,args=(q,))
#     f2=multiprocessing.Process(target=read,args=(q,))
#     f1.start()
#     f1.join()
#     f2.start()



"""
定义一个类，实现线程执行功能，定义三个任务work1    work2    work3,
(1)在每个任务中打印出当前执行的是哪个线程
(2)正确继承线程模块
"""
# import threading,time
# def work1():
#     print('我是线程1哦。。。')
#     time.sleep(1)
#
# def work2():
#     print('我是线程2哦...')
#     time.sleep(1)
#
# def work3():
#     print('我是线程3哦....')
#     time.sleep(1)
#
# if __name__ == '__main__':
#     f1=threading.Thread(target=work1)
#     f2=threading.Thread(target=work2)
#     f3=threading.Thread(target=work3)
#     print(threading.current_thread())   #当前执行的线程
#     f1.start()
#     print(threading.enumerate())       #也是当前执行的有哪些线程
#     print(len(threading.enumerate()))   #当前执行线程的个数
#     f1.join()
#     f2.start()
#     print(threading.enumerate())  # 也是当前执行的有哪些线程
#     print(len(threading.enumerate()))  # 当前执行线程的个数
#     f2.join()
#     f3.start()
#     print(threading.enumerate())  # 也是当前执行的有哪些线程
#     print(len(threading.enumerate()))  # 当前执行线程的个数
#     f3.join()
#     print('主线程要结束了哦')
#     print(threading.enumerate())  # 也是当前执行的有哪些线程
#     print(len(threading.enumerate()))  # 当前执行线程的个数





"""
内置性能测试
"""
# import timeit
# def func():
#     print('我是测试模块哦...')
#
# if __name__ == '__main__':
#     f=timeit.Timer('func()','from __main__ import func')
#     print(f.timeit(10))           # f.timeit(10)  是   代码执行十次  并返回运行的时间




"""
[12,56,7,89,103,13],给定一个列表，随机录入输入一个数字，判断这个录入的数是否在这个列表中
"""
# x=[12,56,7,89,103,13]
# num=int(input('请输入你要判断的数字：'))
# if num in x:
#     print('在哦')
# else:
#     print('哎，不再')


"""
使用greenlet模块实现协程，并有耗时等待
"""
# from greenlet import greenlet
# import time
# def f1():
#     while True:
#         n=s2.switch()
#         print('消费者：',n)
#
# def f2():
#     for x in range(5):
#         print('生产者：',x)
#         s1.switch(x)
#         time.sleep(1)
#
# if __name__ == '__main__':
#     s1=greenlet(f1)
#     s2=greenlet(f2)
#     s1.switch()


"""
正则匹配手机号
"""
# import re
# list=['13146152021','12146152021','131461520211','13146152024']
# for x in list:
#     f=re.match('^1[3-9]\d{8}[^47]$',x)
#     if f:
#         print(f.group())
#     else:
#         print('手机号不符合规则')


'''
正则匹配邮箱
'''
# import re
# f=re.match(r'^\w{4,25}@(163|139|109)\.com$','asdzxc123@163.com')
# if f:
#     print(f.group())
# else:
#     print('匹配失败')

'''
正则匹配网址
'''
# import re
# f=re.match(r'<(\w+)><(\w+)>.+</\2></\1>','<html><h1>lueluelue</h1></html>')
# if f:
#     print(f.group())
# else:
#     print('匹配失败')



'''四大高阶函数'''

'''map()'''
# def cheng(n):
#     return n*2
# f=map(cheng,[1,2,3,4,5])
# print(list(f))

'''reduce()'''
# from functools import reduce
# def sum(x,y):
#     return x+y
# f=reduce(sum,[1,2,3,4,5])
# print(f)

'''filter()'''
# def shaixuan(n):
#     return n%2==0
# f=filter(shaixuan,[1,2,3,4,5])
# print(list(f))

'''sorted()'''
# print(sorted([1,3,2,5,4],key=lambda x:x,reverse=True))


'''udp'''
# from socket import *
# udp_socket=socket(AF_INET,SOCK_DGRAM)
# addr=('192.168.1.6',8080)
# udp_socket.sendto('我想你了'.encode('gbk'),addr)
# ret,ip=udp_socket.recvfrom(1024)
# print(ret.decode('gbk'))
# print(ip)
# udp_socket.close()

'''绑定客户端'''
# from socket import *
# udp_socket=socket(AF_INET,SOCK_DGRAM)
# addr=('',8080)
# udp_socket.sendto('我不想你啊'.encode('gbk'),('192.168.1.6',8800))
# ret,ip=udp_socket.recvfrom(1000)
# print(ret.decode('gbk'))
# print(ip)
# udp_socket.close()


'''tcp'''
# from socket import *
# tcp_socket=socket(AF_INET,SOCK_STREAM)
# addr=('192.168.1.6',8080)
# tcp_socket.connect(addr)
# tcp_socket.send('我好想你'.encode('gbk'))
# ret=tcp_socket.recv(1000)
# print(ret.decode('gbk'))
# tcp_socket.close()

#绑定
# from socket  import *
# tcp_server_socket=socket(AF_INET,SOCK_STREAM)
# tcp_server_socket.bind(('',8080))
# tcp_server_socket.listen(100)
# tcp_client_socket,tep_client_ip=tcp_server_socket.accept()
# tcp_client_socket.send('我真想你啊'.encode('gbk'))
# ret=tcp_client_socket.recv(1000)
# print(ret.decode('gbk'))
# tcp_client_socket.close()
# tcp_server_socket.close()

# import re
# ss=''
# str= 'asd123qwe456-789---5WS-23sd'
# while True:
#     i = 0
#     for x in str:
#         if x.isalpha():
#
#             break
#         i += 1
#     f = re.search('[a-zA-Z]+', str)
#     if f:
#         ss += f.group()
#         str = str[(i + len(f.group())):]
#     else:
#         break
# print(ss)


# x=1
# if type(x) is int:
#     print(2)

# f=re.search('\d+',str)
# str = str[( len(f.group())):]
# print(str)

# for x in str:
#     if x>='0' and x<='9':
#         print(x)



# i = 0
# for x in str:
#     if type(x) is int:
#         i = x
#     i += 1
# print(i)
# f = re.search('\d+', str)
# if f:
#     ss += f.group()
#     str = str[(i + len(f.group())):]
#
# print(str)


import threading
def work():
    lock.acquire()




if __name__ == '__main__':
    lock=threading.Lock()















