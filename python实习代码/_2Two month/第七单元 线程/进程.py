#Process语法结构

# Process([group [, target [, name [, args [, kwargs]]]]])
# target：如果传递了函数的引用，可以任务这个子进程就执行这里的代码
# args：给target指定的函数传递的参数，以元组的方式传递
# kwargs：给target指定的函数传递命名参数
# name：给进程设定一个名字，可以不设定
# group：指定进程组，大多数情况下用不到

# Process创建的实例对象的常用方法：
# start()：启动子进程实例（创建子进程）
# is_alive()：判断主进程子进程是否还在活着
# join([timeout])：是否等待子进程执行结束，或等待多少秒
# terminate()：不管任务是否完成，立即终止子进程

# Process创建的实例对象的常用属性：
# name：当前进程的别名，默认为Process-N，N为从1开始递增的整数
# pid：当前进程的pid（进程号）

#实例1  两个while循环一起执行
# import multiprocessing,time
# def q():
#     while True:
#         print('--2---')
#         time.sleep(2)
# if __name__=='__main__':
#     p = multiprocessing.Process(target=q)
#     p.start()
#     while True:
#         print('---1----')
#         time.sleep(2)

#实例2-打印进程pid
# import multiprocessing,os,time
# def zi():
#     # os.getpid()获取当前进程的进程号
#     print('子进程运行中，pid=%d...'%os.getpid())
#     print('子程序将要结束')

# if __name__=='__main__':
#     print('父进程pid:%d'%os.getpid())
#     p=multiprocessing.Process(target=zi)
#     p.start()


#进程间不共享全局变量
#多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响

#例如：
# from multiprocessing import Process
# import os,time
# nums=[11,22]
# def work1(num):
#     '''子进程要执行的代码'''
#     print('in process1 pid=%d,nums=%s'%(os.getpid(),nums))
#     nums.append(33)
#     time.sleep(2)
#     print('in process1 pid=%d,nums=%s'%(os.getpid(),nums))
# def work2(num):
#     '''子进程要执行的代码'''
#     print('in process2 pid=%d,nums=%s'%(os.getpid(),nums))
#     nums.append(44)
#     time.sleep(2)
#     print('in process2 pid=%d,nums=%s'%(os.getpid(),nums))
# if __name__=='__main__':
#     p1=Process(target=work1,args=(nums,))
#     p1.start()
#     p1.join()
#     p2=Process(target=work2,args=(nums,))
#     p2.start()
#     p2.join()
#     nums.append(55)
#     print('in main process pid=%d,nums=%s'%(os.getpid(),nums))


# import multiprocessing,time
# def run_proc():
#     while True:
#         print('---2---')
#         time.sleep(1)
# def w():
#     print('eeeeeeeeeeee')
# if __name__ == '__main__':
#     # p=multiprocessing.Process(target=run_proc)
#     # p.start()
#     p2=multiprocessing.Process(target=w)
#     p2.start()
#     p2.join()
#     print('123')

# import threading,time
# def run_proc():
#     while True:
#         print('--2--')
#         time.sleep(1)
# if __name__ == '__main__':
#     p=threading.Thread(target=run_proc)
#     p.start()
#     while True:
#         print('--1--')
#         time.sleep(1)


# import multiprocessing,os,time
# def run_proc():
#     print('子进程运行中，pid=%d...'%os.getpid())
#     print('子进程将要结束...')
# if __name__ == '__main__':
#     print('123')
#     p=multiprocessing.Process(target=run_proc)
#     p.start()
#     # time.sleep(2)
#     print('父进程pid:%d'%os.getpid())


#进程间通信
from multiprocessing import Process,Queue
import time
def write(q):
    for value in ['A','B','C']:
        print('put %s to queue...'%value)
        q.put(value)
        time.sleep(1)
def read(q):
    while not q.empty():
        value=q.get(True)
        print('get %s from queue'%value)
        time.sleep(1)
if __name__ == '__main__':
    q=Queue()
    p1=Process(target=write,args=(q,))
    p1.start()
    p1.join()
    p2=Process(target=read,args=(q,))
    p2.start()
    p2.join()





# import multiprocessing
# def w():
#     for x in range(6):
#         print(x)
#
# if __name__ == '__main__':
#     p=multiprocessing.Process(target=w)
#     p.start()



# a='asd123qwe456*789'
# f=filter(lambda x:x.isdigit(),a)
# x=''.join(list(f))
# # print(type(x))
# import re
# s=re.match('\d*',x)
# print(s.group())



