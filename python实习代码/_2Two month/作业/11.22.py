'''
给定两个列表，list1 = [[3,2,63],90],list2 =[(2,3),[“I”,”love”,”china”]],

分别对两个列表完成浅拷贝、深拷贝操作，并描述最外层和里面的列表元素发生什么样变化。

1.list1 最外层是可变类型数据，经过浅拷贝最外层会产生新的对象，内层的可变数据直接引用，内层的不可变也是直接引用，经过深拷贝最外层会生成新的引用，内层的可变也会生成新的引用，内层不可变直接引用

2.list2最外层是不可变类型数据，经过浅拷贝最外层会直接引用，内层不可变类型数据是直接引用，内存可变类型也是直接引用 ，经过深拷贝，最外层会生成新的对象，内层不可变是直接引用，内层可变类型是产生新的引用

'''
# list1=[[3,2,63],90]
# list2=[(2,3),['I','love','china']]
# import copy
# a=copy.copy(list1)
# b=copy.deepcopy(list1)
# c=copy.copy(list2)
# d=copy.deepcopy(list2)

# class F(object):
#     def __init__(self):
#         self.q=[]
#     def add(self,n):
#         self.q.append(n)
#     def  __iter__(self):
#         s=F2(self)
#         return s
# class F2(object):
#     def __init__(self,w):
#         self.w=w
#         self.d=0
#     def __next__(self):
#         if self.d<len(self.w.q):
#             x=self.w.q[self.d]
#             self.d+=1
#             return x
#         else:
#             raise StopIteration
#     def __iter__(self):
#         return self
# f=F()
# for x in range(5,0,-1):
#     f.add('*'*x)
# for i in f:
#     print(i)



# class F(object):
#     def __init__(self):
#         self.list=[]
#         self.current=0
#     def add(self,n):
#         self.list.append(n)
#     def __next__(self):
#         if self.current<len(self.list):
#             self.current+=1
#             return self.list[self.current-1]
#         else:
#             raise StopIteration
#     def __iter__(self):
#         return self
# f=F()
# for x in range(5,0,-1):
#     f.add('*'*x)
# for i in f:
#     print(i)


# def f(n):
#     num1,num2=0,1
#     for x in range(n):
#         num,num1,num2=num1,num2,num1+num2
#         yield num
# for x in f(5):
#     print(x)






def w(func):
    def f():
        print('装饰器哦')
        func()
    return f

def w2(func):
    def f():
        print('装饰器2号哦')
        func()
    return f

@w
@w2
def f():
    print('我是被装饰的函数哦')

if __name__ == '__main__':
    import timeit
    t=timeit.Timer('f()','from __main__ import f')
    print(t.timeit(1))
































