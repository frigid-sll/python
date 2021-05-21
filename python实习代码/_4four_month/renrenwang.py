import requests,re
from lxml import etree
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
data={'email':'13439770580','password':'123456xbh'}
url='http://www.renren.com/PLogin.do'
session=requests.session()
response=session.post(url=url,headers=headers,data=data,verify=False)
if response.status_code==200:
    html=etree.HTML(response.text)
    url=html.xpath("//*[@id='nxHeader']/div/div/div/dl/dd/a[1]/@href")
    url=''.join(url)
    response=session.get(url=url,headers=headers,verify=False)
    print(response.text)

