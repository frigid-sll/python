import requests
from lxml import etree

class CatEye(object):
    def __init__(self,response):
        self.html=etree.HTML(response.text)

    def GetTitle(self):
        self.listTitle=self.html.xpath("//div[@class='main']//p[@class='name']/a/text()")
        # print(self.listTitle)

    def GetAdd(self):
        self.listAdd=self.html.xpath("//div[@class='main']//p[@class='month-wish']/span/span/text()")

    def GetAll(self):
        self.listAll=self.html.xpath("//div[@class='main']//p[@class='total-wish']/span/span/text()")

    def GetContent(self):
        self.listUrl=self.html.xpath("//div[@class='main']//p[@class='name']/a/@href")
        self.listUrl2=[]
        for x in self.listUrl:
            self.listUrl2.append('https://maoyan.com'+x)
        self.listContent=[]
        for x in self.listUrl2:
            response2=requests.get(url=x,headers=headers,verify=False)
            html2=etree.HTML(response2.text)
            content=html2.xpath("//*[@id='app']/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/span/text()")
            self.listContent.append(''.join(content))
        print(self.listContent)

if __name__ == '__main__':
    url='https://maoyan.com/board/6'
    headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    response=requests.get(url=url,headers=headers,verify=False)
    cateye=CatEye(response)
    # cateye.GetTitle()
    cateye.GetContent()








