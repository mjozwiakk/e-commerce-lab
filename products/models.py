from django.db import models
from django.urls import reverse
# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100, default='Product name')
    price = models.DecimalField(decimal_places = 2, max_digits = 10000 , default=0)
    description = models.TextField(default='Product description')
    image = models.ImageField()

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"id": self.id})
    