from django.db import models


# Create your models here.
class Vegetables(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    image = models.CharField(max_length=200, )
    price = models.CharField(max_length=200, )
    discount = models.CharField(max_length=200, blank=True)
    price_sale = models.CharField(max_length=500, blank=True)
    type = models.CharField(max_length=50)
    enable = models.CharField(max_length=50, blank=True)