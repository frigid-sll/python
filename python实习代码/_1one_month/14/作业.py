'''
1	创建父类Dog，含有两个属性，两个实例方法（run，eat）。
	创建子类Hashiqi，重写父类的方法。
其中创建父类对象分别调用父类的两个方法。	
之后创建子类对象，并依次调用其属性和方法。分别展示效果
2	创建猫类，含有属性：姓名，年龄，方法：捉老鼠。
	创建狗类，含有属性：姓名，年龄，方法：玩球，捉老鼠。
	以上两个类有其共同父类：动物类，含有属性：姓名，年龄，方法：玩球，捉老鼠。
分别实例化两个子类对象，调用并输出父类同名属性和方法。
3	创建教师类，含有属性：姓名，年龄，课程，方法：吃。
	创建学生类，含有属性：姓	名，年龄，班级，方法：学习，吃。
	通过描述，创建出一个父类Teacher类，创建出一个学生类，学生类继承自Teacher类，
使用学生类实例化出来的对象分别调用父类的同名属性和方法。
4	定义一个类：Person，它用来表示一个人，它包含：
2个实例属性：name和age（分别表示一个人的姓名和年龄）
用户由键盘随机输入一个字符串和正整数数字，将输入的这两个值作为Person类	__init__方法的两个参数传入，并赋给类的实例属性name和age
'''
'''
5个实例方法：
1）show_my_info()
格式化打印出“我是xx，今年xx岁”，姓名和年龄由属性name和age提供
2）show_my_birth()
打印出我是哪一年出生的，比如今年是2018年，age是10岁，那么可得知我是2008	年出生的，输出“我是2008年出生”
3）show_my_life()
打印我的成长历程，比如如果我是2008年出生，今年10岁，则打印出类似如下结	果：
2008年 出生
2009年 1岁 
...
2018年 10岁
4）show_leap_year()
判断从我出生那一年到今年（2018年），是否含有闰年（能被4整除但不能被100整	除，或者能被400整除的年份），如果有，打印出全部闰年，如果没有，则打印“没	有闰年”
5）can_recite()
表示我能背诵九九乘法表，打印出9*9乘法表
'''

# class Person(object):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def show_my_info(self):
#         print('我是%s,今年%d岁'%(self.name,self.age))
#     def show_my_birth(self):
#         print('\n我是%d年出生的\n'%(2018-self.age))
#     def show_my_life(self):
#         for x in range(self.age+1):
#             if x==0:
#                 print('%d年 出生'%(2018-self.age))
#             else:
#                 print('%d年 %d岁'%((2018-self.age+x),x))
#     def show_leap_year(self):
#         num=[]
#         for x in range((2018-self.age),2019):
#             if x%4==0 and x%100!=0 or x%400==0:
#                 num.append(x)
#         if len(num)==0:
#             print('没有闰年')
#         else:
#             print('闰年有：')
#             for x in num:
#                 print('%d '%x,end='')
#     def can_recite(self):
#         print('\n我会背诵九九乘法表\n')
#         print('\n'.join([' '.join(['%d*%d=%d'%(x,y,x*y) for x in range(1,1+y)]) for y in range(1,10)]))
# name=input("请输入姓名：")
# age=int(input("请输入年龄："))
# person=Person(name,age)
# person.show_my_info()
# person.show_my_birth()
# person.show_my_life()
# person.show_leap_year()
# person.can_recite()




# class Teacher(object):
#      name='王老师'
#      age=18
#      study='人工智能'
#      def eat(self):
#          print('吃')
# class Student(Teacher):
#     name='师玲珑'
#     age=18
#     jiaoshi='1809A'
#     def study(self):
#         print('学习')
#     def eat(self):
#         print('吃2')
# student=Student()
# student.eat()
# print(student.name,student.age)



