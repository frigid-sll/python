```python
#爬新闻标题  复习

# from selenium import webdriver
# import requests
# from pymysql import connect

# conn=connect(host='localhost',user='root',password='mysql',database='news',charset='utf8')
# driver=webdriver.Chrome()
# cursor=conn.cursor()

# url='https://www.xuexi.cn/f997e76a890b0e5a053c57b19f468436/018d244441062d8916dd472a4c6a0a0b.html'

# driver.get(url=url)

# driver.implicitly_wait(10)

# list_content=driver.find_elements_by_xpath('//*[@id="b50e"]/div/div/div/div/div/section/div/div/div/div/div[2]/section/div/div/div/div/div/div/div/div/span')

# for x in list_content:
#     x.click()
#     windows=driver.window_handles
#     driver.switch_to.window(windows[-1])
#     title=driver.find_element_by_xpath('//*[@id="Cd1smadng91s00"]/p').text
#     sql="insert into news values('%s')"%title
#     cursor.execute(sql)
#     conn.commit()
#     driver.close()
#     driver.switch_to.window(windows[0])

# driver.close()
# cursor.close()
# conn.close()
```

