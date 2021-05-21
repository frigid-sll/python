# -*- coding: utf-8 -*-
import scrapy
from ..items import TwoItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    url='https://www.xminseo.com/page/'
    num=1
    allowed_domains = ['xminseo.com']
    start_urls = [url+str(num)]

    def parse(self, response):
        listTitle =response.xpath("//div[@class='content']//article[@class='excerpt']/header/h2/a/text()").extract()
        listDate=response.xpath("//div[@class='content']//article[@class='excerpt']/p")
        listCount=response.xpath("//div[@class='content']//article[@class='excerpt']/p")
        for x in range(len(listDate)):
            listDate[x]=listDate[x].xpath("./span[1]/text()").extract()[0]
            listCount[x]=''.join(listCount[x].xpath("./span[2]/text()").extract())
        listImgUrl=response.xpath("//div[@class='content']//article[@class='excerpt']/div[@class='focus']/a/img/@src").extract()
        listCountUrl= response.xpath("//div[@class='content']//article[@class='excerpt']/header/h2/a/@href").extract()
        listLikeCount=response.xpath("//div[@class='content']//article[@class='excerpt']/p[@class='auth-span']/span//span[@class='count']/text()").extract()
        listContent=response.xpath("//div[@class='content']//article[@class='excerpt']/span[@class='note']/text()").extract()
        list=[]
        for x in range(len(listCount)):
            item=TwoItem()
            item['title']=listTitle[x]
            item['date']=listDate[x]
            item['count']=listCount[x]
            item['like']=listLikeCount[x]
            item['url']=listCountUrl[x]
            item['image']=listImgUrl[x]
            item['content']=listContent[x]
            list.append(dict(item))
            yield item
        # if self.num!=3:
        #     self.num += 1
        #     yield scrapy.Request(url=self.url+str(self.num),callback=self.parse)
        # print(list)
