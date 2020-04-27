from django.db import models
from django.urls import reverse
# Create your models here.

CATEGORY = (
    ('o', 'Inne'),
    ('m', 'Męskie'),
    ('w', 'Damskie'),
    ('k', 'Dziecięce'),
)


class Product(models.Model):
    title = models.CharField(max_length=100, default='Product name')
    category = models.CharField(choices=CATEGORY, max_length=1, default='o')
    price = models.DecimalField(decimal_places = 2, max_digits = 10000 , default=0)
    short_description = models.TextField(default='Product short description (shown on item-lists)')
    description = models.TextField(default='Product description')
    image = models.ImageField()
    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"id": self.id})
    