from django.db.models.signals import post_save
from django.db import models
from django.urls import reverse
from django.conf import settings
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
    short_description = models.TextField(default='Product short description (means product code)')
    description = models.TextField(default='Product description')
    image = models.ImageField()
    slug = models.SlugField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"slug": self.slug})

    def get_add_to_cart_url(self):
        return reverse("products:add-to-cart", kwargs={"slug": self.slug})

    def get_remove_from_cart_url(self):
        return reverse("products:remove-from-cart", kwargs={"slug": self.slug})

    def get_remove_single_from_cart_url(self):
        return reverse("products:remove-single-from-cart", kwargs={"slug": self.slug})

class OrderProduct(models.Model): 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 1)

    def __str__(self):
        return f"Ilość: {self.quantity}, Produkt : {self.product.title}"

    def get_total_item_price(self):
        return self.quantity * self.product.price
    

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    products = models.ManyToManyField(OrderProduct)

    def __str__(self):
        return self.user.username

    def get_product_sum_price(self):
        total = 0
        for product in self.products.all():
            total += product.get_total_item_price()
        return total

    def get_total_price(self):
        total = 0
        for product in self.products.all():
            total += product.get_total_item_price()
        return total + 15
    