# class lei(object):
#     '''文档说明'''
#     def __init__(self,name,age):
#         print('_init_方法被调用')
#         self.name=name
#         self.age=age
#     def shu(self):
#         print(self.name)
#     def __str__(self):
#         return'姓名是：%s,年龄是：%s'%(self.name,self.age)
#     def __del__(self):
#         print('_del_方法被调用')
#         print('对象被干掉了')
# dui=lei('冲击之刃',20)
# dui1=dui
# dui2=dui
# dui3=dui
# # print(dui)
# # print(dui.__doc__)
# print('%d被删除'%id(dui))
# del(dui)
# print('%d被删除'%id(dui1))
# del(dui1)
# print('%d被删除'%id(dui2))
# del(dui2)

#烤地瓜
# class gua(object):
#     def __init__(self):
#         self.a=0
#         self.b='生的'
#         self.condiment=[]
#     def kao(self,time):
#         self.a+=time
#         if self.a>8:
#             self.b='焦的'
#         elif self.a>5:
#             self.b='熟的'
#         elif self.a>3:
#             self.b='半生不熟的'
#         else:
#             self.b='生的'
#     def add(self,q):
#         self.condiment.append(q)
#         digua=self.b+'地瓜'
#         digua+='('
#         for a,x in enumerate(self.condiment):
#             if a<len(self.condiment)-1:
#                 digua =digua+ x+','
#             else:
#                 digua+=x
#         digua+=')'
#         print(digua)
# di=gua()
# di.kao(1)
# print(di.b)
# di.kao(3)
# print(di.b)
# di.kao(3)
# print(di.b)
# di.kao(2)
# print(di.b)
# di.add('咸味的')
# di.add('甜的')

class kao(object):
    def __init__(self):
        self.time=0
        self.c=''
        self.liao=[]
    def hot(self,n):
        self.time+=n
        if self.time>8:
            selc.c='焦的'
            print('焦的')
        elif self.time>5:
            self.c='熟的'
            print('熟的')
        elif self.time>3:
            self.c='半生不熟的'
            print('半生不熟的')
        else:
            self.c='生的'
            print('生的')
    def add(self,a):
        self.liao.append(a)
        z=''
        z = self.c + '地瓜'
        z+='('
        for q,w in enumerate(self.liao):
            if q < len(self.liao) - 1:
                z = z + w + ','
            else:
                z += w
        z+=')'
        print(z)
gua=kao()
gua.hot(1)
gua.hot(3)
gua.add('番茄味')
gua.add('咸的')




