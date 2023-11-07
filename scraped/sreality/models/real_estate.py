from django.db import models


class RealEstate(models.Model):
    title = models.CharField(max_length=80)
    image_url = models.CharField(max_length=256)
