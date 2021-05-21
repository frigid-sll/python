# import csv
#
# with open('1.csv',mode='a',newline='') as f:    #没有这个新建  有的话追加
#     writer=csv.writer(f)
#     writer.writerows([['123','456'],['789','333']])
#
# with open('1.csv',mode='r') as f:
#     reader=csv.reader(f)
#     for x in reader:
#         print(x)

# fieldnames=['title','content']
# listData=[{'title':'father','content':'星期一'},{'title':'mother','content':'星期二'}]
# with open('1.csv',mode='a',newline='') as f:
#     writer=csv.DictWriter(f,fieldnames=fieldnames)
#     writer.writeheader()      #第一行将标题写入文件
#     writer.writerows(listData)
# #
# with open('1.csv',mode='r') as f:
#     reader=csv.DictReader(f)
#     for x in reader:
#         print(dict(x))

# import requests
# from bs4 import BeautifulSoup
# from lxml import etree
# from selenium import webdriver
# driver=webdriver.Chrome()
# url='https://hr.tencent.com/position.php?lid=&tid=&keywords='
# driver.get(url=url)
# listPartTitle=driver.find_elements_by_xpath('//*[@id="position"]/div[1]/table/tbody/tr/td[1]/a')
# listTitle=[]
# for x in listPartTitle:
#     listTitle.append(x.text)
# # print(listTitle)
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'}
# response=requests.get(url=url,headers=headers,verify=False)
# html=etree.HTML(response.text)
# listNumber=html.xpath("//div[@class='left wcont_b box']//tr[position()>1]/td[3]/text()")
# # print(listNumber)
# listAddress=html.xpath("//div[@class='left wcont_b box']//tr[position()>1]/td[4]/text()")
# # print(listAddress)
# listAll=[]
# for x in range(len(listAddress)):
#     dict={}
#     dict['title']=listTitle[x]
#     dict['number']=listNumber[x]
#     dict['address']=listAddress[x]
#     listAll.append(dict)
# title=['title','number','address']
# with open('tengxun.csv',mode='a',newline='') as f:
#     writer=csv.DictWriter(f,fieldnames=title)
#     writer.writeheader()
#     writer.writerows(listAll)


# import requests,csv
# from lxml import etree
#
# class Tencent:
#     def GetTitle(self):
#         self.listTitle=html.xpath("//div[@class='left wcont_b box']//td/a/text()")
#         return self.GetNumber()
#
#     def GetNumber(self):
#         self.listNum=html.xpath("//div[@class='left wcont_b box']//tr[position()>1]/td[3]/text()")
#         return self.GetAddress()
#
#     def GetAddress(self):
#         self.listAdd=html.xpath("//div[@class='left wcont_b box']//tr[position()>1]/td[4]/text()")
#         return self.Write()
#
#     def Write(self):
#         listAll=[]
#         for x in range(len(self.listTitle)):
#             dict={}
#             dict['Title']=self.listTitle[x]
#             dict['Number']=self.listNum[x]
#             dict['Address']=self.listAdd[x]
#             listAll.append(dict)
#         fieldnames=['Title','Number','Address']
#         with open('Tencent.csv',mode='a',newline='') as f:
#             writer=csv.DictWriter(f,fieldnames=fieldnames)
#             if i==0:
#                 writer.writeheader()
#             writer.writerows(listAll)
#
# if __name__ == '__main__':
#     for i in range(0,51,10):
#         url = 'https://hr.tencent.com/position.php?lid=&tid=&keywords=&start=%d#a' % i
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'}
#         tencent = Tencent()
#         response = requests.get(url=url, headers=headers, verify=False)
#         html = etree.HTML(response.text)
#         tencent.GetTitle()



# for x in range(1,10):
#     for y in range(1,x+1):
#         print('%d*%d=%d'%(x,y,x*y),end=' ')
#     print('\n')



# print('\n'.join([' '.join(['%d*%d=%d'%(x,y,x*y) for x in range(1,y+1)]) for y in range(1,10)]))

'''
随机输入一个1-15之间的整数k,有一个整数n，根据这个n的值可以求出一个值s，规则是这样的：s=1+1/2+1/3+...+1/n,找出s>k时n的最小值
'''
# while True:
#     k=int(input("请输入一个1到15之间的整数："))
#     if k>=1 and k<=15:
#         n=2
#         while True:
#             _sum=sum([1/x for x in range(1,n+1)])
#             if _sum <= k:
#                 n+=1
#             else:
#                 print('n的最小值为:%d'%n)
#                 break
#         break
#     else:
#         print('你输入的数字无效')


'''
随机输入两个整数，求出这两个数的最小公倍数和最大公约数之和
'''
# m=int(input('请输入m的值：'))
# n=int(input('请输入n的值：'))
# m_yue=[x for x in range(1,m+1) if m%x==0]
# n_yue=[x for x in range(1,n+1) if n%x==0]
# max_yue=max([x for x in m_yue if x in n_yue])
# if m>n:
#     m_bei=[m*x for x in range(1,m+1)]
#     n_bei=[n*x for x in range(1,m+1)]
# else:
#     m_bei=[m*x for x in range(1,n+1)]
#     n_bei=[n*x for x in range(1,n+1)]
# min_bei=min([x for x in m_bei if x in n_bei])
# print('最小公倍数和最大公约数的和为：%d'%(max_yue+min_bei))


'''
随机输入一个整数n,这个n的值代表有n盏灯和n个人,数字就是灯的编号。最开始n盏灯都是亮着的，规则如下：
第一个人对第一盏灯和能被2整除的灯的编号进行一次开关操作，
第二个人对第二盏灯和能被2整除的灯的编号进行一次开关操作，
...
第n个人对第n盏灯和能被2整除的灯的编号进行一次开关操作，
最后一个人只对最后一盏灯进行一次开关操作，
求出最后开着的灯的编号
'''
# n=int(input('请输入有几盏灯：'))
# exe_list=[]
# for x in range(1,n+1):
#     if x ==n:
#         exe_list.append(x)
#     else:
#         exe_list.extend([y for y in range(1, n+1) if y == x or y % 2 == 0])
# exe_distinct=['%s'%x for x in set(exe_list)]
# _str=''.join(['%s'%x for x in exe_list])
# list_open=[x for x in exe_distinct if _str.count(x)%2==1]
# print('开着的灯有:%s'%(' '.join(list_open)))

'''
随机输入一个整数，代表这个列表的长度，都是由0和1组成的，打印出所有能组合出的列表
比如输入的整数为1，那么结果为：
[0],[1]
输入的整数为2，那么结果为：
[0,0],[0,1],[1,0],[1,1]
'''
# columns = int(input("请输入你要的数据是几列："))
# replace_num = 2 ** columns
# replace_list = [x + 1 for x in range(replace_num)]
# num = []
# l = len(replace_list)
# for x in range(l):
#     if (2 ** (x + 1)) < l:
#         num.append(2 ** (x + 1))
# a = []
# for x in range(columns):
#     a.append(0)
# for x in range(replace_num):
#     b = []
#     for k in range(len(num)):  # 有几个if
#         if (x + 1) % num[k] == 0:
#             a[-k - 1] = 1
#         else:
#             a[-k - 1] = 0
#         if num[k] > 2:
#             for h in range(int(num[k] - num[k] / 2 - 1)):  # 有几个判断  k/2+h+1
#                 if (x + 1) % num[k] == num[k] / 2 + h + 1:
#                     a[-k - 1] = 1
#
#     if x == replace_num / num[0]:
#         a[0] = 1
#     print(a)