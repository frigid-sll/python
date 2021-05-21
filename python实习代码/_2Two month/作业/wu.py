'''1、键盘录入一个数字，请用正则表达式 表现 该数值是否是1-100间的数字，是返回True 否则返回False
'''""
# import re
# a=input("请输入数字：")
# ret=re.match("(100|[1-9]\d|[1-9])$",a)
# if ret:
#     print("True")
# else:
#     print("False")





'''2、请用折半查找法，至少两种方法表现33和81，是否在 alist = [3,6,8,23,33,45,65,75,85,99]这个列表中，
是返回True 否则返回False
'''
# def er(alsit,itme):
#     find=0
#     last=len(alsit)
#     while find<=last:
#         mid=(find+last)//2
#         if itme==alsit[mid]:
#             return True
#         elif itme<alsit[mid]:
#             last=mid-1
#         else:
#             find=mid+1
#     else:
#         return False
# if __name__ == '__main__':
#     alsit= [3, 6, 8, 23, 33, 45, 65, 75, 85, 99]
#     print(er(alsit,33))
#     print(er(alsit,81))
# def er(alist,itme):
#     n=len(alist)
#     if n==0:
#         return False
#     else:
#         mid=n//2
#         if itme==alist[mid]:
#             return True
#         elif itme<alist[mid]:
#             return er(alist[:mid],itme)
#         else:
#             return er(alist[mid+1:],itme)
#
# if __name__ == '__main__':
#     alist= [3, 6, 8, 23, 33, 45, 65, 75, 85, 99]
#     print(er(alist,33))
#     print(er(alist,81))

'''3、请用3种方法打出斐波那契数列，个数不小于30 要求：迭代器、生成器、递归
'''
# class Fei(object):
#     def __init__(self,n):
#         self.num1,self.num2=0,1
#         self.count=0
#         self.n=n
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.n>self.count:
#             num=self.num1
#             self.count+=1
#             self.num1,self.num2=self.num2,self.num1+self.num2
#             return num
#         else:
#             raise StopIteration
# if __name__ == '__main__':
#     fei=Fei(30)
#     print(list(fei))


# def fei(n):
#     num1,num2=0,1
#     count=0
#     while n>count:
#         count+=1
#         num=num1
#         num1,num2=num2,num1+num2
#         yield num
# if __name__ == '__main__':
#     print(list(fei(30)))



'''4、自定义一个返回函数的demo
'''
# def f1():
#     def f2():
#         print("aaa")
#     return f2
# if __name__ == '__main__':
#     f1()()




'''5、请借用线程实现生产者消费者模式，要求执行100次数据还能保持每生产一个消费一个
'''






'''6、请定义一个任务work1，使用进程池最大执行5个任务，至少批量执行3次，
完成并行执行输出，注意需要设置主进程阻塞，等待子进程退出。
'''





'''7、键盘录入一个邮箱，请用正则表达式匹配邮箱163、139、qq、sina  如：www.chenkai123@sina.com
'''
# import re
# a=input("请输入邮箱：")
# ret=re.match(r"^(www\.)\w{4,20}@(163|139|qq|sina)(\.com)$",a)
# if ret:
#     print("True")
# else:
#     print("False")






'''8、请用套接字实现tcp网络通讯  要求tcp分别实现服务端、客户端的通讯
'''





'''9、使用线程模块的互斥锁解决多线程间恶意竞争资源的问题，模拟情景存在全局变量num = 0，
分别创建执行函数work1和work2，并分别完成对全局变量num的修改，要求修改一次num值加1，
循环修改1000000次，并分别输出最终的num的输出结果。
'''





'''10、模拟场景当前有如下函数function(),一日老板突发奇想，想要在实现函数原有功能之前，实现附加验证功能A和B，
要求分别实现并给函数添加具有模拟实现附加验证功能A和附加验证功能B的两个装饰器函数，并给function()添加并调用，
显示输出效果。并用时间测验出执行时间
def  function():  
    print(“执行程序原有功能”)
'''
# def f1(func):
#     def f2():
#         print("阿瑟东萨达萨达")
#         func()
#     return f2
# def f2(func):
#     def f1():
#         print("d啊实打实大苏打")
#         func()
#     return f1
# @f1
# @f2
# def  function():
#     print("执行程序原有功能")
# if __name__ == '__main__':
#     function()




'''11、请用进程实现进程间通信
'''






'''12、请用sorted函数为列表排序 要求：表现分别实现升序和倒序
'''
# list=[8,2,32,2,13,21,65,515,61]
# print(sorted(list,key=lambda x:x,reverse=True))
# print(sorted(list,key=lambda x:x))




'''13、请用递归函数实现表现阶乘的结果数列 如: 0 1 2 6 24 120 720 5040 40320 362880 .....
'''






'''14、自定义一个函数，实现一个闭包
'''
# def f1():
#     a=100
#     def f2():
#         print(a)
#     return f2
# if __name__ == '__main__':
#     f1()()






