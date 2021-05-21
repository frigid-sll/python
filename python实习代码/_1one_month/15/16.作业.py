'''
定义一个类：MyNum，它包含：
1个实例属性：num用户由键盘随机输入一个正整数数字，如：100，
将该值作为	MyNum类__init__方法的一个参数传入，并赋给类的实例属性num
12个实例方法：
1）show_num()
打印从1到属性num之间所有的数字，
如：如果属性num为100，则打印“1 2 3 	4 ...99 100”
2）calc_sum()
计算从1-num之间所有数字的和并输出，
如：如果属性num的值为100，则计算	1+2+3+...+99+100的值
3）calc_odd_sum()
计算从1-num之间所有奇数的和并输出，
如：如果属性num的值为100，则计算	1+3+5+7+...+99的值
4）calc_even_sum()
计算从1-num之间所有偶数的和并输出，
如：如果属性num的值为100，则计算	2+4+6+8+...+100的值
5）show_num_div()
打印出从1-num之间所有能被7整除的数或者包含7的数字,如果找到了输出 
例：“找到了 7 ， 过”，如果未找到不用输出
6）check_num()
判断num是否是回文数（即是给定一个数，这个数顺读和逆读都是一样的）并输出	判断结果，
如：如果属性num的值为101，则输出“101是回文数”；
如果属性	num的值为123，则输出	“123不是回文数”
7）show_sanjiao()
打印倒三角demo（使用至少三种方法实现）
8）replace_item()
my_list = [1,2,3,4,5]   交换相邻元素，索引为奇数和索引为偶数位置元素    ----》 my_list = [2,1,4,3,5]
(要求使用两种方法完成)
9) isleap()
打印1998--2200年之间的所有闰年（能被4整除但不能被100整除，或者能被400整除的年份）
10）定义方法
使用两种方法实现99乘法表的输出
11）封装方法实现
倒着打印99乘法表
12)封装一个方法实现模拟演示两个玩家之间的猜拳游戏
'''

# class MyNum(object):
#     def __init__(self,num):
#         self.num=num
#     def show_num(self):
#         print(','.join(['%s'%x for x in range(1,self.num+1)]))
#     def calc_sum(self):
#         print(sum([x for x in range(1,(self.num+1))]))
#     def calc_odd_sum(self):
#         print(sum([x for x in range(1,(self.num+1)) if x%2==1]))
#     def calc_even_sum(self):
#         print(sum([x for x in range(1,(self.num+1)) if x%2==0]))
#     def check_num(self):
#         if str(self.num)==str(self.num)[::-1]:
#             print('%d是回文数'%self.num)
#         else:
#             print('%d不是回文数'%self.num)
#     def show_num_div(self):
#         print(','.join(['%s'%x for x in range(1,self.num+1) if (x%7==0 or ('7' in str(x)))]))
#     def show_sanjiao(self):
#         print('\n'.join(['*'*x for x in range(5,0,-1)]))
#     def replace_item(self):
#         mylist,l=[1,2,3,4,5],[]
#         for x in mylist:
#             l.append(x)
#         for a in range(len(mylist)):
#             if a%2==0:
#                 if a==len(mylist)-1:
#                     pass
#                 else:
#                     mylist[a]=l[a+1]
#             else:
#                 mylist[a]=l[a-1]
#         print(mylist)
#     def isleap(self):
#         print(','.join(['%s' % x for x in range(1998, 2201) if (x % 4 == 0 and x%100!=0 or x%400==0)]))
#     def zheng(self):
#         print('\n'.join([' '.join(['%d*%d=%d'%(x,y,x*y) for x in range(1,1+y)]) for y in range(1,10)]))
#     def dao(self):
#         print('\n'.join([' '.join(['%d*%d=%d'%(x,y,x*y) for x in range(1,1+y)]) for y in range(9,0,-1)]))
#     def cai(self):
#         a=int(input("请输入第一个玩家出的拳法： 1、拳头 2、剪刀 3、布 ："))
#         b=int(input("请输入第二个玩家出的拳法： 1、拳头 2、剪刀 3、布 ："))
#         if (a<=3 and a>=1) and (b<=3 and b>=0):
#             if a == b:
#                 print('平局')
#             elif (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
#                 print('玩家一赢了')
#             else:
#                 print('玩家二赢了')
#         else:
#             print("输入的拳法错误")
#
# f = MyNum(int(input("请输入：")))
# print('1、打印从1到属性num之间所有的数字，')
# f.show_num()
# print('2、计算从1-num之间所有数字的和并输出，')
# f.calc_sum()
# print('3、计算从1-num之间所有奇数的和并输出，')
# f.calc_odd_sum()
# print('4、计算从1-num之间所有偶数的和并输出，')
# f.calc_even_sum()
# print('5、打印出从1-num之间所有能被7整除的数或者包含7的数字,如果找到了输出 ')
# f.show_num_div()
# print('6、判断num是否是回文数（即是给定一个数，这个数顺读和逆读都是一样的）并输出	判断结果，')
# f.check_num()
# print('7、打印倒三角demo（使用至少三种方法实现）')
# f.show_sanjiao()
# print('8、交换相邻元素，索引为奇数和索引为偶数位置元素')
# f.replace_item()
# print('9、打印1998--2200年之间的所有闰年（能被4整除但不能被100整除，或者能被400整除的年份）')
# f.isleap()
# print('10、使用两种方法实现99乘法表的输出')
# f.zheng()
# print('11、倒着打印99乘法表')
# f.dao()
# print('12、封装一个方法实现模拟演示两个玩家之间的猜拳游戏')
# f.cai()



# for x in range(9,0,-1):
#     for y in range(1,1+x):
#         print('%d*%d=%d '%(x,y,x*y),end='')
#     print()






