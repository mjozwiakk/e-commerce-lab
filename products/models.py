from django.db import models
from django.urls import reverse
# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100, default='Product name')
    description = models.TextField(default='Product description')
    price = models.DecimalField(decimal_places = 2, max_digits = 10000 , default=0)
    
    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"id": self.id})
    