'''15、自定义一个迭代器，对列表[112,34,545,6578,6,645,43,3,4]进行遍历，重写iter方法和next方法
'''
# class Dei(object):
#     def __init__(self,alist):
#         self.alist=alist
#         self.count=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if len(self.alist)>self.count:
#             self.count+=1
#             return self.alist[self.count-1]
#         else:
#             raise StopIteration
# if __name__ == '__main__':
#     alist=[112,34,545,6578,6,645,43,3,4]
#     de=Dei(alist)
#     for i in de:
#         print(i)






'''16、键盘录入一个网址，用正则表达式匹配网址，如：http://www.baidu.com
'''
# import re
# a=input("请输入网址：")
# ret=re.match(r"^(http://www\.)\w{4,20}(\.com)$",a)
# if ret:
#     print("True")
# else:
#     print("False")





'''17、请用列表实现模拟一个队列，要求：添加3个元素，删除一个元素，展示队列变化
Queue() 创建一个空的队列
enqueue(item) 往队列中添加一个item元素
dequeue() 从队列头部删除一个元素
is_empty() 判断一个队列是否为空
size() 返回队列的大小
'''





'''18、定义函数，使用isinstance方法判断列表、元组、数字、集合、字符串、字典中的可迭代对象
要求（按完成的功能量给与相应条件的分数，未实现该条件功能效果不给分）：
1) 正确引入isinstance需要导入的python库
2) 正确用代码判断并且打印方法返回的对象
3) 正确判断所有对象的返回值，并无遗漏
'''
# from collections import Iterable
# def ietr():
#     print(isinstance([],Iterable))
#     print(isinstance((),Iterable))
#     print(isinstance({1,2,3},Iterable))
#     print(isinstance({"name":"sad"},Iterable))
#     print(isinstance(741,Iterable))
#     print(isinstance("asdasdas",Iterable))
#
#
#
# if __name__ == '__main__':
#     ietr()






'''19、使用filter过滤器和lambda表达式得到1-20之间能被2整除的数
'''
# print(list(filter(lambda x:x%2==0,[x for x in range(1,21)])))






'''20、请用列表模拟一个栈，要求：添加至少3个元素，弹出一个元素，并分别查看栈顶，展示栈的变化
Stack() 创建一个新的空栈
push(item) 添加一个新的元素item到栈顶
pop() 弹出栈顶元素
peek() 返回栈顶元素
is_empty() 判断栈是否为空
size() 返回栈的元素个数
'''







'''21、分别用冒泡排序选择排序对列表进行升序排序， 列表：alist = [ 4,3,6,2,7,9,1]
'''
# def pao(alist):
#     n=len(alist)
#     for i in range(n-1):
#         for j in range(n-1-i):
#             if alist[j]>alist[j+1]:
#                 alist[j],alist[j+1]=alist[j+1],alist[j]
# if __name__ == '__main__':
#     alist = [4, 3, 6, 2, 7, 9, 1]
#     pao(alist)
#     print(alist)
# def xuan(alist):
#     n=len(alist)
#     for i in range(n-1):
#         xiabiao=i
#         for j in range(i+1,n):
#             if alist[xiabiao]>alist[j]:
#                 alist[xiabiao],alist[j]=alist[j],alist[xiabiao]
# if __name__ == '__main__':
#     alist = [ 4,3,6,2,7,9,1]
#     xuan(alist)
#     print(alist)

'''22、使用递归实现0--100和，偶数和，奇数和
'''










'''23、请用线程实现 守护主线程
'''











'''24、自定义协程  要求使用yield 和next关键字实现
'''










'''25、用demo体现线程间全局变量共享
'''










'''26、键盘录入一个手机号，请用正则表达式匹配手机号，要求开头为1号段3-8  共11位 结尾不能以147结尾
'''
# import re
# a=input("请输入手机号：")
# ret=re.match("^1[3-8]\d{8}[^147]$",a)
# if ret:
#     print(ret.group())
# else:
#     print("dsaasdf")









'''27、请使用reduce()函数，让一个参数x，对一个列表[1,2,3,4,5,6]的数值依次相乘，将结果返回
'''










'''28、使用map（）函数将第一个参数a依次作用在参数[1,2,3,4,5,6]的每一个元素上，
返回包含每次函数返回值的新迭代器  
'''







'''29、暴力破解：
条件：密码：
1.a+b+c=1000
2.a**2+b**2=c**2
要求：算出执行时间
'''










'''30、请用套接字实现udp网络通讯  要求ucp分别实现服务端、客户端的通讯
'''






'''31、定义一个类，实现进程的执行功能，定义三个任务，work1、work2、work3，
打印出每个任务当前执行的是那条进程，正确继承模块，主动终止work2，并判断work2是否存活，当前有几条进程
'''







'''32、使用genvent实现协程
'''







'''33、greenlet实现协程
'''






'''34、写出开头匹配字母和下划线，末尾是数字的正则表达式，键盘录入数据
'''






'''35、用正则表达式匹配“adhdsa135555543dasdadasd”，拿出字符串中的数字
'''










