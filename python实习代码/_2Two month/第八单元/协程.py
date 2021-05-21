# import time
# def work1():
#     while True:
#         print('work1...')
#         time.sleep(0.5)
#         yield
#
# def work2():
#     while True:
#         print('work2...')
#         time.sleep(0.5)
#         yield
#
# if __name__ == '__main__':
#     while True:
#         next(work1())
#         next(work2())


# def consumer():
#     r=''
#     while True:
#         n=yield r
#         print('消费了：',n)
#
# def produce(c):
#     c.send(None)
#     for x in range(5):
#         print('生产者：',x)
#         c.send(x)
#
# produce(consumer())



# from greenlet import greenlet
# def consumer():
#     while True:
#         n=f2.switch()
#         print('消费了：',n)
# def produce():
#     for x in range(5):
#         print('生产了:',x)
#         f1.switch(x)
# if __name__ == '__main__':
#     f1=greenlet(consumer)
#     f2=greenlet(produce)
#     f1.switch()

# import gevent
# def work1():
#     print(1)
# def work2():
#     print(2)
# def work3():
#     print(3)
# if __name__ == '__main__':
#     gevent.joinall(
#         [
#             gevent.spawn(work1),
#             gevent.spawn(work2),
#             gevent.spawn(work3)
#         ]
#     )

# from greenlet import greenlet
# def consuner():
#     while True:
#         n=f2.switch()
#         print('消费了：',n)
#
# def produce():
#     for x in range(5):
#         print('生产了:',x)
#         f1.switch(x)
#
# if __name__ == '__main__':
#     f1=greenlet(consuner)
#     f2=greenlet(produce)
#     f1.switch()



# import gevent
# def work1():
#     print(1)
# def work2():
#     print(2)
# def work3():
#     print(3)
#
# if __name__ == '__main__':
#     gevent.joinall(
#         [
#             gevent.spawn(work1),
#             gevent.spawn(work2),
#             gevent.spawn(work3)
#         ]
#     )

# print(list(map(abs,range(-4,5))))



# import gevent,time
# from gevent import monkey
# # monkey.patch_all()
#
# def work1():
#     print('work1',gevent.getcurrent())
#     for x in range(10):
#         print('wokr1')
#         time.sleep(1)
#
# def work2():
#     print('work2',gevent.getcurrent())
#     for i in range(10):
#         print('work2')
#         time.sleep(1)
#
# if __name__ == '__main__':
#     gevent.joinall(
#         [
#             gevent.spawn(work1),
#             gevent.spawn(work2)
#         ]
#     )

# import threading
# def f(n):
#     a=[1,2,3,4,5]
#     lock.acquire()
#     if n>=len(a):
#         print(6666666)
#         return
#     print(a[n])
#     lock.release()
#
# if __name__ == '__main__':
#     lock=threading.Lock()
#     for x in range(10):
#         f1 = threading.Thread(target=f, args=(x,))
#         f1.start()



