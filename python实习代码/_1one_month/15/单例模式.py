# class Singleton(object):
#     __a=None
#     __first=True
#     def __new__(cls,age):
#         if cls.__a is None:
#             cls.__a=object.__new__(cls)
#         return cls.__a
#     def __init__(self,age):
#         if self.__first:
#             self.age=age
#             self.__first=False
# a=Singleton(18)
# b=Singleton(19)
# print(a.age,b.age)


# class jing(object):
#     __pan=None
#     __first=True
#     def  __new__(cls, *args, **kwargs):
#         if cls.__pan==None:
#             cls.__pan=object.__new__(cls)
#           return cls.__pan
#     def __init__(self,age):
#         if self.__first==True:
#             self.age = age
#             self.__first=False
# a=jing(18)
# print(a.age)
# b=jing(1)
# print(a.age)


class F(object):
    __a=None
    __b=True
    def __new__(cls, *args, **kwargs):
        if cls.__a is None:
            cls.__a=object.__new__(cls)
        return cls.__a
    def __init__(self,age,score):
        # if self.__b:
            self.age = age
            self.score = score
            # self.__b=False

f1=F(1,2)
f2=F(3,4)
print(f1.age,f1.score)
print(f2.age,f2.score)






