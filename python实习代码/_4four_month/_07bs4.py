# from bs4 import BeautifulSoup
# import requests
# response=requests.get(url='')
# #2、将内容放入到BeautifulSoup
# #第一个参数：要解析的内容，第二个参数：解析器
# soup=BeautifulSoup(response.text,'lxml')
# #name:要查找的标签名称
# listId=soup.find_all(name='td',attrs={'data-title':'IP'})
# listPort=soup.find_all(name='td',attrs={'data-title':'PORT'})
# print(listId)
# for x in listId:
#     print(x.get_text())    #获取标签里面的内容
#
# for x in listPort:
#     print(x.get_text())

# import requests
# from bs4 import BeautifulSoup
# # print(list)
# # proxies={'http':'163.125.28.243:8118'}
# # response=requests.get(url='https://www.baidu.com',proxies=proxies)
# # print(response.text)
# from retrying import retry
#
# def getIP():
#     response = requests.get(url='https://www.kuaidaili.com/free/')
#     soup = BeautifulSoup(response.text, 'lxml')
#     listIp = soup.find_all(name='td', attrs={'data-title': 'IP'})
#     listPort = soup.find_all(name='td', attrs={'data-title': 'PORT'})
#     list = []
#     for x in range(len(listPort)):
#         list.append('%s:%s' % (listIp[x].get_text(), listPort[x].get_text()))
#     return list
#
# @retry(stop_max_attempt_number=2)
# def getHTML(url,proxies):
#     response=requests.get(url=url,proxies=proxies,timeout=2)
#     print(response.content.decode())
#
# if __name__ == '__main__':
#     list=getIP()
#     for x in list:
#         try:
#             getHTML('https://www.baidu.com', {'http': x})
#             break
#         except:
#             print('进入下一个循环')


# import requests
# from retrying import retry
# from bs4 import BeautifulSoup
# def getlist():
#     url = 'https://www.kuaidaili.com/free/'
#     response = requests.get(url=url)
#     soup = BeautifulSoup(response.text, 'lxml')
#     listIp = soup.find_all(name='td', attrs={'data-title': 'IP'})
#     listPort = soup.find_all(name='td', attrs={'data-title': 'PORT'})
#     list=[]
#     for x in range(len(listPort)):
#         list.append('%s:%s'%(listIp[x].get_text(),listPort[x].get_text()))
#     return list
# # print(listIp)
# # print(listPort)
# def getHTML(url,proxies):
#     response=requests.get(url=url,proxies=proxies)
#     print(response.content.decode())
#
# if __name__ == '__main__':
#     list=getlist()
#     for i in list:
#         try:
#             getHTML('https://www.baidu.com',{'html':i})
#             break
#         except:
#             pass

# import requests,re
# url='https://www.kuaidaili.com/free/'
# response=requests.get(url=url)
# # with open('ip.txt',mode='w',encoding='utf8') as f:
# #     f.write(response.text)
# listIp=re.findall('<td data-title="IP">(.*?)</td>',response.text,re.S)
# listPort=re.findall('<td data-title="PORT">(.*?)</td>',response.text,re.S)
# # print(listIp)
# # print(listPort)
# list=[]
# for x in range(len(listPort)):
#     list.append('%s:%s'%(listIp[x],listPort[x]))
# # print(list)
# proxies={'http':list[0]}、
# response=requests.get(url='https://www.baidu.com',proxies=proxies)
# print(response.text)


# from bs4 import BeautifulSoup
# import requests
# url='https://www.kuaidaili.com/free/'
# response=requests.get(url=url)
# soup=BeautifulSoup(response.text,'lxml')
# listIp = soup.find_all(name='td', attrs={'data-title': 'IP'})
# for x in listIp:
#     print(x.get_text())

from bs4 import BeautifulSoup
import requests
url='https://www.36kr.com/p/5175852'
response=requests.get(url=url)
soup=BeautifulSoup(response.text,'lxml')
listTitle=soup.find_all(name=['h1','h2'],attrs={'class':'article-title margin-bottom-20 common-width'})
for x in listTitle:
    print(x.get('class'))


# from bs4 import BeautifulSoup
# import requests
# url='https://www.kuaidaili.com/free'
# response=requests.get(url=url)
# soup=BeautifulSoup(response.text,'lxml')
# listId=soup.find_all(name='td',attrs={'data-title':'ID'})
# for x in listId:
#     print(x.get_text())