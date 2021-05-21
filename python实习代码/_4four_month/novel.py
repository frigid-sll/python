import os,requests
from lxml import etree
url='http://www.17k.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
response=requests.get(url=url,headers=headers,verify=False)
html=etree.HTML(response.text)
list=html.xpath("//div[@class='BJTJ']//li[1]/a[2]/@href")
# print(list)
url2=str(list[0]).replace('book','list')
# print(url2)
response=requests.get(url=url2)
html=etree.HTML(response.text)
list=html.xpath("//dl[@class='Volume'][1]/dd/a/@href")
# print(list)
listUrl=[]
for x in list:
    listUrl.append('http://www.17k.com'+x)
# print(listUrl)
os.mkdir('小说')
os.chdir('./小说')
for x in range(len(listUrl)):
    with open('第%d章.txt'%(x+1),mode='w',encoding='utf8') as f:
        response=requests.get(url=listUrl[x])
        response.encoding='utf8'
        html=etree.HTML(response.text)
        title=html.xpath("//div[@class='readAreaBox content']/h1/text()")
        content=html.xpath("//div[@class='p']/text()")
        f.write(''.join(title))
        f.write('\n')
        f.write(''.join(content).replace(' ',''))



