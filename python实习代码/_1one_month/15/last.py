class A(object):
    b=2
    def __init__(self):
        self.a=1
    @classmethod
    def q(cls):
        cls.b=3
    @staticmethod
    def w():
        A.b=3
        A.a=4
z=A()
print(A.b)
z.q()
print(A.b)
print(z.a)
z.w()
print(z.b)
print(z.a)
print(A.a)