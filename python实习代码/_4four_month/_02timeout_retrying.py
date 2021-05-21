# import os
# os.rename('_03timeout_retrying.py','_02timeout_retrying.py')


# import requests
# #timeout ：超时，单位：秒，超过时间无响应则抛出异常
# try:
#     response=requests.get(url='http://www.baidu.com',timeout=0.001)
#     print(response.text)
# except:
#     print('获取数据失败')

# import requests
# response=requests.get(url='http://www.baidu.com',timeout=3)
# if response.status_code==200:
#     print(response.content.decode())


#verify  ：False  不遵循SSL, True：遵循SSL

# import requests
# try:
#     # response=requests.get(url='http://www.baidu.com',timeout=1,verify=False)
#     response=requests.get(url='http://www.baidu.com',timeout=0.01,veriyf=True)
#     print(response.text)
# except Exception as e:
#     print('获取数据错误',e)

# import requests
# try:
#     response=requests.get(url='http://www.baidu.com',timeout=0.01,verify=False)
#     print(response.text)
# except Exception as f:
#     print('获取数据错误',f)



# import requests
# from retrying import retry
# @retry(stop_max_attempt_number=3)
# def getHTML(url):
#     print('aaa')
#     global c
#     c += 1
#     try:
#         response=requests.get(url=url,timeout=0.001,verify=False)
#         print(response.text)
#     except Exception as e:
#         print('失败',e)
#
# if __name__ == '__main__':
#     c=0
#     try:
#         getHTML('http://www.baidu.com')
#     except:
#         pass
#     print(c)


# import os
# os.rename('_02json.py','timeout_retry.py')

# import requests
# from retrying import retry
# @retry(stop_max_attempt_number=3)
# def getHTML(url):
#     response=requests.get(url=url,timeout=1,verify=False)
#     print(response.text)
# if __name__ == '__main__':
#     getHTML('http://www.baidu.com')


# import requests,time
# from retrying import retry
# url='https://www.baidu.com'
# @retry(stop_max_attempt_number=3)
# def getHTML(url):
#     print('111')
#     response = requests.get(url=url, timeout=1, verify=False)
#     # print(response.text)
# if __name__ == '__main__':
#     getHTML('https://www.baidu.com')
#     time.sleep(2)
#     print('adsdasdsaasd')

dict={'name':1,'age':2,'sex':3}
for x,y in dict.items():
    print(x,y)
