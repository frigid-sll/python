import requests,json
from bs4 import BeautifulSoup

def Get(i):
    url = 'http://www.abckg.com/index_%d.html'%i
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')
    listTitle = soup.select(' div.post > h2 > a')
    for x in listTitle:
        dict = {}
        dict['Title'] = x.get_text()
        dict['Url'] = x.get('href')
        response2 = requests.get(url=x.get('href'))
        soup2 = BeautifulSoup(response2.text, 'lxml')
        dict['content'] = soup2.select('#post-1192 > dd > p')[0].get_text()
        listAll.append(dict)

def Write():
    with open('JD.json', mode='w', encoding='utf8') as f:
        json.dump(listAll, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    listAll = []
    for i in range(1,11):
        Get(i)
    Write()

# import requests,json,jsonpath
# from bs4 import BeautifulSoup
#
# class Daili:
#     def GetTitle(self):
#         self.content=json.loads(response.text)
#         self.listTitle=jsonpath.jsonpath(self.content,'$..title')
#         # print(self.listTitle)
#
#     def GetImg(self):
#         self.listImgUrl=jsonpath.jsonpath(self.content,'$..result.list.thumb')
#         print(type(self.listImgUrl))
#         for x in self.listImgUrl:
#             # print(x)
#             response2=requests.get(url=x,headers=headers,verify=False)
#             with open('{}.jpg'.format(x),mode='wb') as f:
#                 f.write(response2.content)
#
#
#
# if __name__ == '__main__':
#     url=' https://www.cnbeta.com/home/more?&type=all&page=2&_csrf=7zMm-D-OHDgfH2jyq-cimhBkSS9akKZINNxpvULd4D2OXW2gS91eT1lPO6rJ1GGtQxwMYTb8zhJRqVGMMYyudw%3D%3D&_=1550111873469'
#     headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}
#     response=requests.get(url=url,headers=headers,verify=False)
#     # print(response.text)
#     if response.status_code==200:
#         daili=Daili()
#         daili.GetTitle()
#         daili.GetImg()


# import requests
# from selenium import webdriver
#
# class Daili:            #定义一个类
#     def GetTitle(self):           #定义一个抓取网页标题的方法
#         self.listTitle=driver.find_elements_by_xpath("//div[@class='item']//dt/a")         #用driver.find_elements_by_xpath()方法获取标题元素，括号内写标题的xpath路径
#         for x in range(len(self.listTitle)):              #根据下表循环遍历该列表
#             self.listTitle[x]=self.listTitle[x].text       #将每个列表里的每个元素修改为内容，用.text
#         # print(self.listTitle)
#
#     def GetImg(self):             #定义一个抓取网页图片的方法
#         self.listImgUrl=driver.find_elements_by_xpath("//div[@class='item']//dl/a/img[@class='lazy']")  #用driver.find_elements_by_xpath()方法获取图片元素，括号内写图片的xpath路径
#         for x in range(len(self.listImgUrl)):            #根据下表循环遍历该列表
#             self.listImgUrl[x]=self.listImgUrl[x].get_attribute('src')      #将每个列表里的每个元素修改为图片,用.get_attribute()方法  括号内写你要抓取的标签属性，记得加引号
#             with open('%d.jpg'%x,mode='wb') as f:              #打开文件，以二进制的方法打开新建，因为是图片，后缀名为.jpg
#                 response=requests.get(url=self.listImgUrl[x])          #响应图片网址的内容
#                 f.write(response.content)                       #将图片内容写入文件  将相当于下载了
#         # print(self.listImgUrl)
#
# if __name__ == '__main__':
#     driver=webdriver.Chrome()
#     driver.get(url='https://www.cnbeta.com/')
#     driver.implicitly_wait(10)
#     daili=Daili()              #定义一个对象来接收上面那个类
#     daili.GetTitle()          #执行GetTitle()这个方法
#     daili.GetImg()              #执行GetImg()这个方法


