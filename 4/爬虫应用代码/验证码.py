from selenium import webdriver
import  requests
import  time
import  re
from PIL import Image
import json

driver=webdriver.Chrome()

#输入账号密码
url='https://hfdingshua.chinapnr.com/supm/login'
driver.get(url=url)
driver.find_element_by_xpath('//*[@id="userName"]').send_keys('gaoxinyu')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('gxy123456')
driver.implicitly_wait(10)

#获取界面验证码的图片
driver.get_screenshot_as_file('screenshot.png')
element=driver.find_element_by_xpath('//*[@id="img-code"]')
left=element.location['x']
top=element.location['y']
right=element.location['x']+element.size['width']
bottom=element.location['y']+element.size['height']

im=Image.open('screenshot.png')
im=im.crop((left,top,right,bottom))
#将得到的图片保存在本地桌面上
im.save('C:/Users/Administrator.DESKTOP-6KVNT6V/Desktop/screenshot.png')

#得到验证码图片的bs64信息流
driver2=webdriver.Chrome()
url2='http://tool.chinaz.com/tools/imgtobase/'
driver2.get(url=url2)
driver2.find_element_by_xpath('//*[@id="imgtobase"]').click()
time.sleep(10)
content=driver2.find_element_by_xpath('//*[@id="basestr"]').text
driver2.close()


#将验证码图片给平台识别
url3='http://apigateway.jianjiaoshuju.com/api/v_1/yzm.html'
headers={
'appCode':'33949A052FF5F827BB1FD015CC8A0D44',
'appKey':'AKID7732db5880bf75bb5c6bf1c9b4ceed07',
'appSecret':'767d16c02e00b131dd0fe2d474691b9b'
}
data={
'v_pic':content,
'v_type':'ne5'
}

response=requests.post(url=url3,headers=headers,data=data).text

code=response.split(',')[1][10:-1]
#print(code)      识别出的验证码

#输入验证码登陆
driver.find_element_by_xpath('//*[@id="captcha"]').send_keys(code)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/a[1]/span').click()
driver.implicitly_wait(10)

#进入交易明细查询页面
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[3]/div[1]/div/ul/li[3]/dl/dt/a').click()
time.sleep(0.5)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[3]/div[1]/div/ul/li[3]/dl/dd/a').click()
time.sleep(0.5)
#修改日期
driver.find_element_by_xpath('//*[@id="startDate"]').click()
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div[2]/table/tbody/tr[4]/td[6]/a').click()
time.sleep(0.5)
#修改交易类型:刷卡支付收款
driver.find_element_by_xpath('//*[@id="transType"]').click()
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="transType"]/option[2]').click()
#查询
driver.find_element_by_xpath('//*[@id="queryResult"]/span').click()
time.sleep(0.5)
#爬取内容

content=driver.find_element_by_xpath('//*[@id="controllerDiv"]/div/div/table').get_attribute("outerHTML")
with open('C:/Users/Administrator.DESKTOP-6KVNT6V/Desktop/jiao_shua.md','w',encoding='utf-8') as f:
    f.write(content)
f.close()
