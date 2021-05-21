class Master(object):
    def __init__(self):
        self.peifang='古法煎饼果子配方'
    def make_cake(self):
        print('按照%s制作了一份煎饼果子'%self.peifang)

class School(Master):
    def __init__(self):
        self.peifang='现代煎饼果子配方'
    def make_cake(self):
        print('按照%s制作了一份煎饼果子'%self.peifang)
        super(School, self).__init__()
        super(School, self).make_cake()
    def cook(self):
        print('鱼香肉丝')

class Prentice(School):    #多个父类实例方法重名时只继承第一个的方法，不重名的都继承
    def __init__(self):
        self.__money=1000
        self.peifang='猫氏煎饼果子配方'
    def make_cake(self):
        print('按照%s制作了一份煎饼果子'%self.peifang)
    def __setter(self):
        print(self.__money)
    def diao(self):
        self.__setter()
    def make_all_cake(self):
        self.make_cake()
        super(Prentice, self).__init__()
        super(Prentice, self).make_cake()

class PrenticePrentice(Prentice):
    __money=10
    a=1
    def __init__(self):
        pass
    @classmethod
    def gai(cls):
        cls.a=2
        cls.__money=100
    def shu(self):
        print(self.__money)
prentice=PrenticePrentice()
# prentice.gai()
# print(PrenticePrentice.a)
# prentice.shu()
# prentice.__setter()
q=Prentice()
q.diao()
# prentice.diao()

