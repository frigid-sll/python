# def func(n):
#     for i in range(0,n):
#         arg=yield i
#         print('func:',arg)
#
# f=func(10)
# f.send(None)
# print(next(f))
# f.send(100)
# f.send(90)

# def consumer():
#     r=''
#     while True:
#         n=yield r
#         print('[CONSUMER] Consuming %s...'%n)
#
# def produce(c):
#     c.send(None)
#     for n in range(1,6):
#         print('[PRODUCER] Producing %s ...'%n)
#         print(c.send(n))
#     c.close()

# produce(consumer())

# from greenlet import greenlet
#
# def consumer():
#     while True:
#         n = gr_produce.switch()
#         print('[CONSUMER] Consuming %s...' % n)
#
#
# def produce():
#     for n in range(1, 6):
#         print('[PRODUCER] Producing %s...' % n)
#         gr_consumer.switch(n)
#
# gr_consumer = greenlet(consumer)
# gr_produce = greenlet(produce)
#
# # 切换到consumer中运行
# gr_consumer.switch()

# def sheng():
#     for x in range(10):
#         r=yield x
#         print(r)
#
# f=sheng()
# print(f.send(None))
# print(f.send(111))
# print(f.send(222))
# print(f.send(333))
# print(f.send(333))
# print(f.send(333))
# print(f.send(333))
# print(f.send(333))
# print(f.send(333))
# print(f.send(333))
# print(f.send(333))
# print(f.send(333))
# f.send(2)
# f.send(3)


# def consumer():
#     r=''
#     while True:
#         n=yield r
#         print('消费者消费%d'%n)
#
# def produce(x):
#     x.send(None)
#     for i in range(1,6):
#         print('生产者生产了%d'%i)
#         x.send(i)
#     x.close()
#
# produce(consumer())

# def consumer():
#     r=''
#     while True:
#         n=yield r
#         print('消费者消费了%d'%n)
#
# def produce(x):
#     x.send(None)
#     for i in range(10):
#         print('生产者生产了%d'%i)
#         print(x.send(i))
#     x.close()
# produce(consumer())


# def consumer():
#     r=''
#     while True:
#         n=yield r
#         print('消费者消费了%d'%n)
#
# def produce(x):
#     x.send(None)
#     for i in range(1,6):
#         print('生产者生产了%d'%i)
#         x.send(i)
#     x.close()
#
# produce(consumer())





# import time
# def consumer():
#     r=''
#     while True:
#         n=yield r
#         print('消费者消费了%d'%n)
# def produce(c):
#     c.send(None)
#     for x in range(1,6):
#         print('生产者生产了%d'%x)
#         c.send(x)
#     c.close()
# produce(consumer())




# import threading,time
# def produce(q):
#     for x in range(10):
#         print('生产了：',x)
#         q.append(x)
#         time.sleep(2)
#
# def consumer(q):
#     while True:
#         if len(q)==0:
#             break
#         else:
#             print('取出:',q.pop(0))
#             time.sleep(2.02)
#
# if __name__ == '__main__':
#     q=[]
#     f1=threading.Thread(target=produce,args=(q,))
#     f2=threading.Thread(target=consumer,args=(q,))
#     f1.start()
#     f2.start()


# from greenlet import greenlet
# def consumer():
#     while True:
#         n=gr_produce.switch()
#         print('[CONSUMER] Consuming %s...'%n)
#
# def produce():
#     for n in range(1,6):
#         print('[PRODUCER] Producing %s...'%n)
#         gr_consumer.switch(n)
#
# gr_consumer=greenlet(consumer)
# gr_produce=greenlet(produce)
# gr_consumer.switch()


# from greenlet import greenlet
# def w():
#     print('123')
#     f2.switch(8)
#
# def q():
#     print(4556)
#     n=f.switch()
#     print(n)
# f=greenlet(w)
# f2=greenlet(q)
# f2.switch()


# def q():
#     print(1)
# def w():
#     while True:
#         print(2)
#         q()
#         print(3)
#
# # qp=w()


# from greenlet import greenlet
# def Consumer():
#     while True:
#         n=f2.switch()
#         print('消费者：',n)
#
# def Produce():
#     for x in range(10):
#         print('生产者：',x)
#         f1.switch(x)
#
# if __name__ == '__main__':
#     f1=greenlet(Consumer)
#     f2=greenlet(Produce)
#     f1.switch()

# from greenlet import greenlet
# def consumer():
#     while True:
#         n=f2.switch()
#         print('消费者：',n)
#
# def produce():
#     for x in range(5):
#         print('生产者:',x)
#         f1.switch(x)
#
# if __name__ == '__main__':
#     f1=greenlet(consumer)
#     f2=greenlet(produce)
#     f1.switch()


# def consuer():
#     r=''
#     while True:
#         n=yield r
#         print('消费者：',n)
#
# def produce(c):
#     c.send(None)
#     for x in range(5):
#         print('生产者：',x)
#         c.send(x)
#
# if __name__ == '__main__':
#     produce(consuer())


# from greenlet import greenlet
#
# def consumer():
#     while True:
#         n=f2.switch()
#         print('消费者：',n)
#
# def produce():
#     for x in range(5):
#         print('生产者：',x)
#         f1.switch(x)
#
# if __name__ == '__main__':
#     f1=greenlet(consumer)
#     f2=greenlet(produce)
#     f1.switch()

import gevent


# def task1():
#     print('[TASK1] Begin')
#     gevent.sleep(8)
#     print('[TASK1] End')
#
#
# def task2():
#     print('---[TASK2] Begin')
#     gevent.sleep(3)
#     print('---[TASK2] End')
#
#
# def task3():
#     print('------[TASK3] Begin')
#     print('------[TASK3] End')
#
#
# gevent.joinall([
#     gevent.spawn(task1),
#     gevent.spawn(task2),
#     gevent.spawn(task3)
# ])

# import gevent
#
# def work1():
#     print('我是work1...')
# def work2():
#     print('我是work2...')
# def work3():
#     print('我是work3...')
#
# if __name__ == '__main__':
#     gevent.joinall(
#         [
#             gevent.spawn(work1),
#             gevent.spawn(work2),
#             gevent.spawn(work3)
#         ]
#     )


import gevent,time
def consumer(n):
    print('我是消费者:',n)

def produce():
    for x in range(5):
        print('我是生产者：',x)
        gevent.spawn(consumer,x)
        gevent.sleep(1)

if __name__ == '__main__':
    gevent.joinall(
        [
            gevent.spawn(produce)
        ]
    )