# class animal(object):
#     name='动物'
#     age=10
#     def play(self):
#         print('玩球1')
#     def run(self):
#         print('捉老鼠1')
#
# class Cat(animal):
#     name='小猫'
#     age=2
#     def run(self):
#         print('捉老鼠2')
# class Dog(animal):
#     name='大黄'
#     age=3
#     def play(self):
#         print('玩球3')
#     def run(self):
#         print('捉老鼠3')
# cat=Cat()
# print(cat.name,cat.age)
# cat.run()
# dog=Dog()
# print(dog.name,dog.age)
# dog.run()
# dog.play()



# class Dog(object):
#     name='大黄'
#     age=3
#     def run(self):
#         print('正在跑')
#     def eat(self):
#         print('正在吃饭')
# class Hashiqi(Dog):
#     def run(self):
#         print('儿子正在跑')
#     def eat(self):
#         print('儿子正在吃饭')
# dog=Dog()
# dog.run()
# dog.eat()
# son=Hashiqi()
# son.eat()
# son.run()
# print(son.name)
# print(son.age)

'''
1	创建类，Person，含有类的私有属性 __country为China，实例方法：eat，输出吃饭；	实例方法：run，输出“跑步”；创建其子类：Student，含有实例方法：study，“学习使我	快乐”。调用，并分别输出
'''
# class Person(object):
#     def __init__(self):
#         self.__country='China'
#     def eat(self):
#         print('吃饭')
#     def run(self):
#         print('跑步')
# class Student(Person):
#     def study(self):
#         print("学习使我快乐")
# student=Student()
# student.run()
# student.eat()
# student.study()



'''
2	创建类，Person，含有私有实例属性 __address为“北京”，实例方法：eat，输出吃饭；	实例方法：run，输出“跑步”在类内创建调用私有属性的getter方法和修改实例属性的	
	setter方法，创建实例对象分别调用输出以上方法；创建其子类：Student，含有实例方	法：study，“学习使我	快乐”。调用，并分别输出
'''
# class Person(object):
#     def __init__(self):
#         self.__address='北京'
#     def eat(self):
#         print('吃饭')
#     def run(self):
#         print('跑步')
#     def getter(self):
#         print(self.__address)
#     def setter(self):
#         self.__address='上海'
#         print(self.__address)
# person=Person()
# person.eat()
# person.run()
# person.getter()
# person.setter()
# class Student(Person):
#     def study(self):
#         print('学习使我快乐')
# student=Student()
# student.study()


