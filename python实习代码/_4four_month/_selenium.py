# from pymysql import connect
# conn=connect(host='localhost',user='root',password='mysql',database='selenium',port=3306,charset='utf8')
#
# cur=conn.cursor()
#
# from selenium import webdriver
# driver=webdriver.Chrome()
#
#
# for x in range(1,4):
#     url='https://www.zhipin.com/c101210100-p100109/?page={}&ka=page-{}'.format(x,x)
#     driver.get(url=url)
#     driver.implicitly_wait(5)
#     listTitle=driver.find_elements_by_xpath("//div[@class='job-list']/ul/li//div[@class='job-title']")
#     listSalary=driver.find_elements_by_xpath("//div[@class='job-list']/ul/li//span[@class='red']")
#     for i in range(len(listTitle)):
#         sql='insert into data VALUES ("%s","%s")'%(listTitle[i].text,listSalary[i].text)
#         cur.execute(sql)
#
# conn.commit()
# cur.close()
# conn.close()
#
# driver.close()

# 导包
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains   #双击按钮需要导入的包

#初始化引擎，打开页面
driver=webdriver.Chrome()
url='https://www.mikecrm.com/login.php'
driver.get(url=url)
driver.implicitly_wait(5)   #隐士等待，等待页面元素加载完毕

#登陆
driver.find_element_by_xpath('//*[@id="login_wrapper"]/div/div[1]/div/div/div[2]/div[2]/div[2]/div/div[1]/input').send_keys('1511720234@qq.com')
time.sleep(0.1)
driver.find_element_by_xpath('//*[@id="login_wrapper"]/div/div[1]/div/div/div[2]/div[2]/div[3]/div/div[1]/input').send_keys('Bao087671.')
time.sleep(0.1)
driver.find_element_by_xpath('//*[@id="login_wrapper"]/div/div[1]/div/div/div[2]/div[2]/div[4]/a').click()
driver.implicitly_wait(5)

#点击表单按钮
driver.find_element_by_xpath('//*[@id="header"]/div/div/ul/li[2]/a').click()
driver.implicitly_wait(5)

#点击查看反馈
driver.find_element_by_xpath('//*[@id="mklgscrollcom914"]/ul/li[2]/div/div[2]/p/a').click()
driver.implicitly_wait(5)



for x in range(39,45):
    # 出现详情页面
    appear = driver.find_element_by_xpath('//*[@id="mklgscrollcom915"]/ul/li[{}]'.format(x))
    ActionChains(driver).double_click(appear).perform()
    time.sleep(1)

    print(driver.find_element_by_xpath('//*[@id="mklgscrollcom916"]/ul/li[1]/div/div[1]/p').text)

    # 使详情页面消失
    disappear = driver.find_element_by_xpath('//*[@id="mklgscrollcom915"]/ul/li[{}]/div/div[3]/a'.format(x)).click()
    time.sleep(1)
#
#     driver.execute_script("arguments[0].scrollIntoView(false);", appear)
    # js = "var q=document.documentElement.scrollTop=10000"
    # driver.execute_script(js)
    # time.sleep(2)


# from selenium import webdriver
#
# #初始化驱动
# driver=webdriver.Chrome()
# #请求页面
# driver.get(url='https://sou.zhaopin.com/?jl=530&kw=python&kt=3')
# #找到对应标签，发送文本
# # driver.find_element_by_xpath("//*[@id='kw']").send_keys('2019')
#
# #找到按钮，点击click
#
# driver.implicitly_wait(10)
#
# driver.switch_to.frame('ptlogin_iframe')
#
# driver.find_element_by_xpath('//*[@id="listContent"]/div[1]/div/a/div[1]/div[1]/span[1]').click()
#获取页面内容
# content=driver.page_source
# print(content)
# #解析页面

# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get(url='https://www.baidu.com')
# driver.find_element_by_xpath("//*[@id='kw']").send_keys('2019')
# driver.find_element_by_xpath("//*[@id='su']").click()
# driver.implicitly_wait(10)
# driver.find_element_by_xpath('//*[@class="t c-gap-bottom-small"]/a').click()
# content=driver.page_source
# print(content)


# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get(url='https://www.baidu.com')
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys('2019')
# driver.find_element_by_xpath('//*[@id="su"]').click()
# driver.implicitly_wait(10)
# listContent=[]
# for x in range(1,10):
#     content=driver.find_element_by_xpath("//*[@id=%d]/h3/a"%x).text
#     listContent.append(content)
# print(listContent)

# from selenium import webdriver
#
# driver=webdriver.Chrome()
# driver.get(url='https://movie.douban.com/')
# # listTitle=driver.find_elements_by_xpath("//div[@class='slide-page']/a/p")
# listTitle=driver.find_elements_by_xpath('//*[@id="content"]/div/div[2]/div[4]/div[3]/div/div[1]/div/div[2]/a/p')
# # listTitle2=[]
# # for x in listTitle:
# #     listTitle2.append(x.text)
# # print(''.join(listTitle2))
# for x in listTitle:
#     print(x.text)


# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get(url='http://www.ruanyifeng.com/survivor/collapse/index.html')
# listTitle=driver.find_elements_by_xpath('/html/body/section/div/div[1]/div[2]/nav/div/aside/ul/li/ul/li/a/span[2]')
# for x in listTitle:
#     print(x.text)

# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get(url='https://www.baidu.com')




# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get(url='http://www.ruanyifeng.com/survivor/collapse/index.html')
# #隐士等待
# driver.implicitly_wait(10)
# #点击事件
# driver.find_element_by_xpath('/html/body/section/div/div[1]/div[1]/article/ul/li[1]/a').click()
# #切换窗口
# windows=driver.window_handles
# driver.switch_to.window(windows[1])
# #获取详细页面里面的内容
# content=driver.find_element_by_xpath('/html/body/section/div/div[1]/div[1]/article/p[16]')
# print(content.text)
# #关闭当前窗口
# driver.close()



# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get(url='http://www.ruanyifeng.com/survivor/collapse/index.html')
# driver.implicitly_wait(10)
# driver.find_element_by_xpath('/html/body/section/div/div[1]/div[1]/article/ul/li[1]/a').click()
# windows=driver.window_handles
# driver.switch_to.window(windows[1])
# content=driver.find_element_by_xpath('/html/body/section/div/div[1]/div[1]/article/p[14]')
# print(content.text)
# driver.close()




# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get(url='http://www.ruanyifeng.com/survivor/collapse/index.html')
# driver.implicitly_wait(10)
# listTitle=driver.find_elements_by_xpath('/html/body/section/div/div[1]/div[1]/article//ul/li/a')
# # print(len(listTitle))
# for x in range(len(listTitle)):
#     driver.find_element_by_xpath('/html/body/section/div/div[1]/div[1]/article//ul/li[%d]/a'%(x+1)).click()
#     windows=driver.window_handles
#     driver.switch_to.window(windows[1])
#     content=driver.find_element_by_xpath('/html/body/section/div/div[1]/div[1]/article/p[3]')
#     print(content.text)
#     driver.close()
#     driver.switch_to.window(windows[0])
#
# #退出
# driver.quit()




# import re
# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get(url='http://www.ruanyifeng.com/survivor/collapse/index.html')
# driver.implicitly_wait(10)
# listTitle=driver.find_elements_by_xpath('/html/body/section/div/div[1]/div[1]/article//ul/li/a')
# def removeTags(content):
#     content=re.findall("(?<=[(])[^()]+\.[^()]+(?=[)])",content)
#     return content
#
# for x in range(len(listTitle)):
#     driver.find_element_by_xpath('/html/body/section/div/div[1]/div[1]/article//ul/li[%d]/a'%(x+1)).click()
#     windows=driver.window_handles
#     driver.switch_to.window(windows[1])
#     content=re.findall('<article class="content is-size-4-desktop">(.*)</article>',driver.page_source,re.S)
#     print(removeTags(''.join(content)))
#     driver.close()
#     driver.switch_to.window(windows[0])




# from selenium import webdriver
# from pymysql import connect
# import json
#
# conn=connect(host='localhost',port=3306,database='car',user='root',password='mysql',charset='utf8')
# cur=conn.cursor()
# driver=webdriver.Chrome()
#
# url_list=[chr(x) for x in range(65,91)]
#
# # for x in url_list:
# driver.get(url='https://www.autohome.com.cn/grade/carhtml/{}.html'.format('A'))
# pinpai_list=[m.text for m in driver.find_elements_by_xpath('//dt/div/a')]
# classify_list=[[m.text for m in driver.find_elements_by_xpath('html/body/dl[{}]//dd/div/a'.format(y))] for y in range(1,len(pinpai_list)+1)]
# details=[{'pinpai':detail} for detail in [[{classify_list[y-1][key-1]:[m.text for m in driver.find_elements_by_xpath('html/body/dl[{}]/dd/ul[{}]/li/h4'.format(y,key))]} for key in range(1,len(classify_list[y-1])+1)] for y in range(1,len(pinpai_list)+1)]]
# for m in range(len(details)):
#     details[m][pinpai_list[m]]=details[m].pop('pinpai')
#
# for g in details:
#     for key,value in g.items():
#         for f in value:
#             for key2,value2 in f.items():
#                 for d in value2:
#                     sql = "insert into car VALUES ('%s','%s','%s')" % (key,key2,d)
#                     cur.execute(sql)
#
# conn.commit()
# cur.close()
# conn.close()
#
#
#
# # with open('student.json',mode='w',encoding='utf8') as f:
# #    json.dump(details,f,ensure_ascii=False,indent=2)
#
# driver.close()






















