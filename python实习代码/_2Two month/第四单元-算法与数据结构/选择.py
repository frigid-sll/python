# a=[1,3,2,5,4]
# for x in range(len(a)-1):
#     minn=x
#     for y in range(x+1,len(a)):
#         if a[minn]>a[y]:
#             minn=y
#     if minn!=x:
#         a[x], a[minn] = a[minn], a[x]
# print(a)



# a=[1,3,2,5,4]
# for x in range(len(a)-1):
#     minn=x
#     for i in range(x+1,len(a)-1):
#         if a[minn]>a[i]:
#             minn=i
#     if minn!=x:
#         a[minn],a[x]=a[x],a[minn]
# print(a)

# def cha(a,item):
#
#     if len(a)==0:
#         return False
#     else:
#          x=len(a)//2
#         if item == a[x]:
#             return True
#         elif item > a[x]:
#             return cha(a[x+1:], item)
#         else:
#             return cha(a[:x], item)
#
# a=[1,3,2,5,4]
# a.sort()
# print(cha(a,6))


# def s(a,item):
#     first=0
#     last=len(a)-1
#     while first<=last:
#         x=(first+last)//2
#         if a[x]==item:
#             return True
#         elif a[x]>item:
#             last = x - 1
#         else:
#             first=x+1
#     return False
# print(s([1,2,3,4,5],6))


# a=[1,3,2,5,4]
# for x in range(len(a)-1):
#     minn=x
#     for i in range(x+1,len(a)):
#         if a[minn]>a[i]:
#             minn=i
#     if minn!=x:
#         a[minn],a[x]=a[x],a[minn]
# print(a)

# a=[1,3,2,5,4]
# for x in range(len(a)-1):
#     minn=x
#     for i in range(x+1,len(a)):
#         if a[minn]>a[i]:
#             minn=i
#     if minn!=x:
#         a[minn],a[x]=a[x],a[minn]
# print(a)

a=[1,3,2,5,4]
for x in range(len(a)-1):
    minn=x
    for i in range(x+1,len(a)):
        if a[minn]>a[i]:
            minn=i
    if minn!=x:
        a[minn],a[x]=a[x],a[minn]
print(a)


