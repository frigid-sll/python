# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient

class ItcomPipeline(object):

    def open_spider(self,spider):
        self.comment = MongoClient(host='127.0.0.1',port=27017)
        self.db = self.comment['posts']['news']

    def process_item(self, item, spider):
        self.db.insert_one(dict(item))
        return item

    def close_spider(self,spider):
        self.comment.close()
