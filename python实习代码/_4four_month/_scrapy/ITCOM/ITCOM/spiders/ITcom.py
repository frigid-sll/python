# -*- coding: utf-8 -*-
import scrapy
from ..items import ItcomItem


class ItcomSpider(scrapy.Spider):
    name = 'ITcom'
    allowed_domains = ['citreport.com/news/it/']
    start_urls = ['http://www.citreport.com/news/it/']

    def parse(self, response):
        #标题
        title = response.xpath('//*[@id="ct"]/div[1]/div[2]/div[2]/div/div/div/h2/a/text()').extract()
        # print(title)
        #文章链接
        url = response.xpath('//*[@id="ct"]/div[1]/div[2]/div[2]/div/div/div/h2/a/@href').extract()
        # print(url)
        #图片链接
        images = response.xpath('//*[@id="ct"]/div[1]/div[2]/div[2]/div/div/div[1]/a/img/@src').extract()
        for index,values in enumerate(title):
            item = ItcomItem()
            item['title'] = title[index]   #标题
            item['url'] = url[index]   #文章详情页地址
            item['image_urls'] = [images[index]]  #图片链接
            # meta是向下个方法里传递参数 以字典的形式  key:value 可以传递多个参数  dont_filter是url去重
            yield scrapy.Request(url=url[index],callback=self.content_parse,method='GET',meta={'item':item},dont_filter=True)
    #获取详情页
    def content_parse(self,response):
        item = response.meta['item']
        item1 = response.xpath('//p/text()').extract()
        item['content2'] = ''.join(item1)
        print(item['content2'])
        yield item

