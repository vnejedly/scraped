from django.core.management.base import BaseCommand
import requests
from typing import Dict
from ...models.real_estate import RealEstate


class Command(BaseCommand):

    def handle(self, *args, **options):
        for page in range(1, 11):
            print(f'Saving page number {page}')

            for estate in self.get_page(50, page)['_embedded']['estates']:
                model = RealEstate(
                    title=estate['name'],
                    image_url=estate['_links']['images'][0]['href'],
                )

                model.save()

    @staticmethod
    def get_page(size: int, number: int) -> Dict:
        response = requests.get(
            f'https://www.sreality.cz/api/cs/v2/estates'
            f'?category_main_cb=1&category_type_cb=1&tms=1699305570332'
            f'&per_page={size}&page={number}'
        )

        return response.json()
