# 结论：
# 浅拷贝和深层拷贝 列表
# 当列表里没有嵌套列表时，两者无区别
# 修改一个列表里的元素值时另一个列表对应下标的元素值不变
# 当列表里有嵌套列表时，两者有区别
# 浅层拷贝：修改一个列表里嵌套的列表'的元素值时另一个列表对应下标的元素值改变
# 深层拷贝：修改列表里嵌套的列表的元素值时另一个列表对应下标的元素值不改变

# copy模块用于对象的拷贝操作。
#
# 该模块只提供了两个主要的方法：copy.copy与copy.deepcopy，分别表示浅拷贝与深拷贝。
#
# 浅拷贝：
# 不管是多么复杂的数据结构，浅拷贝只会拷贝第一层
# 浅拷贝是对于一个对象的顶层拷贝
# 通俗的理解是：拷贝了引用(地址)，并没有拷贝内容

# 深拷贝：
# 深拷贝会完全复制原变量的所有数据（ 递归性质的拷贝 ），在内存中生成一套完全一样的内容，我们对这两个变量中的一个进行任意修改都不会影响另一个变量。
# 新拷贝的列表里的每一个元素的地址与原地址里每个相同元素的地址是不一样的
# 整体新列表与原列表地址是不一样的 ，里面对应的元素的地址也是不一样的

# a=[11,22]
# b=a
# print(id(a))
# print(id(b))
# a.append(33)
# print(a)
# print(b)
# print(id(a))
# print(id(b))


# c=[[1,2],[[3,4],5]]
# import copy
# w=copy.copy(c)
# e=copy.deepcopy(c)
# print(id(c))
# print(id(w))
# print(id(e))
# print(id(c[0]))
# print(id(w[0]))
# print(id(e[0]))
# print(id(c[1][1]))
# print(id(w[1][1]))
# print(id(e[1][1]))

import copy
# a=1
# b=copy.copy(a)
# c=copy.deepcopy(a)
# d=a
# print(id(a))
# print(id(b))
# print(id(c))
# print(id(d))
'''
140703516058448
140703516058448
140703516058448
140703516058448
'''
# a=[1,2]
'''
140703494169456
140703494169456
2295152244296
2295152223112
2295152325960
2295152244296
'''
a=[[1,2],[3,4]]
b=copy.copy(a)
c=copy.deepcopy(a)
d=a
print(id(a[1]))
print(id(b[1]))
print(id(c[1]))
print(id(d[1]))
print(id(a[1][1]))
print(id(b[1][1]))
print(id(c[1][1]))
print(id(d[1][1]))
print(id(a))
print(id(b))
print(id(c))
print(id(d))

# q=c
# print(q)
# print(c)
# print(id(q))
# print(id(c))
# print(id(q[0]))
# print(id(q[1]))
# print(id(c[0]))
# print(id(c[1]))


# a=1
# b=1
# c=a
# print(id(a))
# print(id(b))
# print(id(c))
import copy
# d=copy.copy(a)
# print(id(d))
# a=2
# print(a)
# print(id(a))
# print(d)
# print(id(d))

# e=copy.deepcopy(a)
# print(e)
# print(id(e))
# a=2
# print(id(e))
# print(e)
# a=[1,[2,3],3]
# s=copy.deepcopy(a)
# print(s)
# print(id(a[1]))
# print(id(s[1]))
# print(id(a))
# print(id(s))
# print(id(a[0]))
# print(id(s[0]))
# a[0]=7
# print(id(a[0]))
# print(id(s[0]))
# print(s[0])
# print(a[0])
# d=copy.deepcopy(a)
# print(id(d))