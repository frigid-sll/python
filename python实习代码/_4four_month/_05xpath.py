#获取36kr网站内容
# import requests,json
# session=requests.session()
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
# url='https://36kr.com'
# response=session.get(url=url,headers=headers,verify=False)
# if response.status_code==200:
#     with open('36kr.txt',mode='w') as f:
#         json.dump(response.text,f,ensure_ascii=False,indent=2)

# from lxml import etree
# html=etree.HTML(36kr.txt)
# ret_list=html.xpath()

# from lxml import etree
# import requests
# url='https://www.36kr.com/'
# response=requests.get(url=url,headers=headers,verify=False)
# html=etree.HTML(response.content.decode())
# print(response.content.decode())
# list=html.xpath("//div[@class='kr-home-flow-list']//div[@class='kr-shadow-content']//a[@class='article-item-title ellipsis-2 weight-bold']/text()")
# print(list)
# print(len(list))

# import requests,json,jsonpath
# from lxml import etree
# url='https://36kr.com/api/search-column/mainsite?per_page=20&page=2&_=1547966171507'
# response=requests.get(url=url)
# # with open('7xml.txt',mode='w') as f:
# #     json.dump(response.text,f,ensure_ascii=False)
# with open('7xml.txt',mode='r') as f:
#     content=json.load(f)
#     listTitle=jsonpath.jsonpath(content,'$.data.items[*].title')
#     print(listTitle)

# from lxml import etree
# import requests
# url='https://www.36kr.com/'
# response=requests.get(url=url)
# html=etree.HTML(response.text)
# list=html.xpath("//div[@class='kr-home-flow-list']//a[@class='article-item-title ellipsis-2 weight-bold']/text()")
# print(list)

# import requests,jsonpath,json
# url='https://36kr.com/api/search-column/mainsite?per_page=20&page=2&_=1547967096053'
# response=requests.get(url=url)
# with open('8.txt',mode='w') as f:
#     json.dump(response.text,f,ensure_ascii=False)
# with open('8.txt',mode='r') as f:
#     content=json.load(f)
#     list=jsonpath.jsonpath(content,'$.data.items[*].title')
#     print(list)
# a=response.text
# b=json.loads(a)
# if b==response.json():
#     print(111111111111111111)
# list=jsonpath.jsonpath(dict(json.loads(response.text)),'$.data.items[*].title')
# list=jsonpath.jsonpath(dict(response.json()),'$.data.items[*].title')
# print(list)

# import requests
# from lxml import etree
# response=requests.get('https://www.36kr.com')
# html=etree.HTML(response.text)
# list=html.xpath("//div[@class='kr-home-flow-list']//a[2]/text()")
# print(list)



# import requests,json,jsonpath
# response=requests.get('https://36kr.com/api/search-column/mainsite?per_page=20&page=2&_=1547968986476')
# list=jsonpath.jsonpath(response.json(),'$..cover')
# # print(list)
# for x in range(len(list)):
#     with open('img%d.jpg'%x,mode='wb') as f:
#         img=requests.get(list[x])
#         f.write(img.content)


# import requests,json,jsonpath
# from lxml import etree
# url='http://www.abckg.com'
# response=requests.get(url=url)
# html=etree.HTML(response.text)
# listContent=html.xpath("//div[@class='intro']/p/text()")
# listTitle=html.xpath("//div[@class='post']/h2/a/text()")
# # print(listTitle)
# # print(listContent)
# list=[]
# for x in range(len(listContent)):
#     dict={}
#     dict['title']=listTitle[x]
#     dict['content']=listContent[x]
#     list.append(dict)
# with open('abckg.json',mode='w') as f:
#     json.dump(list,f,ensure_ascii=False,indent=2)

# import requests,jsonpath,json
# response=requests.get('https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=qq%E5%A4%B4%E5%83%8F%E7%94%B7%E7%94%9F%E8%83%8C%E5%BD%B1&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&word=qq%E5%A4%B4%E5%83%8F%E7%94%B7%E7%94%9F%E8%83%8C%E5%BD%B1&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&fr=&expermode=&force=&pn=120&rn=30&gsm=78&1547970975885=')
# list=jsonpath.jsonpath(response.json(),'$.data[*].thumbURL')
# # print(list)
# # print(len(list))
# for x in range(len(list)):
#     img=requests.get(list[x])
#     with open('img%d.jpg'%x,mode='wb') as f:
#         f.write(img.content)



# import requests
# import re
# from lxml import etree
# response=requests.get(url='http://www.feiyiproxy.com/?page_id=1457',verify=False,headers=headers)
# html=etree.HTML(response.text)
# # print(response.text)
# # with open(file='1.html',mode='w', encoding='utf-8') as f:
# #     f.write(response.text)
# pattern = re.compile('<td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td>')
# data = re.findall(pattern=pattern, string=response.text)25
# pattern2=re.compile('<td>(\d{2,6})</td>')
# pattern3=re.compile('<th>(IP)</th>')
# data3=re.findall(pattern=pattern3,string=response.text)
# data2=re.findall(pattern=pattern2,string=response.text)
# # print(data)
# # print(type(data))
# for i in data2:
#     print(i)
# print(data3)

# list=html.xpath("//div[@class='et_pb_row et_pb_row_2']//th[position()<3]")
# print(list)

# import requests,re
# url='https://www.36kr.com/'
# response=requests.get(url=url,headers=headers)
# # with open(file='zhengze.html',mode='w',encoding='utf-8') as f:
# #     f.write(response.text)
#
# pattern=re.compile('<script>var props=(.*?),locationnal=')
# data=re.findall(pattern=pattern,string=response.text)
# print(data)


# url='http://www.abckg.com/'
# import requests,json,jsonpath
# from lxml import etree
# response=requests.get(url=url)
# html=etree.HTML(response.text)
# list=html.xpath("//div[@class='content']//h2/a/text()")
# print(list)


# import requests,json,jsonpath
# response=requests.get('https://36kr.com/pp/api/aggregation-entity?type=web_latest_article&b_id=44111&per_page=20')
# list=jsonpath.jsonpath(response.json(),'$..cover')
# # print(list)
# print(len(list))
# for x in range(len(list)):
#     with open('img%d.jpg'%x,mode='wb') as f:
#         img=requests.get(list[x])
#         f.write(img.content)


# import requests,json,jsonpath                        #引入模块requests,json,jsonpath
# from lxml import etree                              #引入lxml模块里的etree
# url='http://www.abckg.com/'                         #这是你要爬的网址
# response=requests.get(url=url)                      #定义一个变量response来接收响应内容
# html=etree.HTML(response.text)
# list=html.xpath("//div[@class='content']//h2/a/text()")         #用来获取标题  括号里面是xml
# list2=html.xpath("//div[@class='intro']/p/text()")              #用来获取内容
# # print(list)
# # print(list2)
# list3=[]                        #顶一个空列表
# for x in range(len(list)):          #for循环  将标题、内容封装成字典添加到列表里
#     dict={}
#     dict['title']=list[x]
#     dict['content']=list2[x]
#     list3.append(dict)
# # print(list3)
# with open('9.json',mode='w',encoding='utf-8') as f:
#     json.dump(list3,f,ensure_ascii=False,indent=2)              #将python类型转为json类型写入到文件里

