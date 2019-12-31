# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.files import FilesPipeline
from scrapy import Request
from scrapy.exceptions import DropItem
import json
import os

class ValidateDatePipeline(object):
    def process_item(self, item, spider):
        date = item['date']
        if len(date) >= 23:
            return item
        else:
            raise DropItem("Missing date in %s" % item)

class AdjustCampusPipeline(object):
    def process_item(self, item, spider):
        item['campus'] = item['campus'].replace(' ','')
        return item     

class AdjustDatePipeline(object):
    def process_item(self, item, spider):
        item['date'] = item['date'].strip()
        item['date'] = item['date'].replace('/','-')
        item['date'] = item['date'].split(' \u00e0 ')
        return item

class JsonWriterPipeline(object):
    def open_spider(self, spider):
        self.list = []
        if not os.path.exists('./outputs'):
            os.mkdir('./outputs')
        self.file = open('./outputs/scraped.json', 'w')

    def close_spider(self, spider):
        self.file.write(json.dumps(self.list, indent=4, ensure_ascii=False))
        self.file.close()

    def process_item(self, item, spider):
        self.list.append(dict(item))
        return item

class DownloaderPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        return [Request(x, meta={'filename': item.get('campus') + item.get('date')[0]}) for x in item.get(self.files_urls_field, [])]

    def file_path(self, request, response=None, info=None):
        media_ext = os.path.splitext(request.url)[1]
        
        return 'outputs/pdfs/%s%s' % (request.meta['filename'], media_ext)