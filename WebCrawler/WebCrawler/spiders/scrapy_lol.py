import scrapy
from scrapy import Request
from WebCrawler.items import ReviewLoLItem


class ScrapyLolSpider(scrapy.Spider):
  name = 'scrapy_lol'
  allowed_domains = ['u.gg']
  start_urls = ['http://u.gg/']

  def parse_lol(self, response):
    champions_list = response.css('div.rowgroup div.rt-tr-group')

    # Boucle qui parcours l'ensemble des éléments de la liste des champions
    for champion in champions_list:
      item = ReviewLoLItem()

      # Nom du film
      try:
        item['title'] = champion.css('h2 a::text')[0].extract()
      except:
        item['title'] = 'None'

      yield item
  
  def start_requests(self):
    for url in self.start_url:
      yield Request(url = url, callback = self.parse_boursorama)
