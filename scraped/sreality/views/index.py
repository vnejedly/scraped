from typing import Iterator, Tuple
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from ..models.real_estate import RealEstate


class Index(View):

    PAGE_SIZE = 10

    def get(self, request: WSGIRequest) -> HttpResponse:
        offset = int(request.GET.get('offset', 0))
        real_estates = RealEstate.objects.all()[offset:offset+self.PAGE_SIZE]

        return render(request, "index.html", {
            'real_estates': real_estates,
            'pager': self._get_pager(self.PAGE_SIZE),
        })

    @staticmethod
    def _get_pager(page_size: int) -> Iterator[Tuple[int, int]]:
        page = 0
        for offset in range(0, RealEstate.objects.count(), page_size):
            page += 1
            yield page, offset
