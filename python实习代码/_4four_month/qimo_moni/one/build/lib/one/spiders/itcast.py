# -*- coding: utf-8 -*-
import scrapy,re
from ..items import OneItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['zhangxinxu.com']
    start_urls = ['https://www.zhangxinxu.com/wordpress/']

    def parse(self, response):
        listTitle=response.xpath("//div[@id='content']/div/h2/a/text()").extract()
        listDate=response.xpath("//div[@id='content']/div/small/span[1]/text()").extract()
        listCount=response.xpath("//div[@id='content']/div/small/text()[2]").extract()
        for x in range(len(listCount)):
            listCount[x]=re.findall('\d+',listCount[x])[1]
        listTag=response.xpath("//div[@id='content']/div/p")
        for x in range(len(listTag)):
            listTag[x]=listTag[x].xpath("./a[position()<last()-1]/text()").extract()
        listContentUrl=response.xpath("//div[@id='content']/div/h2/a/@href").extract()
        listContent=response.xpath("//div[@id='content']/div/div++++++ [@role='summary']")
        for x in range(len(listContent)):
            listContent[x]=listContent[x].xpath("./p/text()").extract()
        list=[]
        for x in range(len(listContentUrl)):
            item=OneItem()
            item['title']=listTitle[x]
            item['date']=listDate[x]
            item['count']=int(listCount[x])
            item['tag']=listTag[x]
            item['url']=listContentUrl[x]
            item['content']=listContent[x]
            list.append(dict(item))
            print(list)
            yield item
