# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import pymongo
import scrapy
from scrapy.conf import settings
from scrapy import log
from scrapy.pipelines.files import FilesPipeline
from scrapy.exceptions import DropItem


class MongoDBPipeline(object):

    def __init__(self):
        host = settings['MONGODB_SERVER']
        port = settings['MONGODB_PORT']
        connection = pymongo.MongoClient(host,port)
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {}!".format(data))
        if valid:
            self.collection.update({"url":item["url"]},dict(item),True,True)
            log.msg("Question added to MongoDB database!",
                    level=log.DEBUG, spider=spider)
        return item


class JavbusPipeline(object):
    def process_item(self, item, spider):
        return item

class KuaiyaojingPipeline(object):

    def __init__(self):
        host = settings['MONGODB_SERVER']
        port = settings['MONGODB_PORT']
        connection = pymongo.MongoClient(host,port)
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION2']]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {}!".format(data))
        if valid:
            self.collection.update({"id":item["id"]},dict(item),True,True)
            log.msg("Question added to MongoDB database!",
                    level=log.DEBUG, spider=spider)
        return item


class VideoPipeline(FilesPipeline):

    def file_path(self, request, response=None, info=None):
        original_path = super(VideoPipeline, self).file_path(request, response=None, info=None)
        sha1_and_extension = original_path.split('/')[1]  # delete 'full/' from the path
        return request.meta.get('title', '') + "_" + sha1_and_extension
    def get_media_requests(self, item, info):
        if not os.path.exists("D:\Video"):
            os.mkdir("D:\Video")

        yield scrapy.Request(item['video'],meta={"title":item["title"]})
        # else:
        #     print("Floder existed Now！")

    def item_completed(self, results, item, info):
        file_paths = [x['path'] for ok, x in results if ok]
        if not file_paths:
            raise DropItem("Item contains no video")
        item['file_paths'] = file_paths
        return item