'''
3	定义一个类：MyYear，它包含：
1个实例属性：year用户由键盘随机输入一个年份，如：2018，将该值作为MyYear	类__init__方法的一个参数传入，并赋给类的实例属性year
4个实例方法：
1)show_season()
打印该年所有月份，并显示所属季节，如：“1月 冬季 2月 冬季 3月 春季”等
2)isleap()
打印该年是否是闰年（能被4整除但不能被100整除，或者能被400整除的年份），	如：如果属性year的值为2018，则输出：“2018年不是闰年”
3)year_sum()
打印从1到该年所在数字之间所有整数的和，如：如果属性year的值为2018，则计	算1+2+3+4+5+...+2018的值并输出结果。
4)check_num()
判断该年所在数字是否是回文数（即是给定一个数，这个数顺读和逆读都是一样的）并输出判断	结果，如：如果属性year的值为2002，则输出“2002是回文数”；如果属性year的值为2018，	则输出“2018不是回文数”。
'''
# class MyYear(object):
#     def __init__(self,year):
#         self.year=year
#     def show_season(self):
#         for x in range(1,13):
#             if x<3:
#                 print('%d月 冬季 '%x,end='')
#             elif x<6:
#                 print('%d月 春季 ' % x, end='')
#             elif x < 9:
#                 print('%d月 夏季 ' % x, end='')
#             elif x<12:
#                 print('%d月 秋季 ' % x, end='')
#             else:
#                 print('%d月 冬季 ' % x, end='')
#     def isleap(self):
#         if self.year%4==0 and self.year%100!=0 or self.year%400==0:
#             print('\n%d是闰年'%self.year)
#         else:
#             print('\n%d不是闰年'%self.year)
#     def year_sum(self):
#         sum=0
#         for x in range(self.year):
#             sum+=x
#         print(sum)
#     def chock_num(self):
#         a=str(self.year)
#         if a==a[::-1]:
#             print('%d是回文数'%self.year)
#         else:
#             print('%d不是回文数' % self.year)
# year=int(input("请输入年份:"))
# my=MyYear(year)
# my.show_season()
# my.isleap()
# my.year_sum()
# my.chock_num()
'''
4	定义一个类：MyString，它包含：
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
#         print(len(self.mystr))
#     def show_char_counts(self):
#         q=self.mystr.replace(' ','')
#         print(len(q))
#     def show_cap(self):
#         q=self.mystr.upper()
#         print(q)
#     def show_word_counts(self):
#         q=self.mystr.split(' ')
#         print(len(q))
#     def show_last_word_len(self):
#         q=self.mystr.split(" ")
#         print(len(q[-1]))
#     def show_long_word(self):
#         q=self.mystr.split(" ")
#         w=[]
#         for x in q:
#             w.append(len(x))
#         for x in q:
#             if len(x)==max(w):
#                 print(x)
# while True:
#     word=input("请输入：")
#     s=word.replace(' ','')
#     if s.isalpha() or word.isspace():
#         mystring=Mystring(word)
#         mystring.show_counts()
#         mystring.show_char_counts()
#         mystring.show_cap()
#         mystring.show_word_counts()
#         mystring.show_last_word_len()
#         mystring.show_long_word()
#         break




'''
5	定义一个类：MyNum，它包含：
1个实例属性：num用户由键盘随机输入一个正整数数字，如：100，将该值作为	MyNum类__init__方法的一个参数传入，并赋给类的实例属性num

6个实例方法：
1）show_num()
打印从1到属性num之间所有的数字，如：如果属性num为100，则打印“1 2 3 	4 ...99 100”
2）calc_sum()
计算从1-num之间所有数字的和并输出，如：如果属性num的值为100，则计算	1+2+3+...+99+100的值
3）calc_odd_sum()
计算从1-num之间所有奇数的和并输出，如：如果属性num的值为100，则计算	1+3+5+7+...+99的值
4）calc_even_sum()
计算从1-num之间所有偶数的和并输出，如：如果属性num的值为100，则计算	2+4+6+8+...+100的值
5）show_num_div()
打印出从1-num之间所有能被7整除的数
6）check_num()
判断num是否是回文数（即是给定一个数，这个数顺读和逆读都是一样的）并输出	判断结果，	如：如果属性num的值为101，则输出“101是回文数”；如果属性	num的值为123，则输出	“123不是回文数”'''

class Mysum(object):
    def __init__(self,num):
        self.num=num
    def show_num(self):
        for x in range(1,self.num+1):
            print('%d '%x,end='')
    def calc_sum(self):
        sum=0
        for x in range(self.num+1):
            sum+=x
        print(sum)
    def calc_odd_sum(self):
        sum2=0
        for x in range(self.num+1):
            if x%2==1:
                sum2+=x
        print(sum2)
    def calc_aven_sum(self):
        sum3=0
        for x in range(self.num+1):
            if x %2==0:
                sum3+=x
        print(sum3)
    def show_num_div(self):
        for x in range(1,self.num+1):
            if x %7==0:
                print('%d '%x,end='')
    def check_num(self):
        self.num=str(self.num)
        if self.num==self.num[::-1]:
            print('是回文数')
        else:
            print("不是回文数")
num=int(input("请输入:"))

my=Mysum(num)
my.show_num()
my.calc_sum()
my.calc_odd_sum()
my.calc_aven_sum()
my.show_num_div()
my.check_num()


