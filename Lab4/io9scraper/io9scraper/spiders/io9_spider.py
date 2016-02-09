import scrapy

from io9scraper.items import Io9Post

class Io9Spider(scrapy.Spider):
	name = 'io9'
	allowed_domains = ['dmoz.org']
	start_urls = ['http://www.io9.gizmodo.com/']

	def parse(self, response):
		for headline in response.css('.headline::text').extract():
			item = Io9Post()
			item['headline'] = headline
			yield {'headline':headline}
