class Hero(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def moving(self):
        print('正在赶往战场')
    def attact(self):
        print('大保健...')
if __name__ == '__main__':      #程序入口
    f = Hero('黄忠', 18)
    f2 = f  # 引用计数+1
    f3 = f  # +1
    print(id(f))
    print(id(f2))
    print(id(f3))
    del (f2)  # -1
    # print(f2)
    del (f3)  # -1
    print(id(f3))

