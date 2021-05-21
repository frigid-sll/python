import requests
from lxml import etree
from pymysql import connect

class Goods(object):
    def __init__(self,response):
        self.html=etree.HTML(response.text)

    def GetName(self):
        self.listName=self.html.xpath("//div[@id='J_goodsList']//div[@class='p-name p-name-type-2']//em/text()")
        # print(self.listName)

    def GetPrice(self):
        self.listPrice=self.html.xpath("//div[@id='J_goodsList']//div[@class='p-price']//i/text()")
        # print(self.listPrice)

    def GetAll(self):
        self.listAll=[]
        for x in range(len(self.listPrice)):
            dict={}
            dict['Name']=self.listName[x]
            dict['Price']=self.listPrice[x]
            self.listAll.append(dict)
        return self.listAll

if __name__ == '__main__':
    for y in range(1,4,2):
        url ='https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page={}&s=58&click=0'.format(y)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
        response = requests.get(url=url, headers=headers, verify=False)
        response.encoding = 'utf8'
        if response.status_code == 200:
            goods = Goods(response)
            goods.GetName()
            goods.GetPrice()
            conn = connect(host='localhost', port=3306, database='vacation', user='root', password='qwq', charset='utf8')
            cursor=conn.cursor()
            for i in goods.GetAll():
                for key,value in i.items():
                    if key=='Name':
                        cursor.execute("insert into content(name) VALUES('%s') "%value)
                        name=value
                    else:
                        cursor.execute("update content set price=%.2f where name= '%s'"%(float(value),name))
            conn.commit()











