# -*- coding: utf-8 -*-
import scrapy
from ..items import FourItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['yunmss.cn']
    start_urls = ['http://www.yunmss.cn/']

    def parse(self, response):
        all=response.xpath("//div[@class='posts']/div[@class='loop']")
        for x in all:
            item=FourItem()
            item['title']=x.xpath("./div[@class='content_body']/h2/a/text()").extract()[0]
            item['url']=x.xpath("./div[@class='content_body']/h2/a/@href").extract()[0]
            item['img']=x.xpath("./div[@class='content-two']/a/img/@src").extract()[0]
            item['date']=x.xpath("./div[@class='content_infor']/span[3]/text()").extract()[0]
            yield scrapy.Request(url=item['url'],callback=self.CrawlContent,method='GET',meta={'item':item},dont_filter=True)

    def CrawlContent(self,response):
        item=response.meta['item']
        item['content']=''.join(response.xpath("//div[@class='post']/p/text()").extract())
        if item['content']=='':
            item['content'] = ''.join(response.xpath("//div[@class='post']/p/span/text()").extract())
        yield item
