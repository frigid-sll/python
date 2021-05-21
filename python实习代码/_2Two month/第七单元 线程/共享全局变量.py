#多线程-共享全局变量

#多线程之间共享全局变量有两种方式：
#子线程函数使用global关键字来调用函数外全局变量
#列表当作实参传递到线程中

#在一个进程内所有的线程共享全局变量，很方便在多个线程间共享数据
#缺点就是，线程是对全局变量随意遂改可能造成多线程之间对全局变量的混乱（即线程非安全）

# 共享全局变量-global全局变量

#例如：
# from threading import Thread
# from time import sleep
# num=100

# def work1():
#     global num
#     for i in range(3):
#         num+=1
#     print('经过work1,num的值为：%d'%num)
# def work2():
#     global num
#     print('经过work2，num的值为：%d'%num)

# print('线程创建之前num的值为：%d'%num)
# t1=Thread(target=work1)
# t1.start()

# #拖延一会，保证t1线程中的事情做完
# sleep(3)

# t2=Thread(target=work2)
# t2.start()



# 共享全局变量-列表当做实参

#例如：
# from threading import Thread
# from time import sleep
# def work1(num):
#     num.append(44)
#     print('经过work1 num列表为：',num)
# def work2(num):
#     #延迟一会，保证t1线程中的事情做完
#     sleep(3)
#     print('经过work2，num列表值为：',num)
# num=[11,22,33]
# t1=Thread(target=work1,args=(num,))
# t1.start()
# t2=Thread(target=work2,args=(num,))
# t2.start()

#结论：t1=Thread(target=work1,args=(list,))  args=  应该是固定的  传过去列表名后面还要有一个逗号

# import threading,time
# def a():
#     global num
#     num+=1
#     print('test1--%d'%num)
# def b():
#     global num
#     num+=1
#     print('test2--%d'%num)
# if __name__=='__main__':
#     print('开始')
#     num = 0
#     f1 = threading.Thread(target=a)
#     f2 = threading.Thread(target=b)
#     f1.start()
#     f2.start()
#     # f1.join()
#     # f2.join()
#     print('lalalal')
#     print('经过test1,test2后 num的值为：%d' % num)

# import threading,time
# def q():
#     for x in range(3):
#         time.sleep(2)
#         print('1')
# def w():
#     for x in range(3):
#         time.sleep(2)
#         print('2')
# print('wuwuwu')
# a=threading.Thread(target=q)
# b=threading.Thread(target=w)
# a.start()
# b.start()
# print('heiheiehi')
# a.join()
# b.join()
# print('lala')

# import threading,time
# def a1(num):
#     num[0]=1
#     print(num)
# def a2(num):
#     num[1]=2
#     print(num)
# num=[9,9,9,9]
# q1=threading.Thread(target=a1,args=(num,))
# q2=threading.Thread(target=a2,args=(num,))
# q1.start()
# q2.start()
# print(num)

# import threading,time
# def a1(num):
#     global add
#     add+=num
#     print(add)
# def a2(num):
#     global add
#     add+=num
#     print(add)
# add=0
# q1=threading.Thread(target=a1,args=(3,))
# q2=threading.Thread(target=a2,args=(4,))
# q1.start()
# q1.join()
# q2.start()
# print('最终结果为：%d'%add)



