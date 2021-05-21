# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient

class OnePipeline(object):
    def open_spider(self,spider):
        self.client=MongoClient(host='localhost',port=27017)
        self.collection=self.client['qimo']['news']
    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item
    def close_spider(self,spider):
        ret1=self.collection.aggregate([{'$project':{'_id':0,'date':0,'count':0,'url':0,'content':0,'tag':0}},{'$sort':{'date':1}}])
        for x in ret1:
            print(x)
        ret2=self.collection.aggregate([{'$group':{'_id':'$date','count':{'$sum':'$count'}}}])
        for x in ret2:
            print(x)
        self.client.close()
