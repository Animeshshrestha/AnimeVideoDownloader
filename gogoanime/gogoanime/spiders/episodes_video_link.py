import scrapy
from .items import GogoanimeItem

class TitleandEpisodesSpider(scrapy.Spider):

	name = 'gogoanime'
	name_of_anime = input("Please Enter the Name of Anime you want to download: ")
	rs = name_of_anime.replace(" ", "-")
	start_urls = ['https://www.gogoanime1.com/watch/'+rs]

	def parse(self, response):

		for href in response.css('.check-list li a::attr(href)'):
			yield response.follow(href, self.parse_video_link)


	def parse_video_link(self,response):

		data = GogoanimeItem()
		data['name'] = self.name_of_anime+' '+'Episode'+' '
		data['title'] = response.css('.vmn-title h1::text').get()
		data['download_link'] = response.css('.vmn-buttons a::attr(href)')[-1].get()
		yield data	

