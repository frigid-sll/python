from selenium import webdriver
import csv
class News:
    def GetTitle(self):
        self.listTitle = driver.find_elements_by_xpath("//div[@class='w1200']//dl/dt/a")
        for x in range(len(self.listTitle)):
            self.listTitle[x] = self.listTitle[x].text

    def GetTitleUrl(self):
        self.listTitleUrl = driver.find_elements_by_xpath("//div[@class='w1200']//dl/dt/a")
        for x in range(len(self.listTitleUrl)):
            self.listTitleUrl[x] = self.listTitleUrl[x].get_attribute('href')

    def GetImgSrc(self):
        self.listImgSrc = driver.find_elements_by_xpath("//div[@class='w1200']//dl//a/img")
        for x in range(len(self.listImgSrc)):
            self.listImgSrc[x] = self.listImgSrc[x].get_attribute('src')

    def GetAll(self):
        self.list=[]
        for x in range(len(self.listTitleUrl)):
            dict={}
            dict['Title']=self.listTitle[x]
            dict['TitleUrl']=self.listTitleUrl[x]
            dict['ImgSrc']=self.listImgSrc[x]
            self.list.append(dict)
        # print(self.list)

    def Write(self):
        fieldnames=['Title','TitleUrl','ImgSrc']
        with open('2.csv',mode='a',encoding='utf8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.list)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.cnbeta.com/')
    news=News()
    news.GetTitle()
    news.GetTitleUrl()
    news.GetImgSrc()
    news.GetAll()
    news.Write()









