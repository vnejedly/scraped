from scrapy_djangoitem import DjangoItem
from ...models.real_estate import RealEstate


class RealEstateItem(DjangoItem):
    django_model = RealEstate
