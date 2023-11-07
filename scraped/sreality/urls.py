from django.urls import path
from .views.index import Index

urlpatterns = [
    path("index/", Index.as_view()),
]
