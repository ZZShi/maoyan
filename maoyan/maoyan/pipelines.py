# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


# class MaoyanPipeline(object):
#     def process_item(self, item, spider):
#         return item
#
#
# class MongoPipeline(object):
#     def __init__(self, mongo_uri, mongo_db):
#         self.mongo_uri = mongo_uri
#         self.mongo_db = mongo_db
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         cls(
#             mongo_uri=crawler.settings.get('MONGO_URI'),
#             mongo_db=crawler.settings.get('MONGO_DB')
#         )
#
#     def open_spider(self, spider):
#         self.client = pymongo.MongoClient(self.mongo_uri)
#         self.db = self.client[self.mongo_db]
#
#     def close_spider(self, spider):
#         self.client.close()
#
#     def process_item(self, item, spider):
#         col = item.get('movieName')
#         # self.my_db[col].update({'userId': item.get('userId')}, {'$set': dict(item)}, upsert=True)
#         my_col = self.db[col]
#         my_col.insert(dict(item))
#         return item

class MongoPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient()
        self.db = self.client['maoyan']

    def process_item(self, item, spider):
        col = item.get('movieName')
        self.db[col].update({'userId': item.get('userId')}, {'$set': dict(item)}, upsert=True)
        return item

