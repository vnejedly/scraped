import scrapy
from typing import Any, Iterable
from scrapy.http import Request, Response
from .real_estate_item import RealEstateItem
from scrapy_splash import SplashRequest
from pprint import pprint


class SrealitySpider(scrapy.Spider):
    name = 'sreality_spider'
    start_urls = ['https://www.sreality.cz/hledani/prodej/byty']

    def start_requests(self) -> Iterable[Request]:
        for url in self.start_urls:
            yield SplashRequest(url, callback=self.parse, args={'wait': 2})

    def parse(self, response: Response, **kwargs: Any) -> Any:
        print(response.body)
        xp = response.xpath('/html/body/div[2]/div[1]/div[2]/div[3]/div[3]')
        # pprint(xp)

        item = RealEstateItem()
        item["title"] = 'title'  # TODO: parse it out of the response
        item["image_url"] = 'image'  # TODO: parse it out of the response

        yield item

