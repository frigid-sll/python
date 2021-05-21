# -*- coding: utf-8 -*-
import scrapy
from ScrapyZXX.items import ScrapyzxxItem

class ZxxSpider(scrapy.Spider):
    name = 'zxx'
    allowed_domains = ['www.zhangxinxu.com/']
    start_urls = ['https://www.zhangxinxu.com/wordpress/']

    def parse(self, response):
        listHref = response.xpath('//*/div/p[1]/img/@src').extract()
        for i in range(len(listHref)):
            item = ScrapyzxxItem()
            # image_urls:必须用次名称（注意：网址必须是http/https开头，还必须是是列表形式）
            item['image_urls'] =  ['http:'+listHref[i]]
            yield item
