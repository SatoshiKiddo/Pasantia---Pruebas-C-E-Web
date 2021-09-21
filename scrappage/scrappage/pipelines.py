# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os


class ScrappagePipeline:
    def process_item(self, item, spider):
        try:
            with open('../routes/exception_routes.conf') as f:
                for ruta in f.readlines():
                    if item['url_route'].find(ruta) != -1:
                        f.close()
                        item['url_route']="/"
                    f.close()
        except FileNotFoundError as e:
            print("Error de archivo - " + e.strerror)
        except IOError as e:
            print("Error de existencia de archivo - " + e.strerror)
        finally:
            return item
