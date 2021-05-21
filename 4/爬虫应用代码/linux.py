from selenium import webdriver
import re
import os

os.mkdir('D:/linux')

driver=webdriver.Chrome()

url='https://www.runoob.com/linux/linux-tutorial.html'

driver.get(url=url)

a_len=len(driver.find_element_by_xpath("//div[@id='leftcolumn']").find_elements_by_xpath('a'))

for a in range(1,a_len):

	html = driver.execute_script("return document.documentElement.outerHTML")
	content='\n'.join(re.findall('<div class="article-body">(.*)<div class="previous-next-links">',html,re.S))
	name='D:/linux/{}'.format(a)+driver.find_element_by_xpath("//div[@id='leftcolumn']/a[{}]".format(a)).text+'.md'

	try:
		with open(name,'w',encoding='utf8') as f:
			f.write(content)
	except:
		pass
	else:
		driver.find_element_by_xpath("//div[@id='leftcolumn']/a[{}]".format(a+1)).click()
		driver.implicitly_wait(10)
		

driver.close()

