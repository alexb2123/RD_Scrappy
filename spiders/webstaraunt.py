# -*- coding: utf-8 -*-
import scrapy


class ItemSpider(scrapy.Spider):
    name = 'Quotes'
#    allowed_domains = ['https://www.webstaurantstore.com']

    def start_requests(self):
        start_urls = ['https://www.webstaurantstore.com/choice-23-x-13-led-oval-open-sign-with-two-display-modes/466OPECONOVL.html'
                      'https://www.webstaurantstore.com/choice-23-x-13-led-oval-pizza-sign-with-two-display-modes/466LEDPIZOVL.html'
                      'https://www.webstaurantstore.com/choice-23-x-13-led-oval-coffee-sign-with-2-display-modes/466LEDCOFOVL.html']

        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

