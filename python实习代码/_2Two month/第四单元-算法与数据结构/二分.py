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
#
# a=[1,2,3,4,5,6]
# print(cha(a,3))

# def cha(a,item):
#     first=0
#     last=len(a)-1
#     while first<=last:
#         x = (last + first)//2
#         if item==a[x]:
#             return True
#         elif item>a[x]:
#             first=x+1
#         else:
#             last=x-1
#     return False
# print(cha([1],1))

# print(1//2)

# def cha(a,item):
#     first = 0
#     last = len(a) - 1
#     while first <= last:
#         x = (first + last) // 2
#         if a[x] == item:
#             return True
#         elif item > a[x]:
#             first = x + 1
#         else:
#             last = x - 1
#     return False

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
# print(cha([1,2,3],3))


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
# print(cha([1,2,3],4))


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
#         x=(last+first)//2
#         if a[x]==item:
#             return True
#         elif item>a[x]:
#             first=x+1
#         else:
#             last=x-1
#     return False
#
# a=[1,3,2,5,4]
# a.sort()
# print(cha(a,4))


# a=[1,2,3,4,5]
#
# def cha(a,item):
#     f=0
#     s=len(a)-1
#     while f<s:




# def cha(a,item):
#     if len(a)==0:
#         return False
#     else:
#         x=len(a)//2
#         if a[x]==item:
#             return True
#         elif item>a[x]:
#             return cha(a[x+1:],item)
#         else:
#             return cha(a[:x],item)

# print(cha(a,5))












