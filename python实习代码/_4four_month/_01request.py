# import requests
#
# response=requests.get(url='https://www.baidu.com')  # 获取响应数据

# print(response) #成功是200  失败是非200
# print(response.status_code)
# response.encoding='utf8'
# print(response.text)
# print(response.content.decode())

# print(type(response))

# print(response.content)  #获取到字节类型数据

# print(response.text) #获取到字符串类型数据
#
# print(response.content.decode())   #将内容解码
#
# print(response.status_code)   #获取状态码


#练习：获取https://www.sina.com.cn

# import requests
# url='https://www.sina.com.cn'
# response=requests.get(url=url)
# print(response.status_code)
# if response.status_code==200:
#     print(response.content.decode())

# import requests
#
# response=requests.get(url='https://www.sina.com.cn')
#
# print(response)
#
# print(response.status_code)
#
# print(response.content.decode())

# import requests
# response=requests.get(url='https://www.baidu.com')
# print(response)
# print(response.content.decode())
# print(response.status_code)


# import requests
# response=requests.get(url='https://www.baidu.com')
# print(response)
# print(type(response))
# print(response.status_code)
# print(response.text)
# print(response.content.decode())


# response.content.decode()
# response.encoding='utf8'
# response.text

# b=b'asd'
# print(type(b))
# c=b.decode()
# print(type(c))
# d=c.encode()
# print(type(d))
# s=b.decode()
# print(type(s))
# s2=s.encode()
# print(type(s2))

# import requests
# response=requests.get(url='https://www.baidu.com')
# print(response.content.decode())
# response.encoding='utf8'
# print(response.text)

# import requests
# url='https://www.baidu.com'
# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
# response=requests.get(url=url,params={'wd':'python'},headers=headers)
# if response.status_code==200:
#     with open('baidu2.html','wb') as f:
#         f.write(response.content)



# import requests
# url='https://www.baidu.com/img/bd_logo1.png'
# response=requests.get(url)
# with open('baidu.png','wb') as f:
#     f.write(response.content)

# import requests
# response=requests.get(url='https://www.baidu.com')
# #打印响应对应请求的请求头信息
# print(response.request.headers)

# import requests
# url='https://www.baidu.com'
# headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
# response=requests.get(url=url,headers=headers)
# print(response.request.headers)

# import requests
# kw={'wd':'python','a':'c'}
# response=requests.get(url='https://www.baidu.com/s?wd=python&a=c')
# # print(response.request._cookies)
# # print(response.cookies)
# print(response.content.decode())

# import requests
# response=requests.get(url='https://www.baidu.com/img/bd_logo1.png')
# with open('baidu2.png','wb') as f:
#     f.write(response.content)


# import requests
# response=requests.get(url='https://www.baidu.com')
# print(response.request.headers)
# print(response.headers)

# import requests
# response=requests.get('https://www.baidu.com/img/bd_logo2.png')
# with open('baidu3.png','wb') as f:
#     f.write(response.content)

# import requests
# response=requests.get(url='https://www.baidu.com')
# print(response.content.decode())
# print(response)
# print(response.status_code)




# import requests
# urlstr='https://www.baidu.com'
# kw={'wd':'python'}
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
# response=requests.get(url=urlstr,headers=headers,params=kw)
# with open('baidu.html',mode='wb') as f:
#     f.write(response.content)


# import requests
# #定义网址
# urlstr='https://www.baidu.com'
# #定义一个参数数据（字典）
# params={'wd':'python'}
# #定义一个请求头
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
# #开始请求网络
# response=requests.get(url=urlstr,headers=headers,params=params)
# #把返回内容写到文件
# with open('baidu.html',mode='wb') as f:
#     f.write(response.content)

# import requests
# url='http://fy.iciba.com/ajax.php?a=fy'

# import requests
# i=input("please input :")
# response=requests.post(url='http://fy.iciba.com/ajax.php?a=fy',data={'w':i})
# if response.status_code==200:
#     print(response.json())


# import requests
# url='http://fy.iciba.com/ajax.php?a=fy'
# word=input("please input:")
# response=requests.post(url=url,data={'w':word})
# if response.status_code==200:
#     print(response.json())


# import requests
# url='http://fy.iciba.com/ajax.php?a=fy'
# #1、接受键盘输入
# word=input("please input:")
# #将输入的内容post提交到金山
# response=requests.post(url=url,data={'w':word})
# #判断状态码200
# if response.status_code==200:
#     print(response.json())

# import requests
# url='http://fy.iciba.com/ajax.php?a=fy'
# word=input("please input:")
# response=requests.post(url=url,data={'w':word})
# if response.status_code==200:
#     print(response.json()['content']['word_mean'])

# session
# import requests
# session=requests.session()
# #封装成字典的用户名和密码
# data={'email':'13439770580','password':'123456xbh'}
# response=session.post(url='http://www.renren.com/PLogin.do',data=data)
# print(response.text)



# import requests
# url='https://qzone.qq.com/'
# session=requests.session()
# data={'u':'','p':''}
# response=session.post(url=url,data=data)
# print(response.content.decode())


