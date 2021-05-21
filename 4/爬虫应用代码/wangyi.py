from selenium import webdriver
import time

driver=webdriver.Chrome()

url='http://fanyi.youdao.com/'

driver.get(url)

driver.find_element_by_xpath('//*[@id="inputOriginal"]').send_keys('good')
driver.find_element_by_xpath('//*[@id="transMachine"]').click()

time.sleep(0.1)

result=driver.find_element_by_xpath('//*[@id="transTarget"]').text

print(result)


driver.close()