# import multiprocessing,os
# def work():
#     print('子进程的编号为:',os.getpid())
#
# if __name__ == '__main__':
#     p=multiprocessing.Process(target=work)
#     p.start()
#     print('父进程编号为：',os.getpid())

# import multiprocessing,os,time
# def work():
#     for x in range(10):
#         print('我正在执行哦,我的进程号为：', os.getpid())
#
# if __name__ == '__main__':
#     f=multiprocessing.Process(target=work)
#     f.start()
#     print('我是父进程，我的进程号是：',os.getpid())
#     # time.sleep(1)
#     f.terminate()
#     print('看看子进程还在不在啊：',f.is_alive())
#     f.join()
#     print('再看一次子进程还在不在啊',f.is_alive())


# import multiprocessing,os
# def w(q):
#     print('我是紫禁城')
#     for x in range(5):
#         print('放入：',x)
#         q.put(x)
#
#
#
# if __name__ == '__main__':
#     q=multiprocessing.Queue()
#     f=multiprocessing.Process(target=w,args=(q,))
#     f.start()
#     f.join()
#     print(q.qsize())
#     print('去除',q.get(True))




# import multiprocessing,os,time
# def work():
#     for x in range(10):
#         print(x)
#         time.sleep(0.1)
#
# if __name__ == '__main__':
#     f=multiprocessing.Process(target=work)
#     f.start()
#     time.sleep(0.5)
#     print('主进程结束')
#     # f.terminate()
#     time.sleep(0.1)
#     # print(f.is_alive())



# import multiprocessing,time
# list=[1,2]
# def work1():
#     list.append(3)
#     print(list)
#
# def work2():
#     list.append(4)
#     print(list)
#
# if __name__ == '__main__':
#     f1=multiprocessing.Process(target=work1)
#     f2=multiprocessing.Process(target=work2)
#     print(list)
#     list.append(5)
#     print(list)
#     time.sleep(1)
#     f1.start()
#     time.sleep(1)
#     f2.start()
#     time.sleep(1)



# import multiprocessing,time
# def write(q):
#     for x in range(10):
#         if q.full():
#             print('队列满了')
#             break
#         else:
#             print('添加',x)
#             q.put(x)
# def read(q):
#     while True:
#         if q.empty():
#             print('队列空了')
#             break
#         else:
#             print('取出',q.get())
#
# if __name__ == '__main__':
#     q=multiprocessing.Queue(5)
#     f1=multiprocessing.Process(target=write,args=(q,))
#     f2=multiprocessing.Process(target=read,args=(q,))
#     f1.start()
#     f1.join()
#     f2.start()

# import multiprocessing,time
# def work1():
#     print('正在拷贝...work1')
#     time.sleep(3)
#
#
# def work2():
#     print('正在拷贝2...work2')
#     time.sleep(3)
#
#
# def work3():
#     print('正在拷贝3...work3')
#
# if __name__ == '__main__':
#     # print(456)
#     pool=multiprocessing.Pool(2)
#     # print(multiprocessing.current_process())
#     # for x in range(10):
#     # pool.apply(work1)
#     f=multiprocessing.Process(target=work1)
#     f.start()
#     for x in range(5):
#         pool.apply_async(work2)
#         # pool.apply(work3)
#         # time.sleep(1)
#         # pool.apply_async(work)
#     pool.close()
#     pool.join()
#     print(123)


# import threading
# g_num=0
# def wokr1():
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
# if __name__ == '__main__':
#     f1=threading.Thread(target=wokr1)
#     f2=threading.Thread(target=work2)
#     f1.start()
#     f1.join()
#     f2.start()
#     f2.join()
#     print(g_num)



# import threading
# def work1():
#     global num
#     lock.acquire()
#     for x in range(10000):
#
#         num+=1
#     print(num)
#     lock.release()
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


# import multiprocessing,time
# def work():
#     print('emmmm')
#     time.sleep(1)
# if __name__ == '__main__':
#     pool=multiprocessing.Pool(3)
#     for x in range(3):
#         pool.apply_async(work)
#     pool.close()
#     pool.join()


# import multiprocessing,time
# def write(q):
#     for x in range(10):
#         if q.full():
#             print('队列满了，存不了啦')
#             break
#         else:
#             print('存进', x)
#             q.put(x)
#
# def read(q):
#     while True:
#         if q.empty():
#             print('队列里的元素都被取完啦')
#             break
#         else:
#             print('取走',q.get())
#
# if __name__ == '__main__':
#     q=multiprocessing.Queue(5)
#     f1=multiprocessing.Process(target=write,args=(q,))
#     f2=multiprocessing.Process(target=read,args=(q,))
#     f1.start()
#     f1.join()
#     f2.start()
#     f2.join()

