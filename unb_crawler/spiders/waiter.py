# -*- coding: utf-8 -*-
import scrapy
from unb_crawler.items import UnbCrawlerItem

#helper functions that either return a string or None
def getCampus(element):
    testCampus = element.css("strong span::text").extract_first()
    if not testCampus:
        testCampus = element.css("strong span a::text").extract_first()
    return testCampus

def getDate(element):
    testDate = element.css("a::text").extract_first()
    return testDate

def getPdfPath(element):
    path = element.css("a::attr(href)").extract_first()
    return path

#spider class
class WaiterSpider(scrapy.Spider):
    name = 'waiter'
    allowed_domains = ['ru.unb.br']
    start_urls = ['http://ru.unb.br/index.php/cardapio-refeitorio']

    def parse(self, response):
        campus = None
        date = None
        for element in response.css(".item-page p"):
            testCampus = getCampus(element)
            if testCampus:
                campus = testCampus
            date = getDate(element)
            pdfPath = getPdfPath(element)
            if campus and date and pdfPath:
                pdf = response.urljoin(pdfPath)  
                item = UnbCrawlerItem(campus=campus, date=date, pdf_url=[pdf])
                yield item
            
             
