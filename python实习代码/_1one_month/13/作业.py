'''
自定义Fish鱼类，要求含有三个属性和两个方法，并创建测试类给属性赋值调用方法
	属性name姓名,weight重量,price价格  
	方法show方法打印所有属性，num计算weight和price的总价	
2	自定义Bird鸟类，要求含有三个属性和两个方法，并创建测试类给属性赋值调用方法	
	属性kind品种,weight重量,sex性别 
	方法show打印所有属性 ,fly方法
3	自定义Car汽车类，要求含有三个属性和两个方法，并创建测试类给属性赋值调用方法	
	属性color 颜色,speed速度,brand品牌 
	方法show打印所有属性，sudu打印我的速度很快
4	自定义Computer电脑类，要求含有三个属性和两个方法，并创建测试类给属性赋值调用方法
	属性 brand品牌,size尺寸,price 价格
	方法show 显示基本信息,play方法“买电脑打代码”
5	定义cirlc圆形类，定义半径r;定义两个方法求面积，求周长; 并创建测试类给属性赋值调用方法
6	定义一个类：MyString，它包含：
1个实例属性：mystr用户由键盘随机输入一个英文字符串（只包含英文字母和空	格），如：”I am a student”，将该值作为MyString类__init__方法的一个参数传入，并	赋给类的实例属性mystr
6个实例方法：
1）show_counts()
打印出字符串总字符数（包括空格），如：如果属性mystr为”I am a student”，则输	出14
2）show_char_counts()
打印出打印出字符串包含英文字母的个数（不包括空格），如：如果属性mystr为”I 	am a student”，则输出11
3）show_cap()
将字符串中英文字母全部转换成大写并输出
4）show_word_counts()
统计字符串中单词的个数并输出，如：如果属性mystr为”I am a student”，则输出4
5）判断show_last_word_len()
计算字符串中最后一个单词的长度，如：如果属性mystr为”I am a student”，则输出7
6）show_long_word()
找到字符串中长度最长的单词并输出，如：如果属性mystr为”I am a student”，则输	出	“student”
'''



# class Mystring(object):
#     def __init__(self,mystr):
#         self.mystr=mystr
#     def show_counts(self):
#         print(len(mystr))
#
#     def show_char_counts(self):
#         a=mystr.replace(" ",'')
#         print(len(a))
#
#     def show_cap(self):
#         print(mystr.upper())
#
#     def show_word_counts(self):
#         q=mystr.split(" ")
#         print(len(q))
#
#     def show_last_word_len(self):
#         z=mystr.split(" ")
#         print(len(z[-1]))
#
#     def show_long_word(self):
#         w=mystr.split(" ")
#         e=[]
#         for x in w:
#            e.append(len(x))
#         for x in w:
#             if len(x)==max(e):
#                 print(x)
#
#     def show(self):
#         print(self.mystr)
#
# while True:
#     mystr = input("请输入：")
#     a=mystr.replace(" ",'')
#     if a.isalpha() or mystr.isspace():
#         mystring = Mystring(mystr)
#         mystring.show()
#         mystring.show_counts()
#         mystring.show_char_counts()
#         mystring.show_cap()
#         mystring.show_word_counts()
#         mystring.show_last_word_len()
#         mystring.show_long_word()
#         break


# class Cirlc(object):
#     def __init__(self):
#         self.r=10
#     def s(self):
#         print(3.14*self.r**2)
#     def c(self):
#         print(2*self.r*3.14)
# cirlc=Cirlc()
# cirlc.s()
# cirlc.c()


# class Computer(object):
#     def __init__(self):
#         self.kind='联想'
#         self.size=15.6
#         self.price=6699
#     def show(self):
#         print(self.kind,self.size,self.price)
#     def play(self):
#         print('买电脑打代码')
# computer=Computer()
# computer.play()
# computer.show()



# class Cat(object):
#     def __init__(self):
#         self.color='黑色'
#         self.speed=100
#         self.brand='老虎'
#     def show(self):
#         print(self.color,self.speed,self.brand)
#     def sudu(self):
#         print('我的速度很快')
# cat=Cat()
# cat.show()
# cat.sudu()



# class Bird(object):
#     def __init__(self,kind,weight,sex):
#         self.kind=kind
#         self.weight=weight
#         self.sex=sex
#     def show(self):
#         print(self.kind,self.weight,self.sex)
# bird=Bird('喜鹊',20,'女')
# bird.show()

# class Fish(object):
#     def __init__(self):
#         self.name='鲨鱼'
#         self.weight=100
#         self.price=20000
#     def show(self):
#         print(self.name,self.weight,self.price)
# fish=Fish()
# fish.show()

