# import threading,time
# class F(object):
#     def __init__(self):
#         pass
#     def work1(self):
#         print(1)
#         print(threading.current_thread())
#
#     def work2(self):
#         print(2)
#         print(threading.current_thread())
#
#     def work3(self):
#         print(3)
#         print(threading.current_thread())
#
# f=F()
# f1=threading.Thread(target=f.work1)
# f2=threading.Thread(target=f.work2)
# f3=threading.Thread(target=f.work3)
# f1.start()
# f1.join()
# f2.start()
# f2.join()
# f3.start()
# f3.join()


# import threading,time
# def work1():
#     global num
#     c=0
#     lock.acquire()
#     for x in range(10):
#         num += 1
#         c+=1
#         if c==4:
#             print(num)
#             lock.release()
#             time.sleep(0.1)
#             lock.acquire()
#     print(num)
#     lock.release()
#
# def work2():
#     global num
#     lock.acquire()
#     for x in range(5):
#         num+=1
#     print(num)
#     lock.release()

# num=0
# lock=threading.Lock()
# if __name__ == '__main__':
#     f1=threading.Thread(target=work1)
#     f2=threading.Thread(target=work2)
#     f1.start()
#     f2.start()

# import multiprocessing,time
# num=0
# def work1():
#     # time.sleep(2)
#     global num
#     for x in range(10):
#         num+=1
#         print(num)
#
# def work2():
#     global num
#     for x in range(5):
#         num+=1
#         print(num)
#
# if __name__ == '__main__':
#     f1=multiprocessing.Process(target=work1)
#     f2=multiprocessing.Process(target=work2)
#     f1.start()
#     f2.start()
    # f1.terminate()

# import threading,time
# def w():
#     global n
#     for x in range(10):
#         n+=1
#         print(n)
#         time.sleep(0.2)
# if __name__ == '__main__':
#     n=0
#     f=threading.Thread(target=w)
#     f.setDaemon(True)
#     f.start()
#     time.sleep(0.4)
#     print('主线程结束')

# import multiprocessing,time
# def w():
#     print(1)
#     time.sleep(1)
#
# if __name__ == '__main__':
#     pool=multiprocessing.Pool(3)
#     for x in range(10):
#         pool.apply_async(w)
#     pool.close()
#     time.sleep(2)
#     pool.terminate()
    # pool.join()




# import multiprocessing,time
# def w(q):
#     for x in range(10):
#         if q.full():
#             print('队列添加满了，不能再加了')
#             break
#         else:
#             print('向队列中添加:', x)
#             q.put(x)
#
#
# def s(q):
#     for x in range(10):
#         if q.empty():
#             print('队列里已经没有元素了')
#             break
#         else:
#             print('从队列里取出:',q.get())
#
# if __name__ == '__main__':
#     q=multiprocessing.Queue(5)
#     f1=multiprocessing.Process(target=w,args=(q,))
#     f2=multiprocessing.Process(target=s,args=(q,))
#     f1.start()
#     f1.join()
#     f2.start()

# import re
# f=re.match(r'<(?P<s>\w+)><(?P<j>\w+)>.+</(?P=j)></(?P=s)>','<html><h1>12</h1></html>')
# print(f.group())


# def cha(n,item):
#     if len(n)==0:
#         return False
#     else:
#         x=len(n)//2
#         if n[x]==item:
#             return True
#         elif item>n[x]:
#             return cha(n[x+1:],item)
#         else:
#             return cha(n[:x],item)

# def cha(n,item):
#     first=0
#     last=len(n)-1
#     while first<=last:
#         x=(first+last)//2
#         if n[x]==item:
#             return True
#         elif item>n[x]:
#             first=x+1
#         else:
#             last=x-1
#     return False


# a=[1,2,3,4,5]
# print(cha(a,5))


# a=[1,3,2,5,4]
# for x in range(len(a)-1):
#     minn=x
#     for i in range(x+1,len(a)):
#         if a[minn]>a[i]:
#             minn=i
#     if minn!=x:
#         a[minn],a[x]=a[x],a[minn]
# print(a)


# a=[1,3,2,5,4]
# for x in range(len(a)-1):
#     for i in range(len(a)-1-x):
#         if a[i]>a[i+1]:
#             a[i],a[i+1]=a[i+1],a[i]
# print(a)

# import timeit,multiprocessing
# def func():
#     print('123')
#
# if __name__ == '__main__':
#     f=multiprocessing.Process(target=func)
#     t=timeit.Timer('f.start()','from __main__ import f')
#     print(t.timeit(1))














