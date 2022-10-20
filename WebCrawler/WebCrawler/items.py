import scrapy


class WebcrawlerItem(scrapy.Item):
  pass

class ReviewLoLItem(scrapy.Item):
  name = scrapy.Field()
  rank = scrapy.Field()
  role = scrapy.Field()
  tier = scrapy.Field()
  win_rate = scrapy.Field()
  pick_rate = scrapy.Field()
  ban_rate = scrapy.Field()
  counter_picks = scrapy.Field()
  matches = scrapy.Field()
