from django.contrib import admin
from .models import Product, Order, OrderProduct
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'ordered',
        ]

class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'short_description',
        'category',
        'price',
        ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct)
