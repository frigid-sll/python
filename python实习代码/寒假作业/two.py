import requests
from lxml import etree

class Joke(object):
    def __init__(self,response):
        self.html=etree.HTML(response)

    def GetTitle(self):
        self.listTitle=self.html.xpath("//div[@class='list_title']//b/a/text()")
        print(self.listTitle)

    def GetContent(self):
        self.listUrl=self.html.xpath("//div[@class='list_title']//b/a/@href")
        print(self.listUrl)
        self.listUrl2=[]
        self.listContent=[]
        for x in self.listUrl:
            self.listUrl2.append('http://www.jokeji.cn'+x)
        print(self.listUrl2)
        # for x in self.listUrl2:
        #     response2=requests.get(url=x,headers=headers,verify=False)
        #     html2=etree.HTML(response2.text)
        #     self.listContent.append(html2.xpath("//div[@class='left']//span[@id='text110']/p/text()"))
        # print(self.listContent)

if __name__ == '__main__':
    url='http://www.jokeji.cn/list_9.htm'
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    response=requests.get(url=url,headers=headers,verify=False)
    if response.status_code==200:
        response.encoding='gbk'
        joke=Joke(response.text)
        joke.GetTitle()
        joke.GetContent()







