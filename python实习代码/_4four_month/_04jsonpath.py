# import jsonpath,json
#
# #读取json数据
# with open('students.json',mode='r') as f:
#     content=json.load(f)
#     #解析json数据
#     print(content)
#     listTitle=jsonpath.jsonpath(content,'$..title')
#     print(listTitle)




# import jsonpath,json
#
# with open('students.json',mode='r') as f:
#     content=json.load(f)
#     listAuthor=jsonpath.jsonpath(content,'$..book')
#     print(listAuthor)

# import jsonpath,json
# with open('students.json',mode='r') as f:
#     s=json.load(f)
#     listPrice=jsonpath.jsonpath(s,'$..price')
#     print(listPrice)


# import json,jsonpath
# with open('students.json',mode='r') as f:
#     content=json.load(f)
#     listAuthor=jsonpath.jsonpath(content,'$..book[-1:-2:-1]')
#     print(listAuthor)


# str='asdf'
# print(str[-1:-5:-1])

# import json,jsonpath
# with open('students.json',mode='r') as f:
#     content=json.load(f)
#     listBook=jsonpath.jsonpath(content,'$..book[?(@.price>10)]')
#     print(listBook)


# import json,jsonpath
# with open('students.json',mode='r') as f:
#     content=json.load(f)
#     listBook=jsonpath.jsonpath(content,'$.store.book[*].price')
#     print(listBook)


# import json,jsonpath
# with open('students.json',mode='r') as f:
#     content=json.load(f)
    # listBook=jsonpath.jsonpath(content,'$..book[1:4]')
    # listBook=jsonpath.jsonpath(content,'$..book[0,1,2]')
    # print(listBook)

# import json,jsonpath
# with open('students.json',mode='r') as f:
#     s=json.load(f)
#     l=jsonpath.jsonpath(s,'$..book[?(@.price>10)].price')
#     print(l)

# import requests
# url='http://www.lagou.com/lbs/getAllCitySearchLabels.json'
# session=requests.session()
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
# response=session.get(url=url,headers=headers)
# if response.status_code==200:
#     with open('lagou.txt',mode='w') as f:
#         f.write(response.content.decode())


# import json,jsonpath
# with open('lagou.txt',mode='r') as f:
#     content=json.load(f)
#     listId=jsonpath.jsonpath(content,'$.content.data.allCitySearchLabels[*]..id')
#     listCity=jsonpath.jsonpath(content,'$.content.data.allCitySearchLabels[*]..name')
#     print(len(listCity)-1)
#     list=[]
#     for x in range(len(listId)-1):
#         dict={}
#         dict['id']=listId[x]
#         dict['name']=listCity[x]
#         list.append(dict)
#     with open('l.txt',mode='w') as f2:
#         json.dump(list,f2,indent=2,ensure_ascii=False)
#
#
#     with open('lagou_city.txt','w') as f2:
#         f2.write(str(jsonlist))







# import requests
# session=requests.session()
# url='http://www.lagou.com/lbs/getAllCitySearchLabels.json '
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
# response=session.get(url=url,headers=headers)
# if response.status_code==200:
#     with open('homework1.json',mode='w') as f:
#         f.write(response.content.decode())

# import json,jsonpath
# with open('homework1.json',mode='r') as f:
#     content=json.load(f)
#     content1=jsonpath.jsonpath(content,'$.content.data.allCitySearchLabels..id')
#     content2=jsonpath.jsonpath(content,'$.content.data.allCitySearchLabels..name')
#     list=[]
#     for x in range(len(content1)-1):
#         dict={}
#         dict['id']=content1[x]
#         dict['name']=content2[x]
#         list.append(dict)
#     with open('homework1_lagou.json',mode='w') as f2:
#         json.dump(list,f2,ensure_ascii=False,indent=2)
# with open('homework1_lagou.json',mode='r') as f:
#     content=json.load(f)
#     print(content)



# import jsonpath,json
# with open('lagou_01.json',mode='r') as f:
#     content=json.load(f)
#     listId=jsonpath.jsonpath(content,'$.content.data.allCitySearchLabels..id')
#     listName=jsonpath.jsonpath(content,'$.content.data.allCitySearchLabels..name')
#     list=[]
#     for x in range(len(listId)):
#         dict={}
#         dict['id']=listId[x]
#         dict['name']=listName[x]
#         list.append(dict)
#     with open('lagou_03.json',mode='w') as f2:
#         json.dump(list,f2,ensure_ascii=False,indent=2)



