import requests
# url='https://www.baidu.com/s?'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
# response=requests.get(url=url,headers=headers,verify=False)
# if response.status_code==200:
    # print(response.content.decode())
params={'wd':'python'}
url='https://www.baidu.com/s?wd=python&a=c'
# response=requests.get(url=url,headers=headers,verify=False,params=params)
response=requests.get(url=url,headers=headers,verify=False)
with open('python.html',mode='w',encoding='utf8') as f:
    f.write(response.text)




