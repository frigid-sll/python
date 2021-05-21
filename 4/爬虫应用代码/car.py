from selenium import webdriver
from pymysql import connect
import json

conn=connect(host='localhost',port=3306,database='car',user='root',password='mysql',charset='utf8')
cur=conn.cursor()
driver=webdriver.Chrome()

url_list=[chr(x) for x in range(65,91)]

for x in url_list:
    driver.get(url='https://www.autohome.com.cn/grade/carhtml/{}.html'.format(x))
    pinpai_list=[m.text for m in driver.find_elements_by_xpath('//dt/div/a')]
    classify_list=[[m.text for m in driver.find_elements_by_xpath('html/body/dl[{}]//dd/div/a'.format(y))] for y in range(1,len(pinpai_list)+1)]
    details=[{'pinpai':detail} for detail in [[{classify_list[y-1][key-1]:[m.text for m in driver.find_elements_by_xpath('html/body/dl[{}]/dd/ul[{}]/li/h4'.format(y,key))]} for key in range(1,len(classify_list[y-1])+1)] for y in range(1,len(pinpai_list)+1)]]
    for m in range(len(details)):
        details[m][pinpai_list[m]]=details[m].pop('pinpai')

    for g in details:
        for key,value in g.items():
            for f in value:
                for key2,value2 in f.items():
                    for d in value2:
                        sql = "insert into car VALUES ('%s','%s','%s')" % (key,key2,d)
                        cur.execute(sql)

conn.commit()
cur.close()
conn.close()
driver.close()

