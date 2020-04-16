# -*- coding: utf-8 -*-
import scrapy


class AmspiderSpider(scrapy.Spider):
    name = 'amspider'
    allowed_domains = ['amazone.com']
    start_urls = ['http://amazone.com/']

    # def start_requests(self):
    #     pass

    def parse(self, response):
        print(dir(response.body))
        print(response.body.decode())
        pass
