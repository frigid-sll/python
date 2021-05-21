"""
1、功能描述：

  使用代码定义一个数组，
  并且用选择排序方法对数组就行排序，
  正序或者倒序用参数来控制，
  用自己的语言将整个排序过程进行注释
"""

# a=[1,3,2,5,4]
# for x in range(len(a)-1):
#     maxx=x
#     for i in range(x+1,len(a)):
#         if a[maxx]<a[i]:
#             maxx=i
#     if maxx!=x:
#         a[x],a[maxx]=a[maxx],a[x]
# print(a)

"""




2、功能描述：

自定义一个迭代器，并且重写iter()和next()方法，
对一个数组进行迭代
"""

# class F(object):
#     def __init__(self,a):
#         self.a=a
#         self.current=0
#     def __next__(self):
#         if self.current<len(a):
#             x=self.a[self.current]
#             self.current+=1
#             return x
#         else:
#             raise StopIteration
#     def __iter__(self):
#         return self
# a=[1,2,3]
# f=F(a)
# for x in f:
#     print(x)

"""
3、功能描述：

使用代码定义装饰器函数嵌套，并用语言描述执行细节

要求（按完成的功能量给与相应条件的分数，未实现该条件功能效果不给分）：
1)正确使用装饰器引用
2)正确使用函数嵌套的逻辑
3)正确用注释语言描述整个过程，并且没有遗漏
"""

# def w(n):
#     print(1)
#     def inner():
#         print(2)
#         n()
#     return inner
#
# @w
# def f():
#     print(3)
#
# f()


"""
4、使用filter过滤器和lambda表达式得到1-20之间能被2整除的数
"""
# print(list(filter(lambda x:x%2==0,[x for x in range(1,21)])))


"""
5、功能描述：

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
#
# for x in fei(20):
#     print(x)








"""
6、定义函数，使用isinstance方法判断列表、元组、数字、集合、字符串、字典中的可变类型和不可变类型数据

要求（按完成的功能量给与相应条件的分数，未实现该条件功能效果不给分）：
1) 正确引入isinstance需要导入的python库
2) 正确用代码判断并且打印方法返回的对象
3) 正确判断所有对象的返回值，并无遗漏
"""

# from collections import Iterable
# print(isinstance([],Iterable))
# print(isinstance((),Iterable))
# print(isinstance(1,Iterable))
# print(isinstance({},Iterable))

"""
7、使用迭代器实现一个斐波那契数列
"""
# class F(object):
#     def __init__(self,n):
#         self.n=n
#         self.num1=0
#         self.num2=1
#         self.current=0
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
# f=F(5)
# for x in f:
#     print(x)



"""
8、自定义列表使用冒泡排序对该无序列表排序
"""
# a=[1,3,2,5,4]
# for x in range(len(a)-1,0,-1):
#     for i in range(x):
#         if a[i]>a[i+1]:
#             a[i],a[i+1]=a[i+1],a[i]
# print(a)

"""
9、功能描述：
给定两个列表，list1 = [[3,2,63],100],list2 =[(1,2),[“I”,”love”,”woman”]],
分别对两个列表完成浅拷贝、深拷贝操作，并描述最外层和里面的列表元素发生什么样变化。
要求（按完成的功能量给与相应条件的分数，未实现该条件功能效果不给分）：
1)实现浅拷贝操作
2)实现深拷贝操作
3)成功描述最外层和里面的元素具体发生了什么变化
"""
# import copy
# list1=[[3,2,63],100]
# list2=[(1,2),['I','love','woman']]
# a1=copy.copy(list1)
# a2=copy.deepcopy(list2)

"""
10、功能描述：

请用代码实现变量名解析LEGB原则，并用语言描述清楚
要求（按完成的功能量给与相应条件的分数，未实现该条件功能效果不给分）：
1) 正确用代码声明全局变量
2) 正确用代码声明嵌套作用域以及局部作用域
3) 正确用注释语言描述清晰
"""
a=1   #全局作用域
def a():
   a=2    #嵌套作用域
   def b():
       a=3   #局部作用域
if __name__ == '__main__':
    a=4    #内置作用域
"""
11、分别使用常规方法和递归函数两种方法，
在有序序列alist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
中搜索8和88两个元素。
"""
# alist=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
# def cha(a,item):
#     if len(a)==0:
#         return False
#     else:
#         x=len(a)//2
#         if item==a[x]:
#             return True
#         elif item>a[x]:
#             return cha(a[x+1:],item)
#         else:
#             return cha(a[:x],item)

# def cha(a,item):
#     first=0
#     last=len(a)-1
#     while first<=last:
#         x = (first + last) // 2
#         if a[x] == item:
#           return True
#         elif item > a[x]:
#             first = x + 1
#         else:
#             last = x - 1
#     return False
#
# print(cha(alist,8))
# print(cha(alist,88))




# def s(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return n+s(n-1)
# print(s(5))

# def s(n):
#     if n==0:
#         return 0
#     else:
#         if n % 2 == 0:
#             return n + s(n - 2)
#         else:
#             return s(n - 1)
# print(s(6))

# n=3.6
# print(int(n))


def sum3(n):
    if n==0:
        return 0
    else:
        return n+sum3(n-1)

def sum1(n):
    if n==0:
        return 0
    else:
        if n%2==0:
            return n+sum1(n-2)
        else:
            return sum1(n-1)

def sum2(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        if n%2!=0:
            return n+sum2(n-2)
        else:
            return sum2(n-1)

print(sum3(3))
print(sum1(3))
print(sum2(3))
