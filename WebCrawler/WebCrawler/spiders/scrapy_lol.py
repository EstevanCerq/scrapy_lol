import scrapy


class ScrapyLolSpider(scrapy.Spider):
    name = 'scrapy_lol'
    allowed_domains = ['u.gg']
    start_urls = ['http://u.gg/']

    def parse(self, response):
        pass
