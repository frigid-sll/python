# a=[x for x in range(16)]
# b=[tuple([x for x in a[index:index+3]]) for index in [y for y in range(len(a)) if y%3==0]]
# print(b)

	


# total=[]
# for x in range(k,0,-1):    
# 	_list=['1' for x in range(x)]    
# 	_list[-1]=str(k-x+1)
# 	total.append('{}='.format(k)+'+'.join(_list))
# print('\n'.join(total))



# k=5
# total='\n'.join([value.replace(value[-1],'{}'.format(index+1),1) for index,value in enumerate(['\t'.join(['{}='.format(k)+'+'.join(['1' for y in range(x)])]) for x in range(k,0,-1)])])
# print(total)




# from selenium import webdriver

# driver=webdriver.Chrome()

# driver.get(url='https://www.cnblogs.com/zhangruiqi/p/9062005.html')
# content=driver.find_element_by_xpath("//div[@id='cnblogs_post_body']").text

# with open('C:/Users/EDZ/Desktop/vue.md','w') as f:
# 	f.write(content)

# driver.close()

# b='asdasd'
# a=f'{b}'+'111'
# print(a)


# num,result=[x for x in range(1,21)],[]
# for x in num:
# 	for y in range(2,11):
# 		if x%y==0 and x!=y:
# 			result.append(x)
# 			break
# print([x for x in num if x not in result])


# i=0
# a=[1,2,3,4,5]
# k=i
# j=i+1
# n=len(a)-1
# while True:
# 	if j<=n:
# 		if a[k]<a[j]:
# 			k=j
# 			j+=1
# 		else:
# 			j+=1
# 	else:
# 		break
# print(f'最大值为:{a[k]}')

# a={x:y for x,y in enumerate([1,2,3,4])}
# print(a)



# import re
# from selenium import webdriver

# driver=webdriver.Chrome()

# driver.get(url='https://xysd.gitbooks.io/test-knowledge/gong-zuo-xi-guan.html')
# driver.implicitly_wait(10)

# li=driver.find_elements_by_xpath("//ul//li")
# for x in li[1:3]:
#     try:
#         a=x.find_element_by_xpath('a')
#         a.click()
#         driver.implicitly_wait(10)
#         html = driver.execute_script("return document.documentElement.outerHTML")
#         content=re.findall('<div class="search-noresults">.*<div class="search-results">',html,re.S)[0]
#         name=f'C:/Users/EDZ/Desktop/test/{a.text}'+'.md'
#         if content!=' ':
#             with open(name,'w',encoding='utf8') as f:
#                 f.write(content)
#     except:
#         print('1111111111111111111')


# driver.close()












# from selenium import webdriver
# import requests
# import time
# import re
# from PIL import Image

# driver=webdriver.Chrome()

# url='https://hfdingshua.chinapnr.com/supm/login'
# driver.get(url=url)
# driver.find_element_by_xpath('//*[@id="userName"]').send_keys('gaoxinyu')
# driver.find_element_by_xpath('//*[@id="password"]').send_keys('gxy123456')
# driver.implicitly_wait(10)

# #截下全屏图保存为quanpingtu.png
# driver.get_screenshot_as_file('quanping.png')
# #定位验证码的位置
# element=driver.find_element_by_xpath('//*[@id="img-code"]')
# left = element.location['x']+50
# top = element.location['y']+50
# right = left + element.size['width']
# bottom = top + element.size['height']
# print(type(left))
# #打开全屏图
# im = Image.open('quanping.png') 
# #截取验证码
# im = im.crop((left, top, right, bottom))
# #保存验证码图片 名字为screenshot.png
# im.save('screenshot.png')

# driver2=webdriver.Chrome()
# url2='http://tool.chinaz.com/tools/imgtobase/'
# driver2.get(url=url2)
# driver2.find_element_by_xpath('//*[@id="imgtobase"]').click()
# time.sleep(10)
# content=driver2.find_element_by_xpath('//*[@id="basestr"]').text
# driver2.close()


# url3='http://apigateway.jianjiaoshuju.com/api/v_1/yzm.html'
# headers={
#     'appCode':'33949A052FF5F827BB1FD015CC8A0D44',
#     'appKey':'AKID7732db5880bf75bb5c6bf1c9b4ceed07',
#     'appSecret':'767d16c02e00b131dd0fe2d474691b9b'
# }
# data={
#     'v_pic':content,
#     'v_type':'ne5'
# }

# response=requests.post(url=url3,headers=headers,data=data).text

# code=response.split(',')[1][10:-1]
# print(code)

# driver.find_element_by_xpath('//*[@id="captcha"]').send_keys(code)
# driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/a[1]/span').click()




# from selenium import webdriver
# driver=webdriver.Chrome()
# url='https://weixin.sogou.com/'
# driver.get(url=url)
# driver.find_element_by_xpath('//*[@id="more_anchor"]').click()
# driver.find_element_by_xpath('//*[@id="pc_7"]').click()
# title=driver.find_elements_by_xpath('//*[@id="pc_7_0"]/li//h3/a')
# title=[x.get_attribute('href') for x in title]
# print('\n'.join(title))



# from selenium import webdriver
# import os
# import re

# path=os.getcwd().replace('\\','/')+'/element-ui'
# try:
#     os.mkdir(path)
# except:
#     pass

# driver=webdriver.Chrome()
# driver.get(url='https://element.eleme.cn/#/zh-CN/component/installation')
# driver.implicitly_wait(10)

# li_list=driver.find_elements_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div/div/div[1]/div[1]/div/div/ul/li[6]/div[1]/ul/li')

# # li_list=[driver.find_elements_by_xpath(f'//*[@id="app"]/div[2]/div/div[1]/div/div/div[1]/div[1]/div/div/ul/li[6]/div[{x}]/ul/li') for x in range(1,7)]

# # for x in range(len(li_list)):
# #     for y in li_list[x]:
# #         y.click()
# #         driver.implicitly_wait(10)
# #         title=y.find_element_by_xpath('/a').text

# for y in li_list:
#     y.click()
#     driver.implicitly_wait(10)
#     title=path+'/'+y.find_element_by_xpath('a').text+'.md'
#     content=driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div/div/div[2]/section').get_attribute('innerHTML')
#     with open(title,'w',encoding='utf-8') as f:
#         f.write(content)
#     f.close()