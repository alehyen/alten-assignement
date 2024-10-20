from django.db import models

class StockStatus(models.TextChoices):
    INSTOCK = 'INSTOCK'
    LOWSTOCK = 'LOWSTOCK'
    OUTOFSTOCK = 'OUTOFSTOCK'


class Product(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.TextField(max_length=100, null=True)
    category = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    internalReference = models.CharField(max_length=250, null=True)
    shellId = models.CharField(max_length=100, null=True)
    inventoryStatus = models.CharField(max_length=50, choices=StockStatus.choices, default=StockStatus.INSTOCK)
    rating = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

