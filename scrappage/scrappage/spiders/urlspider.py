import scrapy
import os
from ..items import UrlsItem

rutas_recorridas = []

class UrlSpider(scrapy.Spider):
    name= "scrapper"
    start_urls = [
        os.getenv("HOST")
    ]

    def parse(self, response):
        global rutas_recorridas
        for href in response.css('a::attr(href)').getall():
            item = UrlsItem()
            if (self.start_urls[0] in href):
                ruta = href.replace(self.start_urls[0],'')
                if (ruta not in rutas_recorridas):
                    rutas_recorridas.append(ruta)
                    yield scrapy.Request(url=href, callback=self.parse)
                    item['url_route']=ruta
                    yield item