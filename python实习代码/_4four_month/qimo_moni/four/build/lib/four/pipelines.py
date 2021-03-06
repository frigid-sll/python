# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy,os
from scrapy.pipelines.images import ImagesPipeline
from pymongo import MongoClient
import json

class FourPipeline(object):
    def open_spider(self,spider):
        self.client=MongoClient(host='localhost',port=27017)
        self.collection=self.client['qimo']['four']
    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item
    def close_spider(self,spider):
        self.client.close()

class CrawlImg(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(url=item['img'])
    def item_completed(self, results, item, info):
        img_path=''.join([x['path'] for ok,x in results if ok])
        os.rename('./img/'+img_path,'./img/'+item['title']+'.jpg')
        return item

class Write(object):
    def open_spider(self,spider):
        self.file=open(file='1.json',mode='a',encoding='utf8')
    def process_item(self, item, spider):
        json.dump(dict(item),self.file,ensure_ascii=False,indent=2)
        return item
    def close_spider(self,spider):
        self.file.close()
