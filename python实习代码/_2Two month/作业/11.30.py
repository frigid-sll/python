"""
1、功能描述：
  使用代码定义一个数组，
  并且用选择排序方法对数组就行排序，
  正序或者倒序用参数来控制，
  用自己的语言将整个排序过程进行注释（20分）
"""
#
# a=[1,3,2,5,4]
# for x in range(len(a)-1):    #进行len(a)-1次外排序
#     minn=x                    #定义最小元素的下标
#     for i in range(x+1,len(a)):   #进行len(a)-x-1次内排序
#         if a[minn]>a[i]:          #若a[minn]不是最小元素就交换下标值
#             minn=i
#     if minn!=x:
#         a[minn],a[x]=a[x],a[minn]     #交换值
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
#     def __next__(self):
#         if self.current<len(self.n):
#             x=self.n[self.current]
#             self.current+=1
#             return x
#         else:
#             raise StopIteration
#     def __iter__(self):
#         return self
# f=F([1,2,3,4,5])
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
#     print(1)
#     def inner(a,b):
#         print("66666666666")
#         print(a+b)
#         func(a)
#     return inner
# @w
# def f(c):
#     print(3)
#
# f(1,2)

"""
4、使用filter过滤器和lambda表达式得到1-20之间能被2整除的数（10分）
"""

# print(','.join(list(filter(lambda x:int(x)%2==0,['%s'%x for x in range(1,21)]))))

"""
5、功能描述：（10分）

请用生成器实现斐波那契数列（长度小于20）

要求（按完成的功能量给与相应条件的分数，未实现该条件功能效果不给分）：
1)正确使用yield关键字
2)正确用代码实现斐波那契逻辑（两值相加等于第三）
正确打印出斐波那契数列，列表元素个数小于20
"""

# def fei(n):
#     num1,num2=0,1
#     for x in range(n):
#         num,num1,num2=num1,num2,num1+num2
#         yield num
# print(list(fei(19)))

"""
6、定义函数，使用isinstance方法判断列表、元组、数字、集合、字符串、字典中的可迭代对象（10分）

要求（按完成的功能量给与相应条件的分数，未实现该条件功能效果不给分）：
1) 正确引入isinstance需要导入的python库
2) 正确用代码判断并且打印方法返回的对象
3) 正确判断所有对象的返回值，并无遗漏
"""

# def pan():
#     from collections import Iterable
#     x=isinstance([1,2],Iterable)
#     y=isinstance((1,2),Iterable)
#     z=isinstance(1,Iterable)
#     a=isinstance({1,2,3},Iterable)
#     b=isinstance('asd2',Iterable)
#     c=isinstance({'name':'123','age':18},Iterable)
#     return x,y,z,a,b,c
# print(pan())

"""
7、使用迭代器实现一个斐波那契数列（10分）
"""

# class F(object):
#     def __init__(self,n):
#         self.current=0
#         self.n=n
#         self.num1=0
#         self.num2=1
#     def __next__(self):
#         if self.current<self.n:
#             num=self.num1
#             self.num1,self.num2=self.num2,self.num1+self.num2
#             self.current+=1
#             return num
#         else:
#             raise StopIteration
#     def __iter__(self):
#         return self
#
# print(list(F(10)))


"""
8、自定义列表使用冒泡排序对该无序列表排序（20分）
"""
a=[1,3,2,5,4]
for x in range(len(a)-1):
    for i in range(len(a)-1-x):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
print(a)

"""
9、功能描述：（10分）
给定两个列表，list1 = [[3,2,63],100],list2 =[(1,2),[“I”,”love”,”woman”]],
分别对两个列表完成浅拷贝、深拷贝操作，并描述最外层和里面的列表元素发生什么样变化。
要求（按完成的功能量给与相应条件的分数，未实现该条件功能效果不给分）：
1)实现浅拷贝操作
2)实现深拷贝操作
3)成功描述最外层和里面的元素具体发生了什么变化
"""
# list1,list2=[[3,2,63],100],[(1,2),['I','love','woman']]
# import copy
# a=copy.copy(list1)
# a2=copy.deepcopy(list1)
# b=copy.copy(list2)
# b2=copy.deepcopy(list2)
# print(id(list1))
# print(id(a))
# print(id(a2))
# print(id(list1[0]))
# print(id(a[0]))
# print(id(a2[0]))
# 浅拷贝最外层的所有元素地址与原列表的元素一样，里面的元素也是一样
# 深拷贝最外层的不可变类型元素的地址与原列表一样，可变元素的地址不一样，里面的元素也是一样
# 深拷贝和浅拷贝的新列表的地址与原列表的地址不一样

"""
10、功能描述：（10分）

请用代码实现变量名解析LEGB原则，并用语言描述清楚
要求（按完成的功能量给与相应条件的分数，未实现该条件功能效果不给分）：
1) 正确用代码声明全局变量
2) 正确用代码声明嵌套作用域以及局部作用域
3) 正确用注释语言描述清晰
"""
# a=0         #全局作用域
# def f():
#     global a
#     # a=1     #嵌套作用域
#     b=1
#     def f2():
#         nonlocal b
#         b=3     #局部作用域
#         # a=4
#         print(a)
#     return f2
#
# print(__name__)       内置
# print(a)
# f()()
#局部作用域》嵌套作用域》全局作用域》内置作用域

"""
11、分别使用常规方法和递归函数两种方法，
在有序序列alist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
中搜索8和88两个元素。(20分)
"""
alist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
# def cha(n,item):
#     if len(n)==0:
#         return False
#     else:
#         x=len(n)//2
#         if item==n[x]:
#             return True
#         elif item>n[x]:
#             return cha(n[x+1:],item)
#         else:
#             return cha(n[:x],item)
# print(cha(alist,8))
# print(cha(alist,88))
# def cha2(a,item):
#     first=0
#     last=len(a)-1
#     while first<=last:
#         x=(first+last)//2
#         if a[x]==item:
#             return True
#         elif item>a[x]:
#             first=x+1
#         else:
#             last=x-1
#     return False
# print(cha2(alist,8))
# print(cha2(alist,88))



"""
12、使用递归实现0--100和，偶数和，奇数和（30分）
"""
# def s(n):
#     if n==0:
#         return 0
#     else:
#         if n%2==0:
#             return n+s(n-2)
#         else:
#             return s(n-1)
# print(s(100))
#
# def s2(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         if n%2==1:
#             return n+s2(n-2)
#         else:
#             return s2(n-1)
# print(s2(100))


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
#     def push(self,item):
#         self.stack.append(item)
#     def pop(self):
#         return self.stack.pop()
#     def peek(self):
#         return self.stack[len(self.stack)-1]
#     def is_empty(self):
#         return self.stack == []
#     def size(self):
#         return len(self.stack)
# s=Stack()
# print(s.is_empty())
# s.push(1)
# s.push(2)
# s.push(3)
# print(s.pop())
# print(s.peek())
# print(s.size())

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
#     def enqueue(self,item):
#         self.queue.append(item)
#     def dequeue(self):
#         return self.queue.pop(0)
#     def is_empty(self):
#         return self.queue == []
#     def size(self):
#         return len(self.queue)
# q=Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# print(q.dequeue())
# print(q.is_empty())
# print(q.size())
"""
15.list内置类型的时间复杂度：（10分）
append      O(1)
insert      O(n)
sort        O(nlogn)
pop()       O(1)
pop(i)      O(i)
reverse     O(n)
"""






# def f(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return f(n-1)+f(n-2)
# n=int(input('请输入你要查看几个数:'))
# for x in range(n):
#     print(f(x))









