from django.core.management.base import BaseCommand
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from ...utils.scrapy.sreality_spider import SrealitySpider
from django.conf import settings


class Command(BaseCommand):

    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())

        process.settings.set('ITEM_PIPELINES', settings.ITEM_PIPELINES)
        process.settings.set('SPLASH_URL', settings.SPLASH_URL)
        process.settings.set('DOWNLOADER_MIDDLEWARES', settings.DOWNLOADER_MIDDLEWARES)
        process.settings.set('SPIDER_MIDDLEWARES', settings.SPIDER_MIDDLEWARES)
        process.settings.set('DUPEFILTER_CLASS', settings.DUPEFILTER_CLASS)
        process.settings.set('HTTPCACHE_STORAGE', settings.HTTPCACHE_STORAGE)

        process.crawl(SrealitySpider)
        process.start()
