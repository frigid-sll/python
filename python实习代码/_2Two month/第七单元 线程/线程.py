# python中如何创建线程：
# python的标准库提供了两个模块：_thread和threading,_thread是低级模块，threading是高级模块
# 对thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块
# 启动一个线程就是把一个函数传入并创建Tread实例，然后调用start()开始执行：

# import os
# os.rename('1.py','线程.py')

# 例如
# import threading,time
# def q():
#     print('555')
# t=threading.Thread(target=q)
# t.start()

# import threading,time
# def sing():
# 	time.sleep(4)
# 	print('正在唱歌')
# def dance():
# 	time.sleep(2)
# 	print('正在跳舞')
# if __name__=='__main__':
# 	a1=threading.Thread(target=sing)
# 	a2=threading.Thread(target=dance)
# 	a1.start()
# 	a2.start()
# 	print('555')

# import threading,time
# def sing():
# 	time.sleep(4)
# 	print('正在唱歌')
# def dance():
# 	time.sleep(2)
# 	print('正在跳舞')
# if __name__=='__main__':
# 	a1=threading.Thread(target=sing)
# 	a2=threading.Thread(target=dance)
# 	a1.start()
# 	a1.join()
# 	a2.start()
# 	a2.join()
# 	print('555')

# import threading,time
# def saysorry():
#     print('亲爱的我错了，我能吃饭了吗？')
#     time.sleep(2)
# if __name__=='__main__':
#     for i in range(5):
#         t=threading.Thread(target=saysorry)
#         t.start()

#结论：for循环中调用函数  函数结束暂停两秒才执行下一个循环  但是这五个是一起执行的  这就是线程


#需要注意的点：
#python中，默认情况下主线程执行完自己的任务后就推出了，此时子线程会继续执行自己的任务，
# 直到自己的任务结束。如果需要主线程等待其他的子线程执行结束之后再终止，需要子线程调用join()函数

 # 多线程程序的执行顺序是不确定的


# import threading
# from time import sleep
#
# def sing():
#     for i in range(5):
#         sleep(2)
#         print('正在唱歌..%d'%i)
# def dance():
#     for i in range(5):
#         sleep(2)
#         print('正在跳舞..%d'%i)
# if __name__=='__main__':
#     print('--开始--')
#     t1=threading.Thread(target=sing)
#     t2=threading.Thread(target=dance)
#     print('lalalal')
#     t2.start()
#     t1.start()
#
#     #可以尝试注释掉这两行，观察主线程和子线程结束的次序
#     t1.join()
#     t2.join()
#     print('结束--')

# import threading,time
# def ce():
#     global num
#     time.sleep(2)
#     num+=1
#     print(num)
# num=0
# f=threading.Thread(target=ce)
# f.start()
# # f.join()
# print('最终结果：%d'%num)

#结论：join()函数
# 如上实例  有join()函数时  join()下面的print是等到上面的函数运行结束后才执行的   输出的结果为1
#没有join()函数，print由于上面函数的sleep（）先执行  输出的结果为0
#当sleep()在变量自增下面时对两个输出的num的值就没有多大影响了
#这个里面的所有都是同步的   有了sleep（）就可以影响运行的结果


# from threading import Thread
# import time
# q=100
# def work1():
#     global q
#     for i in range(3):
#         q+=1
#     print('经过work1，q的值为%d'%q)
# def work2():
#     global q
#     for i in range(2):
#         q+=1
#     print('经过work2，q的值为%d'%q)
# a=Thread(target=work1)
# s=Thread(target=work2)
# a.start()
# a.join()
# s.start()
# s.join()
# print(q)

# from threading import Thread
# def work1(a):
#     a.append(4)
#     print('经过work1,列表为%s'%a)
# def work2(a):
#     a.append(5)
#     print('经过work2,列表为%s'%a)
# w=[1,2,3]
# q=Thread(target=work1,args=(w,))
# s=Thread(target=work2,args=(w,))
# q.start()
# s.start()
# print()
# print(w)


# from threading imp

# g_num = 100
# list=[1,2]
#
# def work1(n,m):
#     global g_num
#     g_num += n
#     print("----in work1, g_num is %d---" % g_num)
#     list.append(3)
#     print(list)
#
#
# def work2(n):
#     global g_num
#     g_num+=n
#     print("----in work2, g_num is %d---" % g_num)
#
#
# print("---线程创建之前g_num is %d---" % g_num)
#
# t1 = Thread(target=work1,args=(3,list,))
# t1.start()
#
# # 延时一会，保证t1线程中的事情做完
# # time.sleep(1)
# t1.join()
# t2 = Thread(target=work2,args=(3,))
# t2.start()
# t1.join()
# print(list)


