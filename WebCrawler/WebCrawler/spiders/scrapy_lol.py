import scrapy
from scrapy import Request
from WebCrawler.items import ReviewLoLItem


class ScrapyLolSpider(scrapy.Spider):
  name = 'scrapy_lol'
  allowed_domains = ['u.gg']
  start_urls = ['http://u.gg/']

  def parse_lol(self, response):
    champions_list = response.css('table tr')

    # Boucle qui parcours l'ensemble des éléments de la liste des champions
    for champion in champions_list:
      item = ReviewLoLItem()

      # Nom du champion
      try:
        item['name'] = champion.css('td span.name::text')[0].extract().strip()
      except:
        item['name'] = 'None'

      # Rôle du champion
      try:
        item['role'] = champion.css('td div.txt i::text')[0].extract().strip()
      except:
        item['role'] = 'None'

      # Classement du champion
      try:
        item['rank'] = champion.css('td.text-right::text')[0].extract().strip().replace('.', '')
      except:
        item['rank'] = 'None'
      
      # Popularité du champion
      try:
        item['fame'] = champion.css('td progressbar')[0].attrib['data-value']
      except:
        item['fame'] = 'None'

      # Taux de victoire du champion
      try:
        item['victory'] = champion.css('td progressbar')[1].attrib['data-value']
      except:
        item['victory'] = 'None'

      # Taux de ban du champion
      try:
        item['ban_rate'] = champion.css('td progressbar')[2].attrib['data-value']
      except:
        item['ban_rate'] = 'None'

      # KDA du champion à compléter
      try:
        item['kda'] = champion.css('h2 a::text')[0].extract()
      except:
        item['kda'] = 'None'

      # Pentas par match du champion à compléter
      try:
        item['pentas_match'] = champion.css('h2 a::text')[0].extract()
      except:
        item['pentas_match'] = 'None'

      yield item
  
  def start_requests(self):
    for url in self.start_url:
      yield Request(url = url, callback = self.parse_lol)

# name :
# response.css('table tr td span.name::text')[0].extract().strip()

# role : 
# response.css('table tr td div.txt i::text')[0].extract().strip()

# rank :
# data = response.css('table tr td progressbar')[0].attrib['data-value']
# data = data * 100
