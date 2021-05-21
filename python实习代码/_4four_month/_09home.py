import requests
from lxml import etree
# for y in range(1,19):
#     url = 'https://bj.fang.lianjia.com/loupan/pg%d/'%y
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
#     response = requests.get(url=url, headers=headers, verify=False, timeout=2)
#     if response.status_code == 200:
#         html = etree.HTML(response.content.decode())
#         listTitle = html.xpath("//div[@class='resblock-name']//a/text()")
#         listAddress1 = html.xpath("//div[@class='resblock-location']/span[1]/text()")
#         listAddress2 = html.xpath("//div[@class='resblock-location']/span[2]/text()")
#         listAddress3 = html.xpath("//div[@class='resblock-location']/a/text()")
#         listAddress = []
#         for x in range(len(listAddress1)):
#             s = listAddress1[x] + '/' + listAddress2[x] + '/' + listAddress3[x]
#             listAddress.append(s)
#         listPrice1 = html.xpath("//div[@class='main-price']/span[@class='number']/text()")
#         listPrice2 = html.xpath("//div[@class='main-price']/span[2]/text()")
#         listPrice = []
#         # print(listPrice1)
#         # print(listPrice2)
#         for x in range(len(listPrice1)):
#             s = listPrice1[x] + listPrice2[x]
#             listPrice.append(s)
#         listImg=html.xpath("//img[@class='lj-lazy']/@src")
#         # print(listPrice)
#         # print(len(listAddress))
#         # print(len(listTitle))
#         for x in range(len(listTitle)):
#             with open('1.txt', mode='a', encoding='utf8') as f:
#                 f.write('标题：' + listTitle[x])
#                 f.write('   ')
#                 f.write('地址：' + listAddress[x])
#                 f.write('   ')
#                 f.write('价格：' + listPrice[x])
#                 f.write('   ')
#                 f.write('图片：'+listImg[x])
#                 f.write('\n')

# import requests,re
# from lxml import etree
# for y in range(1,11):
#     url = 'https://bj.fang.lianjia.com/loupan/pg/pg%d/'%y
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
#     response = requests.get(url, headers=headers, verify=False)
#     if response.status_code == 200:
#         html = etree.HTML(response.text)
#         listTile = html.xpath("//div[@class='resblock-name']/a/text()")
#         # print(listTile)
#         listAddress1 = html.xpath("//div[@class='resblock-location']/span[1]/text()")
#         # print(listAddress1)
#         listAddress2 = html.xpath("//div[@class='resblock-location']/span[2]/text()")
#         # print(listAddress2)
#         listAddress3 = html.xpath("//div[@class='resblock-location']/a/text()")
#         # print(listAddress3)
#         listAddress = []
#         for x in range(len(listAddress1)):
#             listAddress.append(listAddress1[x] + '/' + listAddress2[x] + '/' + listAddress3[x])
#         # print(listAddress)
#         listPrice1 = html.xpath("//div[@class='main-price']/span[1]/text()")
#         # print(listPrice1)
#         listPrice2 = html.xpath("//div[@class='main-price']/span[2]/text()")
#         # print(listPrice2)
#         listTotalPrice = html.xpath("//div[@class='second']/text()")
#         # print(listTotalPrice)
#         listPrice = []
#         for x in range(len(listPrice1)):
#             listPrice.append(listPrice1[x] + re.sub(' ','',listPrice2[x]))
#         # print(listPrice)
#         for x in range(len(listTile)):
#             with open('1.txt', mode='a', encoding='utf8') as f:
#                 f.write('标题:' + listTile[x])
#                 f.write('   ')
#                 f.write('地址：' + listAddress[x])
#                 f.write('   ')
#                 f.write('价格:' + listPrice[x])
#                 f.write('   ')
#                 f.write('\n')



# import requests,os,json
# from lxml import etree
# url='http://www.17k.com/'
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
# response=requests.get(url=url,headers=headers,verify=False)
# if response.status_code==200:
#     html=etree.HTML(response.text)
#     listUrl=html.xpath("//div[@class='BJTJ']//li[1]/a[2]/@href")
#     # print(listUrl)
#     url=str(listUrl[0]).replace('book','list')
#     # print(url)
#     response=requests.get(url=url,headers=headers,verify=False)
#     if response.status_code==200:
#         html=etree.HTML(response.text)
#         listUrl=html.xpath("//div[@class='Main List']//dd//a/@href")
#         # print(listUrl)
#         list=[]
#         for x in listUrl:
#             list.append("http://www.17k.com"+x)
#         # print(list)
#         os.mkdir('小说2')
#         os.chdir('./小说2')
#         for x in range(len(list)):
#             response=requests.get(url=list[x],headers=headers,verify=False)
#             response.encoding='utf8'
#             html=etree.HTML(response.text)
#             listTitle=html.xpath("//div[@class='readAreaBox content']/h1/text()")
#             listContent=html.xpath("//div[@class='p']/text()")
#             with open('第%d章.txt'%(x+1),mode='w',encoding='utf8') as f:
#                 f.write(''.join(listTitle))
#                 # json.dump(''.join(listTitle),f,ensure_ascii=False,indent=2)
#                 f.write('\n')
#                 # json.dump(''.join(listContent).replace(' ',''),f,ensure_ascii=False,indent=2)
#                 f.write(''.join(listContent).replace(' ',''))



