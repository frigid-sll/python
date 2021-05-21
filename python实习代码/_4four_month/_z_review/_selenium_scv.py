from selenium import webdriver
import csv
driver=webdriver.Chrome()
url='http://www.abckg.com/'
driver.get(url=url)
listTitle = driver.find_elements_by_xpath('//*[@id="container"]/div[1]/div/h2/a')
for x in range(len(listTitle)):
    listTitle[x]=listTitle[x].text
listContent=[]
for x in range(2,5):
    driver.find_element_by_xpath('//*[@id="container"]/div[1]/div[{}]/h2/a'.format(x)).click()
    windows = driver.window_handles
    driver.switch_to.window(windows[1])
    Content = driver.find_element_by_xpath('//*[@id="post-1192"]/dd/p').text
    listContent.append(Content)
    driver.close()
    driver.switch_to.window(windows[0])
# print(len(windows))
list=[]
for x in range(len(listContent)):
    dict1={}
    dict1['title']=listTitle[x]
    dict1['content']=listContent[x]
    list.append(dict1)
# print(list)
fieldnames=['title','content']
with open('JD.csv',mode='a',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(list)

with open('JD.csv',mode='r') as f:
    reader=csv.DictReader(f)
    for x in reader:
        print(dict(x))


# print(list)






