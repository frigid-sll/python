#re.match() 能够匹配出以xxx开头的字符串
import re
#正则表达式： 首先要引入re函数  import re
#就是  f=re.match('你要查找的字符串里的内容给出条件','字符串')
#输出时  print(f.group()) 才能输出你找的内容
#字符           功能
#  .            匹配任意一个字符（除了\n)
# []            匹配[]中列举的字符          如[0-9]表示0-9  [0-9a-z_]表示0-9，a-z,和下划线
#\d             匹配数字  即0-9
#\D             匹配非数字
#\s             匹配空白 即空白，tab键
#\S             匹配非空白
#\w             匹配单词字符，即a-z,A-Z,0-9,_
#\W             匹配非单词字符  例如:@ # $ ， 。 .
#上面这些一个只能匹配一个字符  匹配多个就要重复写  例如要匹配出123就要写\d\d\d
# f=re.match('\d\d\d','1234')
# print(f.group())

#用下面这种方法即可不用重复写同样的类型
# 字符         功能
# *             匹配前一个字符出现0次或者无限次，即可有可无
# +             匹配签一个字符出现1次或者无限次，即至少有一次
# ？            匹配前一个字符出现1次或者0次，即要么有1次，要么有0次
#{m}            匹配前一个字符出现m次
#{m,n}          匹配前一个字符出现从m次到n次
#上面的方法就可以这样写：
# f=re.match('\d{3}','123456')
# print(f.group())

#匹配开头结尾
#字符     功能
# ^         匹配字符串开头
# $         匹配字符串结尾

# import os
# os.rename('1.py','正则表达式.py')

#例如：
# 匹配出开头是html结尾是.com的字符串
# a=['html:baidu@.com','html:123@.sdr','httlbaidu@.com']
# import re
# for x in a:
#     f=re.match('^html.[\w]+[\W].com$',x)
#     if f:
#         print(f.group())
#     else:
#         print('错误')

# import re
# f=re.match('^html[\W]+[\w]*.com$','html://123.com')
# print(f.group())




# a=['html123.com','html123am','123com']
# for x in a:
#     f=re.match('^html[\w]*.[\w]*am$',x)
#     if f:
#         print(f.group())
#     else:
#         print('错误')
# 当你要查找字符串时 必须前面的查找完了也就是有对应的匹配方式，后面的才能匹配，否则报错

#匹配分组
#字符         功能
# |            匹配左右任意一个表达式  如果 左边的表达式式是错误的可以匹配右边的  两边都正确用左边的
#(ab|c)        将括号中的字符作为一个分组  找满足其中任意一个
# 例如
#再找以什么结尾时前面的字符必须全部有对应的匹配方式  不然会报错
# f=re.match('[1-9]\d$','088')
# print(f.group())  #这个会报错  因为 用到了$  以什么结尾  前面的字符没有匹配到
# f=re.match('[1-9]\d$|\d*\d$','088')
# print(f.group())        #左边表达式错误的  即用右边的


#分组：
# f=re.match('(1|2)','12')
# print(f.group())   #左边的为先







# ret = re.match("[1-9]?\d$|0(1|8)","08")
# print(ret.group())  # 不是0-100之间



# list=['123456','123asd','12567']
# for x in list:
#     f=re.match('^12\w+?$',x)    #寻找以12开头，7结尾的字符串
#     if f:
#         print(f.group())
#     else:
#         print('错误')
#. 匹配任意一个字符（除了\n)
#[]匹配[]中列举的字符
#\d匹配数字 即0-9
#\D匹配非数字
#\s匹配空白  即空格 tab键
#\S匹配非空白
#\w匹配单词字符 即a-z,A-Z,0-9,_
#\W匹配非单词字符



# import re
# tel=input('请输入你的手机号：')
# f=re.match('[\d]{10}[\d]$',tel)
# print(f.group())


# a='abc,cn'
# import re
# f=re.match('abc',a)
# print(f.group())
# import re
# f=re.match('<[\S]..','<\.html>')
# if f:
#     print(f.group())
# else:
#     print('loser')



# import re
# f=re.match('two\d','two12')
# if f:
#     print(f.group())
# else:
#     print('匹配失败')


# import re
# f=re.match('tw\D','two),')
# if f:
#     print(f.group())
# else:
#     print('匹配失败')

# import re
# f=re.match(r'wt\.[\W]+','wt.\+')
# if f:
#     print(f.group())
# else:
#     print('匹配失败')


# import re
# f=re.match('tc{3,}p','tcccp')  #至少匹配3次
# if f :
#     print(f.group())
# else:
#     print('匹配失败')

# f2=re.match('c{,3}','cccc')  #至多三次
# if f2:
#     print(f2.group())
# else:
#     print('匹配失败')


# \.表示的是.这个符号


# import re
# f=re.match('^1[3-9]\d{9}$','13146152021')
# if f:
#     print(f.group())
# else:
#     print('匹配失败')

