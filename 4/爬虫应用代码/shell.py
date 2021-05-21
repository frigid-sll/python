from selenium import webdriver
import re


driver=webdriver.Chrome()

url='https://www.runoob.com/linux/linux-shell.html'

driver.get(url=url)

for num in range(14,16):
	a=driver.find_element_by_xpath('//*[@id="leftcolumn"]/a[{}]'.format(num)).click()
	driver.implicitly_wait(10)
	html = driver.execute_script("return document.documentElement.outerHTML")
	content='\n'.join(re.findall('<div class="article-body">(.*)<!-- 右边栏 -->',html,re.S))
	with open('{}.md'.format(num),'w',encoding='utf8') as f:
		f.write(content)

driver.close()

