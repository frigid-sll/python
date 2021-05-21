# import re
# content='''bbb123ab<A>12345
# 6</A>cd123123b<A>abc</A>56<a>7c</a>d'''
# print(re.findall('<[A,a]>([0-9,\n]+?)</[A,a]>',content,re.S))


# import re,requests
# response=requests.get(url='https://www.kuaidaili.com/free/')
# # print(response.text)
# listIp=re.findall('<td data-title="IP">(.*)</td>',response.text)
# listPort=re.findall('<td data-title="PORT">(.*)</td>',response.text)
# list=[]
# for x in range(len(listIp)):
#     list.append('%s:%s'%(listIp[x],listPort[x]))
# print(list)


# import requests
# url='https://www.kuaidaili.com/free/'
# from lxml import etree
# response=requests.get(url=url)
# html=etree.HTML(response.text)
# content=html.xpath("//table[@class='table table-bordered table-striped']//th[position()<3]/text()")
#
# print(content)
# import re
#
# def funcsum(str):
#     list=re.findall('\d+',str)
#     print(sum([int(x) for x in list]))
#     # for x in list:
#     #     sum+=int(x)
#     # print(sum)
# if __name__ == '__main__':
#     str=input("Please Input str：")
#     funcsum(str)


# for x in range(1625,1646):
#     url = 'http://www.doupobook.com/doupo/%d.html'%x
#     import requests, json, jsonpath
#     from lxml import etree
#     response = requests.get(url=url)
#     html = etree.HTML(response.content.decode())
#     content = html.xpath("//div[@class='main']//h1/text()")
#     content2 = html.xpath("//div[@class='entry-text']/div/p/text()")
#     with open(file='斗破苍穹.txt', mode='a', encoding='utf-8') as f:
#         json.dump(content, f, ensure_ascii=False, indent=2)
#         json.dump(content2, f, ensure_ascii=False, indent=2)

# from pymysql import connect
# conn=connect(host='localhost',port=3306,database='斗破苍穹',user='root',password='qwq',charset='utf8')
# cur=conn.cursor()
# with open('斗破苍穹.txt',mode='r',encoding='utf8') as f:
#     content=f.readlines()
#     print(content)
#     cur.execute("insert into a values(%s)"%'asd')
# conn.commit()