# import re
# f=re.match('^1[3-9]\d{8}[^47]$','13146152021')
# if f:
#     print(f.group())
# else:
#     print('匹配失败')
#
# f2=re.match('^1[3-9]\d{8}[^47]$','12345678994')
# if f2:
#     print(f2.group())
# else:
#     print('匹配失败')

# ^放在前面是判断以。。开始，放在[]里是不以


# import re
# email_list=['xiaowang@163.com','xiaowang@163.comheihei','com.xiaowang@']
# f=map(lambda x:)

# for email in email_list:
#     ret=re.match('[\w]{4,20}@163\.com$',email)
#     if ret:
#         print(ret.group())
#     else:
#         print('不符合要求')


# import re
# f=re.match('[\w]{4,20}@(163|qq)\.(com)$','2522908520@163.com')
# if f:
#     print(f.group())
# else:
#     print('匹配失败')


# import re
# f=re.match('^(https://www)\..+(\.com)$','https://www.baidu.com')
# if f:
#     print(f.group())
# else:
#     print('匹配失败')
# f=re.match(r'<([a-z]+)>[a-z]+</\1>','<html>hh</html>')
# if f:
#     print(f.group())

# import re
# list=['apple','banana','pear','orange','huolongguo']
# for i in list:
#     f=re.match('banana|huolongguo',i)
#     if f:
#         print(f.group())
#     else:
#         print('不想吃')

# import re
# f=re.match(r'<(\w+)><(\w+)>.+</\2></\1>','<html><h1>hh</h1></html>')
# if f:
#     print(f.group())
# else:
#     print('匹配失败')
# f=re.match(r'<(?P<JJ>\w+)><(?P<ll>\w+)>.+</(?P=ll)></(?P=JJ)>','<html><h1>hh</h1></html>')
# print(f.group())

# import re
# f=re.match(r'<(\w+)><(\w+)>.+</\2></\1>','<html><h1>hh</h1></html>')
# print(f.group())
# f=re.match(r'<(?P<ss>\w+)><(?P<aa>\w+)>.+</(?P=aa)></(?P=ss)>','<html><h1>hh</h1></html>')
# print(f.group())

'''
1、匹配邮箱，1、账号由4-20位单词字符 2、支持匹配163/126/139 3、要求以.com结尾
2、匹配手机号  以1开头  号段3-9  11位最后一位不能是4、7
3】网址 例：https://www.baidu.com
'''
# import re
# f=re.match(r'^\w{4,20}@(163|126|139)(\.com)$','2522908520@163.com')
# if f:
#     print(f.group())
# else:
#     print('匹配失败')





# import re
# f=re.match('^\w{4,20}@(163|126|139)(\.com)$','123456@139.com')
# if f:
#     print(f.group())
# else:
#     print('匹配失败')
# f2=re.match('^1[3-9]\d{8}[^47]$','13146152021')
# if f2:
#     print(f2.group())
# else:
#     print('匹配失败')
#
# f3=re.match('^(https:www\.).+(\.com)$','https:www.baidu.com')
# if f3:
#     print(f3.group())
# else:
#     print('匹配失败')

'''
写出开头匹配字母和下划线，末尾是数字的正则表达式
匹配手机号：手机号位数为11位，开头为1第二位为3、4、5、7、8
python中正则表达式提取出字符串中的数字
'''
# import re
# f=re.match('^[a-z_A-Z].*\d$','1_a1')
# if f:
#     print(f.group())
# else:
#     print('匹配哦失败')
# import re
# f=re.match('^1[34578]\d{9}$','13146152021')
# if f:
#     print(f.group())
# else:
#     print('匹配失败')
# import re
# s='asd123dw456-789'
# def x(n):
#     return n>=0
# f=filter(x,[1,2,3,])
# print(list(f))
# def not_empty(s):
#   return s and s.strip()
#
# f=filter(not_empty, ['A', '1', 'B', None, 'C', ' '])
# print(list(f))
# print(filter(lambda x:x>=0 and x<=9,[x for x in s]))
# f=re.match('\d+','')
# print(f.group())

# f=filter(str.isdigit, '123ab45')
# f=filter(lambda x:x.isdigit(),'12asd456w-789')
# import re
# s=re.match('\d*',)
# if s:
#     print(s.group())
# else:
#     print('匹配失败')
# a='asd123'
# print(a.isdigit())


# print(list(filter(lambda x:x.isdigit(),'asd123we456*789-')))
# import re
# f=re.match(r'<(?P<jj>\w+)><(?P<gg>\w+)>(.+)</(?P=gg)>+</(?P=jj)>','<html><h1>hh</h1></html>')
# if f:
#     print(f.group())
# else:
#     print('匹配失败')

# content=re.findall('<(?P<j>.+?)>(.*?)</(?P=j)>','<html>12<a>3</a></html>')
# print(content)
# p = re.compile(r'(?P<word>\w+)\s+(?P=word)')
# x=p.findall('Paris in the spring')
# print(x)