# import requests
# url='https://www.hao123.com/?tn=02003390_29_hao_pg'
# data={'word':'python'}
# session=requests.session()
# response=session.post(url=url,data=data)
# response.encoding='utf8'
# print(response.text)

# import requests
# session=requests.session()
# url='https://www.baidu.com/s?ie=utf-8'
# data={'wd':'python'}
# response=session.post(url=url,data=data)
# print(response.content.decode())


# import requests
# url='https://www.baidu.com/img/bd_logo1.png'
# session=requests.session()
# response=session.get(url=url)
# with open('baidu2.png',mode='wb') as f:
#     f.write(response.content)


# import requests
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
# data={'email':'13439770580','password':'123456xbh'}
# session=requests.session()
# response=session.post(url='http://www.renren.com/PLogin.do',data=data,headers=headers)
# # print(response.content.decode())
# session2=requests.session()
# response2=session2.get(url='http://www.renren.com/969173485/profile?v=info_timeline',headers=headers)
# if response2.status_code==200:
#     print(response2.content.decode())



# # 使用cookiejar完整代码
# from urllib import request,parse
# from http import cookiejar
#
# # 创建cookiejar的实例
# cookie = cookiejar.CookieJar()
# # 常见cookie的管理器
# cookie_handler = request.HTTPCookieProcessor(cookie)
# # 创建http请求的管理器
# http_handler = request.HTTPHandler()
#
# # 生成https管理器
# https_handler = request.HTTPSHandler()
#
# # 创建请求管理器
# opener = request.build_opener(http_handler,https_handler,cookie_handler)
#
# def login():
#     # 负责首次登录，输入用户名和密码，用来获取cookie
#     url = 'http://www.renren.com/PLogin.do'
#
#     id = input('请输入用户名：')
#     pw = input('请输入密码：')
#
#     data = {
#         # 从input标签的name获取参数的key，value由输入获取
#         "email": id,
#         "password": pw
#     }
#     # 把数据进行编码
#     data = parse.urlencode(data)
#     # 创建一个请求对象
#     req = request.Request(url,data=data.encode('utf-8'))
#     # 使用opener发起请求
#     rsp = opener.open(req)
#
# # 以上代码就可以进一步获取cookie了，cookie在哪呢？cookie在opener里
# def getHomePage():
#     # 地址是用在浏览器登录后的个人信息页地址
#     url = "http://www.renren.com/969173485/profile?v=info_timeline"
#
#     # 如果已经执行login函数，则opener自动已经包含cookie
#     rsp = opener.open(url)
#     html = rsp.read().decode()
#
#     with open("rsp1.html", "w", encoding="utf-8")as f:
#         # 将爬取的页面
#         print(html)
#         f.write(html)
#
# if __name__ == '__main__':
#     login()
#     getHomePage()


# import re
#
# title = u'你好，hello，世界'
# pattern = re.compile('[\u4e00-\u9fa5]+')
# result = pattern.findall(title)
#
# print (result)

#
# import requests
# url='http://www.renren.com/PLogin.do'
# data={'email':'13439770580','password':'123456xbh'}
# session=requests.session()
# response=session.post(url=url,data=data)
# print(response.text)

# import requests
# url='https://qzone.qq.com/'
# data={'u':'737189747','p':'13146152021sll.'}
# session=requests.session()
# response=session.post(url=url,data=data)
# print(response.text)

# import requests
# url='http://www.feiyiproxy.com/?page_id=1457'
# session=requests.session()
# response=session.get(url=url)
# if response.status_code==200:
#     with open('daili.txt',mode='wb') as f:
#         f.write(response.content)


# import requests
# url='https://www.baidu.com'
# response=requests.get(url=url)
# print(response.request.headers)
# print(response.headers)
# import requests
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
# url='https://www.baidu.com/s?'
# params={'wd':'python'}
# response=requests.get(url=url,headers=headers,params=params)
# print(response.status_code)
# print(response.content.decode())
# url='https://www.baidu.com/s?wd=python'
# response=requests.get(url=url,headers=headers)
# # print(response.content.decode())
# if response.status_code==200:
#     with open('baidu3.html',mode='wb') as f:
#         f.write(response.content)


# import requests
# url='http://fy.iciba.com/ajax.php?a=fy'
# word=input("please input:")
# session=requests.session()
# data={'w':word}
# response=session.post(url=url,headers=headers,data=data)
# if response.status_code==200:
#     print(response.json()['content']['word_mean'])


# import requests
# url='https://qzone.qq.com/'
# session=requests.session()
# data={'u':'737189747','p':'13146152021sll.'}
# response=session.post(url=url,headers=headers,data=data)
# if response.status_code==200:
#     with open('qqkongjian.html',mode='wb') as f:
#         f.write(response.content)

# import requests
# from retrying import retry
# url='https://www.baidu.com'
# #最大重试3次，3次全部报错，才会报错
# @retry(stop_max_attempt_number=3)
# def _parse_url(url):
#     #超时的时候会报错并重试
#     response=requests.get(url,headers=headers,timeout=3)
#     #状态码不是200也会报错并重试
#     assert response.status_code==200
#     return response

# s='0123456'
# print(s[-1::-2])




