# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UnbCrawlerItem(scrapy.Item):
    campus = scrapy.Field()
    date = scrapy.Field()
    pdf_url = scrapy.Field()
    pdf = scrapy.Field()