# class Novel(object):
#     def __init__(self,response,headers):
#         self.response=response
#         self.headers=headers
#
#     def GetTitle(self):
#         self.html = etree.HTML(response.text)
#         self.listTile = self.html.xpath("//div[@class='resblock-name']/a/text()")
#         return self.GetAddress()
#
#     def GetAddress(self):
#         self.listAddress1 = self.html.xpath("//div[@class='resblock-location']/span[1]/text()")
#         # print(listAddress1)
#         self.listAddress2 = self.html.xpath("//div[@class='resblock-location']/span[2]/text()")
#         # print(listAddress2)
#         self.listAddress3 = self.html.xpath("//div[@class='resblock-location']/a/text()")
#         # print(listAddress3)
#         self.listAddress = []
#         for x in range(len(self.listAddress1)):
#             self.listAddress.append(self.listAddress1[x] + '/' + self.listAddress2[x] + '/' + self.listAddress3[x])
#         return self.GetPrice()
#
#     def GetPrice(self):
#         self.listPrice1 = self.html.xpath("//div[@class='main-price']/span[1]/text()")
#         # print(listPrice1)
#         self.listPrice2 = self.html.xpath("//div[@class='main-price']/span[2]/text()")
#         # print(listPrice2)
#         self.listPrice = []
#         for x in range(len(self.listPrice1)):
#             self.listPrice.append(self.listPrice1[x] + re.sub('\s','',self.listPrice2[x]))
#         return self.GetPhone()
#
#     def GetPhone(self):
#         self.listUrl1 = self.html.xpath("/html/body/div[4]/ul[2]/li/div/div[1]/a/@href")
#         self.listUrl=[]
#         for x in self.listUrl1:
#             self.listUrl.append('https://bj.fang.lianjia.com'+x)
#         self.listPhone=[]
#         for x in range(len(self.listUrl)):
#             self.response2=requests.get(url=self.listUrl[x],headers=self.headers,verify=False)
#             self.html2=etree.HTML(self.response2.text)
#             self.listPhone.append(''.join(self.html2.xpath("/html/body/div[2]/div[2]/div[4]/div[2]/div[2]/div/div[3]/div/span/text()")))
#         return self.GetRoom()
#
#     def GetRoom(self):
#         self.room = []
#         for x in range(len(self.listAddress)):
#             self.dict = {}
#             self.dict['Title'] = self.listTile[x]
#             self.dict['Address'] = self.listAddress[x]
#             self.dict['Price'] = self.listPrice[x]
#             self.dict['Phone']=self.listPhone[x]
#             self.room.append(self.dict)
#         return self.room
#
# if __name__ == '__main__':
#     import re,requests
#     from lxml import etree
#     Room=[]
#     for x in range(1,10):
#         url = 'https://bj.fang.lianjia.com/loupan/pg/pg%d/'%x
#         headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
#         response = requests.get(url, headers=headers, verify=False)
#         if response.status_code == 200:
#             novel = Novel(response,headers)
#             room= novel.GetTitle()
#             Room.append(room)
#     print(Room)







# url = 'https://bj.fang.lianjia.com/loupan/pg1/'
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
# response = requests.get(url=url, headers=headers, verify=False, timeout=2)
# if response.status_code==200:
#     html=etree.HTML(response.text)
#     listUrl1=html.xpath("/html/body/div[4]/ul[2]/li/div/div[1]/a/@href")
#     print(listUrl1)
#     listUrl = []
#     for x in listUrl1:
#         listUrl.append('https://bj.fang.lianjia.com'+x)
#     listPhone=[]





import requests
url='http://uland.taobao.com/sem/tbsearch?refpid=mm_26632258_3504122_32538762&clk1=7adc8e57c20eb8dc3cb829ba55bffc29&keyword=%E5%8D%8E%E4%B8%BA&page=0'
session=requests.session()
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
           "Cookie":"t=f8d0a009231e2e486d1b5a32c023159e; miid=1141289666719644149; ctoken=UX2XZPfYSPam_IH_7tun6-cv; cna=8EW0FKE34DQCASQXX3fs9ggQ; _m_h5_tk=051f8eecae8f2ec2e2ff991ab561567f_1548301253144; _m_h5_tk_enc=ceec83fa8553dd9d4455a089a6354154; cookie2=10fff20292a842c150b8944cdfe9947d; v=0; _tb_token_=5701339fbe374; unb=2200550140192; sg=727; _l_g_=Ug%3D%3D; skt=f5de11d3fe09a235; cookie1=U7ShGuIy4nQzr%2FJ%2Fg9tHRQXN0PMuH1Ki0xBw0KZSBCg%3D; csg=33ca0ffb; uc3=vt3=F8dByE%2BtDqGM%2BeOeD58%3D&id2=UUphyuwMII7iGH3zuw%3D%3D&nk2=F5RARJ4WPMyeSpo%3D&lg2=UtASsssmOIJ0bQ%3D%3D; existShop=MTU0ODI5MzQ0Nw%3D%3D; tracknick=tb561965967; lgc=tb561965967; _cc_=U%2BGCWk%2F7og%3D%3D; dnk=tb561965967; _nk_=tb561965967; cookie17=UUphyuwMII7iGH3zuw%3D%3D; tg=0; l=Avz8FYtzw9WUbVksxJZkHm/WTJCu5qAf; mt=ci=0_1; thw=cn; uc1=cookie14=UoTYPmOxEfGHRw%3D%3D&lng=zh_CN&cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&existShop=false&cookie21=UtASsssme%2BBq&tag=8&cookie15=Vq8l%2BKCLz3%2F65A%3D%3D&pas=0; isg=BHl5Fg7BASHexd21HlHAfy7ViOX_lkQY6gXTN5uu9aAfIpm049Z9COdwoGZxmgVw"}
response = session.get(url,headers=headers)
response.encoding="utf8"
print(response.text)