# import requests
# url='http://www.lagou.com/lbs/getAllCitySearchLabels.json '
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
# session=requests.session()
# response=session.get(url=url,headers=headers)
# if response.status_code==200:
#     with open('lagou_01.json',mode='w') as f:
#         f.write(response.content.decode())


# import jsonpath,json
# with open('lagou_01.json',mode='r') as f:
#     content=json.load(f)
#     listName=jsonpath.jsonpath(content,'$..name')
#     with open('lagou_02.txt',mode='w') as f2:
#         f2.write(str(listName))





# import jsonpath,json
# with open('students.json',mode='r') as f:
#     content=json.load(f)
#     s=jsonpath.jsonpath(content,'$.store.book[?(@.price>10)].price')
#     print(s)

# import json,jsonpath
# with open('lagou_01.json',mode='r') as f:
#     content=json.load(f)
#     listName=jsonpath.jsonpath(content,'$..name')
#     with open('b.txt',mode='w') as f2:
#         f2.write(str(listName))



# import requests,json
# session=requests.session()
# url='http://fy.iciba.com/ajax.php?a=fy'
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
# response=session.post(url=url,headers=headers,data={'w':'good morning'})
# if response.status_code==200:
#     print(response.json()['content']['word_mean'])
#     x=json.loads(response.text)
#     print(x['content']['word_mean'])



# import requests
# url='https://www.baidu.com/s?'
# session=requests.session()
# params={'wd':'python'}
# response=session.get(url=url,params=params,headers=headers)
# if response.status_code==200:
#     with open('baidu6.html',mode='wb') as f:
#         f.write(response.content)

# import requests
# url='https://www.baidu.com/s?wd=python'
# session=requests.session()
# response=session.get(url=url,headers=headers)
# if response.status_code==200:
#     with open('baidu5.html',mode='wb') as f :
#         f.write(response.content)

# import requests
# session=requests.session()
# url='http://www.renren.com/PLogin.do'
# response=session.post(url=url,headers=headers,data={'email':'13439770580','password':'123456xbh'})
# if response.status_code==200:
#     with open('renren.txt',mode='w') as f:
#         f.write(response.content.decode())


# from retrying import retry
# import requests,json,jsonpath
# @retry(stop_max_attempt_number=3)
# def getHTML(url):
#     try:
#         response=requests.get(url=url,headers=headers,timeout=0.01,verify=False)
#         print(response.text)
#     except Exception as e:
#         print(e)
#
# if __name__ == '__main__':
#     getHTML('https://www.baidu.com')

# import requests,jsonpath,json
# a='{"name":"zhangsan","age":19}'
# b=json.loads(a)
# print(b)
# print(type(b))
# # with open('1.txt',mode='w') as f:
# #     json.dump(b,f,ensure_ascii=False)
# # with open('1.txt',mode='r') as f:
# #     c=json.load(f)
# #     print(c)
# c=json.dumps(b)
# print(c)

# import requests,jsonpath,json
# url='https://www.lagou.com/lbs/getAllCitySearchLabels.json'
# session=requests.session()
# response=session.get(url=url,headers=headers,verify=False)
# if response.status_code==200:
#     with open('3.txt',mode='wb') as f:
#         f.write(response.content)
# with open('3.txt',mode='rb') as f:
#     content=json.load(f)
#     listName=jsonpath.jsonpath(content,'$..name')
#     with open('4.txt',mode='w') as f2:
#         json.dump(listName,f2,ensure_ascii=False,indent=2)



# import requests,json,jsonpath
# session=requests.session()
# url='https://www.lagou.com/lbs/getAllCitySearchLabels.json'
# headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
# response=session.get(url=url,headers=headers,verify=False)
# if response.status_code==200:
#     with open('5.txt',mode='w') as f:
#         json.dump(response.text,f,ensure_ascii=False)


# with open('5.txt',mode='r') as f:
#     content=json.load(f)
#     list=jsonpath.jsonpath(content,'$..name')
#     with open('6.json',mode='w') as f2:
#         json.dump(list,f2,ensure_ascii=False,indent=2)







