# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import json

class ValidateDatePipeline(object):
    def process_item(self, item, spider):
        date = item['date']
        if len(date) >= 23:
            return item
        else:
            raise DropItem("Missing date in %s" % item)

class AdjustCampusPipeline(object):
    def process_item(self, item, spider):
        item['campus'] = item['campus'].strip()
        return item     

class AdjustDatePipeline(object):
    def process_item(self, item, spider):
        item['date'] = item['date'].strip()
        item['date'] = item['date'].split(' \u00e0 ')
        return item

class JsonWriterPipeline(object):
    def open_spider(self, spider):
        self.list = []
        self.file = open('result.json', 'w')

    def close_spider(self, spider):
        self.file.write(json.dumps(self.list, indent=4, ensure_ascii=False))
        self.file.close()

    def process_item(self, item, spider):
        self.list.append(dict(item))
        return item