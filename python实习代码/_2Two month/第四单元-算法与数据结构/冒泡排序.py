#冒泡排序：
#比较相邻的元素。如果第一个比第二个大（升序），就交换他们两个。
#对每一对相邻元素做同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数
#针对所有的元素重复以上的步骤，除了最后一个
#持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字 需要比较。

#代码实现：
# def bubble_sort(alist):
#     for j in range(len(alist)-1,0,-1):
#         for i in range(j):
#             if alist[i]>alist[i+1]:
#                 alist[i],alist[i+1]=alist[i+1],alist[i]
# li=[1,3,2,5,4]
# bubble_sort(li)
# print(li)

# def pai(a):
#     for x in range(len(a)-1,0,-1):
#         for z in range(x):
#             if a[z]>a[z+1]:
#                 a[z],a[z+1]=a[z+1],a[z]
# q=[1,3,2,5,4]
# pai(q)
# print(q)

# def pai(a):
#     for x in range(len(a)-1,0,-1):
#         for i in range(x):
#             if a[i]>a[i+1]:
#                 a[i],a[i+1]=a[i+1],a[i]
# w=[1,3,2,5,4]
# pai(w)
# print(w)

# def pai(a):
#     for x in range(len(a)-1):
#         for q in range(len(a)-1-x):
#             if a[q]>a[q+1]:
#                 a[q],a[q+1]=a[q+1],a[q]
# w=[1,3,2,5,4]
# pai(w)
# print(w)

# a=1
# b=2
# # a=b
# # b=a
# a,b=b,a
# print(a,b)

# a=[1,3,2,5,4]
# for y in range(len(a)-1,0,-1):
#     for x in range(y):
#         if a[x]>a[x+1]:
#             a[x+1],a[x]=a[x],a[x+1]
# print(a)

# a=[1,3,2,5,4]
# for x in range(len(a)-1):
#     for y in range(len(a)-1-x):
#         if a[y]>a[y+1]:
#             a[y],a[y+1]=a[y+1],a[y]
# print(a)

a=[1,2,3,4,5]
# for x in range(len(a)-1,0,-1):
#     for i in range(x):
#         if a[i]>a[i+1]:
#             a[i],a[i+1]=a[i+1],a[i]
# print(a)
for x in range(len(a)-1):
    for i in range(len(a)-1-x):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1].a[i]
print(a)

