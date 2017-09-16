# -*- coding: utf-8 -*-
import scrapy


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['www.jobbole.com']
    start_urls = ['http://www.jobbole.com/']

    def parse(self, response):
        pass
