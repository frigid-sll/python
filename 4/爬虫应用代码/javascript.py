from selenium import webdriver
import re
import os

# os.mkdir('D:/javascript')

driver=webdriver.Chrome()

# url='https://www.w3school.com.cn/js/js_intro.asp'

# driver.get(url=url)

# ul_len=len(driver.find_element_by_xpath('//*[@id="course"]').find_elements_by_xpath('ul'))

# for ul in range(1,ul_len+1):

# 	li_len=len(driver.find_element_by_xpath('//*[@id="course"]/ul[{}]'.format(ul)).find_elements_by_xpath('li'))

# 	name=re.sub('\s','-','D:/javascript/'+'%d'%(ul)+driver.find_element_by_xpath('//*[@id="course"]/h2[{}]'.format(ul)).text)

# 	os.mkdir(name)

# 	for li in range(1,li_len):
# 		html = driver.execute_script("return document.documentElement.outerHTML")
# 		content='\n'.join(re.findall('<div id="maincontent">(.*)<!-- maincontent end -->',html,re.S))
# 		title=name+'/'+'%d'%(li)+re.sub('\s','-',driver.find_element_by_xpath('//*[@id="course"]/ul[{}]/li[{}]/a'.format(ul,li)).get_attribute('title'))+'.md'

# 		try:
# 			with open(title,'w',encoding='utf8') as f:
# 				f.write(content)
# 		except:
# 			pass
# 		else:
# 			driver.find_element_by_xpath("//div[@id='course']/ul[{}]/li[{}]".format(ul,li)).click()
# 			driver.implicitly_wait(10)

# driver.close()



url='https://blog.csdn.net/colin_yu/article/details/77892874'
driver.get(url=url)

html = driver.execute_script("return document.documentElement.outerHTML")
content='\n'.join(re.findall('<div class="table-box">(.*</table>)</div>',html,re.S))

with open('C:/Users/EDZ/Desktop/linux.md','w',encoding='utf-8') as f:
    f.write(content)

f.close()
driver.close()