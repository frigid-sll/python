import re,requests,json
url='http://news.ikanchai.com/'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}
response=requests.get(url=url,headers=headers)
content=response.content.decode()
with open('1.txt',mode='w',encoding='utf8') as f:
    f.write(content)
list1=re.findall(' <div class="."><a href=(.+)>.*?</a>',content)
list2=[]
for x in range(len(list1)):
    if x%2==1:
        list2.append(list1[x])
listUrl=[]
for x in list2:
    dict={}
    dict['url']=x.replace('target="_blank"',' ')
    listUrl.append(dict)
print(listUrl)
with open('content2.json',mode='w',encoding='utf8') as f:
    json.dump(listUrl,f,ensure_ascii=False)







