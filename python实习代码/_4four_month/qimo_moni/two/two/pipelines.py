# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from pymongo import MongoClient
import scrapy,os
from scrapy.pipelines.images import ImagesPipeline

class TwoPipeline(object):
    def open_spider(self,spider):
        self.client=MongoClient(host='localhost',port=27017)
        self.collection=self.client['qimo']['news2']
    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item
    def close_spider(self,spider):
        self.client.close()

class newsPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        img_link=item['image']
        yield scrapy.Request(img_link)
    def item_completed(self, results, item, info):
        image_path=[x['path'] for ok,x in results if ok][0]
        os.rename('./img/'+image_path,'./img/'+item['title']+'.jpg')
        return item
    # def file_path(self, request, response=None, info=None):
    #     img=request.url.split('/')[-1]
    #     return 'full/%s'%(img)   #以图片的网址后缀为图片名