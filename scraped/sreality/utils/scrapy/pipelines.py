import scrapy
from scrapy_djangoitem import DjangoItem


class RealEstatePipeline(object):

    def process_item(self, item: DjangoItem, spider: scrapy.Spider):
        item.save()
        return item
