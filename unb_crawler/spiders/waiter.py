# -*- coding: utf-8 -*-
import scrapy


class WaiterSpider(scrapy.Spider):
    name = 'waiter'
    allowed_domains = ['https://ru.unb.br/index.php/cardapio-refeitorio']
    start_urls = ['http://https://ru.unb.br/index.php/cardapio-refeitorio/']

    def parse(self, response):
        pass
