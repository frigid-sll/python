#选择排序：
#选择排序是一种简单直观的排序方法
#工作原理：
#首先在末排序序列中找到最小（大）元素，存放到排序序列的起始位置
#然后，再从剩余末排元素中继续寻找最小（大）元素，
#然后放到已排序序列的末尾
#以此类推，直到所有元素军排序完毕

#选择排序的主要优点与数据移动有关。如果某个元素位于正确的最终位置上
#则他不会北移动。选择排序每次交换一对元素，他们当中至少有一个将被
#移到其最终位置上，因此对n个元素的表进行排序总共进行至多n-1次交换。
#在所以所有的完全依靠交换区移动元素的排序方法中，选择排序属于非常好的一种

# def select_sort(alist):
#     n=len(alist)
#     #需要进行n-1次选择操作
#     for i in range(n-1):
#         min_index=i
#         #从i+1位置到末尾选择出最小数据
#         for j in range(i+1,n):
#             if alist[j]<alist[min_index]:
#                 min_index=j
#         #如果选择出的数据不再正确位置，进行交换
#         if min_index!=i:
#             alist[i],alist[min_index]=alist[min_index],alist[i]
# alist=[1,4,3,5,2]
# select_sort(alist)
# print(alist)

# def pai(a):
#     for x in range(len(a)-1):
#         minn=x
#         for y in range(x+1,len(a)):
#             if a[minn]>a[y]:
#                 minn=y
#         a[x],a[minn]=a[minn],a[x]
# alist=[1,3,2,5,4]
# pai(alist)
# print(alist)

list=[1,3,2,5,4]
for x in range(len(list)-1):
    minn = x
    for i in range(x+1,len(list)-1):
        if list[minn]>list[i]:
            minn=i
    if minn!=x:
        list[minn],list[x]=list[x],list[minn]
print(list)
