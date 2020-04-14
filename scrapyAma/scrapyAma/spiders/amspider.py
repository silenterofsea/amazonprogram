# -*- coding: utf-8 -*-
import scrapy


class AmspiderSpider(scrapy.Spider):
    name = 'amspider'
    allowed_domains = ['amazone.com']
    start_urls = ['http://amazone.com/']

    def parse(self, response):
        pass
