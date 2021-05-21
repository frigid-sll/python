'''
使用requests抓取  http://www.kepuchina.cn/health/  页面的热点新闻内容
   匹配出新闻的标题，地址，日期，图片地址 至少抓取六条新闻
   将数据存储为list嵌套dict形式
   如 [ {‘title’:’新闻标题’,’url’,’http://123.html’,’img:’4124214.jpg’,’date’:’2018-12-20’} ]
将图片存储到本地硬盘中，如4124214.jpg

1)实现抓内容（5分）
2)将数据存为list嵌套dict 够六条新闻（25分）
3)将图片保存到硬盘中（10分）
'''


import requests
from lxml import etree
import re

response = requests.get(url='http://www.kepuchina.cn/health/')
html = etree.HTML(response.content.decode())

listTitle = html.xpath('/html/body/div/div[3]/div[2]/div/div[1]/div/div/div/h2/a/text()')
# print(listTitle)

listUrl = html.xpath('/html/body/div/div[3]/div[2]/div/div[1]/div/div/div/h2/a/@href')
# print(listUrl)
for x in range(len(listUrl)):
    listUrl[x]='http://www.kepuchina.cn/health'+listUrl[x][1:]
# print(listUrl)
#
listImg = html.xpath('/html/body/div/div[3]/div[2]/div/div[1]/div/div/a/img/@src')
# print(listImg)
for x in range(len(listImg)):
    listImg[x]='http://www.kepuchina.cn/health'+listImg[x][1:]
    with open('{}.jpg'.format(x),mode='wb') as f:
        response2=requests.get(url=listImg[x])
        f.write(response2.content)
# print(listImg)

listDate = html.xpath('/html/body/div/div[3]/div[2]/div/div[1]/div/div/div/p/em/text()')
# print(listDate)
#
list =[]
for x in range(len(listTitle)):
    dict ={}
    dict['title']=listTitle[x]
    dict['url']=listUrl[x]
    dict['imgurl']=listImg[x]
    dict['date']=listDate[x]
    list.append(dict)
# print(list)

