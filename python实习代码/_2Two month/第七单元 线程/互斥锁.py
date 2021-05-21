#当多个线程几乎同时修改摸一个共享数据的时候，需要进行同步控制
# 线程同步能够保证多个线程安全访问竞争资源，最简单的同步机制时引入互斥锁
#互斥锁为资源引入一个状态：锁定/非锁定
#某个线程要更改共享数据时，先将其锁定，此时资源的状态为’锁定‘，其他线程不能更改；
# 直到该线程释放资源，将资源的状态变成‘非锁定’，其他的线程才能再次锁定该资源。
# 互斥锁保证了每次只有一个线程进行写入操作，从而保证了多线程情况下数据的正确性

# threading.Lock()
# threading模块中定义了Lock类，可以方便的处理锁定：
#创建锁
#mutex=threading.Lock()
#锁定
#mutex.acquire()
#释放
#mutex.release()

#注意
#如果这个锁之前是没有上锁弟弟，那么acquire不会堵塞
#如果在调用acquire对这个锁上锁之前 他已经被 其他线程上了锁，那么此时acquire会
# 堵塞，直到这个锁被解锁为止

#使用互斥锁完成2个线程对同一个全局变量各加100万次的操作
# import threading
# def a(x):
#     global num
#     for i in range(x):
#         # mutex.acquire()   #上锁
#         num+=1
#         # mutex.release()    #解锁
#         print(num)
#     print('经过a，num的值为:%d'%num)
# def b(x):
#     global num
#     for i in range(x):
#         # mutex.acquire()
#         num+=1
#         # mutex.release()
#         print(num)
#     print('经过b后num的值为:%d'%num)
# #创建一个互斥锁，默认是未上锁状态
# # mutex=threading.Lock()
# #创建2个线程，让他们各自对num加1000000次
# num=10
# p1=threading.Thread(target=a,args=(3,))
# p1.start()
# p2=threading.Thread(target=b,args=(3,))
# p2.start()
# #等待计算完成
# p1.join()
# p2.join()
# print('2个线程对同一个全局变量操作之后的最终结果是%s'%num)


import threading,time
def work1():
    global num
    c=0
    # mutex.acquire()
    for x in range(4):
        num+=1
        c+=1
        print('%d次的值为%d'%(x,num))
        if c==2:
            # mutex.release()

            time.sleep(2)
            # mutex.acquire()
    # mutex.release()
def work2():
    global num
    # mutex.acquire()
    num=num+1
    print('经过work2后的值为：%d'%num)
    # mutex.release()
num=1
# mutex=threading.Lock()
a=threading.Thread(target=work1)
s=threading.Thread(target=work2)
a.start()
s.start()
s.join()
a.join()
num=num+2
print(num)