# from threading import Thread
# import time
# def func():
#     print('傻不拉几的')
#     time.sleep(1)
#
# if __name__ == '__main__':
#     for x in range(5):
#         f=Thread(target=func)
#         f.start()
#         # time.sleep(1)


# import threading,time
# def sing():
#     for x in range(5):
#         print('这个在唱歌')
#         time.sleep(1)
# def dance():
#     for x in range(5):
#         print('正在跳舞')
#         time.sleep(1)
# if __name__ == '__main__':
#     f1=threading.Thread(target=sing)
#     f2=threading.Thread(target=dance)
#     f1.start()
#     f2.start()
#     f1.join()
#     f2.join()
#     print('结束')


# import threading
# list=[]
# def work1(list,a,b):
#     for x in range(5):
#         list.append(x)
#     print('work1')
#     print(a)
#     print(b)
# def work2(list):
#     for x in list:
#         print(x)
#
# if __name__ == '__main__':
#     f1=threading.Thread(target=work1,args=(list,),kwargs={'a':1,'b':2})
#     f2=threading.Thread(target=work2,args=(list,))
#     f1.start()
#     f2.start()


# import time
# def w(func):
#     def f():
#         print('装饰器')
#         func()
#     return f
# @w
# def s():
#     print('我有漏洞')
#
# if __name__ == '__main__':
    # import timeit
    # a=timeit.Timer('s()','from __main__ import s')
    # print(a.timeit(1))


# import threading,time
# def sing():
#     for x in range(5):
#         print('我在唱歌..',x)
#         time.sleep(1)
#
# def dance():
#     for x in range(5):
#         print('我在跳舞...',x)
#         time.sleep(1)
#
# if __name__ == '__main__':
#     print('1---',threading.enumerate(),len(threading.enumerate()))
#     p1=threading.Thread(target=sing)
#     p2=threading.Thread(target=dance)
#     print('2--',threading.enumerate(),len(threading.enumerate()))
#     p1.start()
#     print('3--',threading.enumerate(),len(threading.enumerate()))
#     p2.start()
#     print('-4--',threading.enumerate(),len(threading.enumerate()))
#     p1.join()
#     p2.join()
#     print('5---',threading.enumerate(),len(threading.enumerate()))




# import threading
# def work1():
#     global num
#     for x in range(10000):
#         num+=1
#     print(num)
#
# def work2():
#     global num
#     for x in range(10000):
#         num+=1
#     print(num)
#
# num=0
# if __name__ == '__main__':
#     p1=threading.Thread(target=work1)
#     p2=threading.Thread(target=work2)
#     p1.start()
#     p1.join()
#     p2.start()
#     p2.join()
#     print(num)


# import threading
# def work1():
#     lock.acquire()
#     global num
#     for x in range(10000):
#         num+=1
#     print(num)
#     lock.release()
# def work2():
#     lock.acquire()
#     global num
#     for x in range(10000):
#         num+=1
#     print(num)
#     lock.release()
#
# num=0
# lock=threading.Lock()
# if __name__ == '__main__':
#     p1=threading.Thread(target=work1)
#     p2=threading.Thread(target=work2)
#     p1.start()
#     p2.start()

# import threading
# def work(x):
#     lock.acquire()
#     if x>=len(list):
#         print('下表吵了')
#         lock.release()
#         return
#     print(list[x])
#     lock.release()
#
#
# lock=threading.Lock()
# list=[1,2,3,4,5]
# if __name__ == '__main__':
#     for x in range(10):
#         p=threading.Thread(target=work,args=(x,))
#         p.start()

# import re
# f=re.match('1(3|5)\d+','13146152021')
# if f:
#     print(f.group())

    # import threadingk


# import threading
# def w():
#     print('ai')
# if __name__ == '__main__':
#     f=threading.Thread(target=w)
#     print(threading.current_thread())

# import threading,time
# def work():
#     lock.acquire()
#     num=0
#     while True:
#         if num>=len(list):
#             print('没有了')
#             lock.release()
#             break
#         else:
#            print(list[num])
#
#         num+=1
# list=[1,2,3,4,5]
# if __name__ == '__main__':
#     lock=threading.Lock()
#     f=threading.Thread(target=work)
#     f.start()
    # time.sleep(1)

# import threading,time
# def sing():
#     for x in range(1000):
#         print('1')
#         time.sleep(0.1)
# if __name__ == '__main__':
#     f=threading.Thread(target=sing)
#     f.setDaemon(True)
#     f.start()
#     time.sleep(0.1)
#     print('主进程')







