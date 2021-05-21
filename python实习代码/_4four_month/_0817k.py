# from lxml import etree
# import requests
# from bs4 import BeautifulSoup
# # #请求网络数据
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
# url='http://www.17k.com/'
# response=requests.get(url=url,headers=headers,timeout=2,verify=False)
# # if response.status_code==200:
# #     print(response.text)
# soup=BeautifulSoup(response.text,'lxml')
# # listUl=soup.find_all(name='ul',attrs={'class':'BJTJ_CONT Top1'})
# listLi=soup.select('ul[class="BJTJ_CONT Top1"] li')
# # print(listLi)
# listBook=[]
# for x in listLi:
#     itemurl=str(x.find_all('a')[1].get('href')).replace('book','list')
#     listBook.append(itemurl)
# # print(listBook)
# listall=[]
# for x in listBook:
#     lista=[]
#     response=requests.get(url=x)
#     html=etree.HTML(response.text)
#     list=html.xpath("//dl[@class='Volume']//a/@href")
#     for i in list:
#         lista.append('http://www.17k.com'+i)
#     listall.append(lista)
# # print(listall[0])
# for x in listall:
#     for i in x:
#         try:
#             response = requests.get(url=i, headers=headers, verify=False)
#             html=etree.HTML(response.content.decode())
#             listb=html.xpath("//div[@class='readAreaBox content']//div[@class='p']/text()")
#             print(''.join(listb).replace(' ','').replace('\n',''),end='')
#         except:
#             pass
#     break





# from lxml import etree
# html=etree.HTML(response.text)
# list=html.xpath("//ul[@class='BJTJ_CONT Top1']/li/a/@href")
# listIp=[]
# for i,x in enumerate(list):
#     if i%2==1:
#         listIp.append(x)
# # print(listIp)
# listIp2=[]
# for x in listIp:
#     listIp2.append(str(x).replace('book','list'))
# print(listIp2)

# import re
# s="'  by ', ' 阅读 1265 次, 今日 79 次 '"
# print(re.findall('\d+',s)[0])

dict={'m':1,'n':2}

for x,i in dict.items():
    if x!='m':
        print(x, i)