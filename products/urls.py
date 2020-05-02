from django.urls import path
from .views import (
    dynamic_lookup_view, 
    product_list_view, 
    product_list_view_filter, 
    add_to_cart, 
    remove_from_cart,
    remove_single_from_cart
)

app_name='products'

urlpatterns = [
    path('', product_list_view, name='product-list'),
    path('category/<str:category>/', product_list_view_filter, name='product-list-filter'),
    path('<slug:slug>/', dynamic_lookup_view, name='product-detail'),
    path('add-to-cart/<slug>', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>', remove_from_cart, name='remove-from-cart'),
    path('remove-single-from-cart/<slug>', remove_single_from_cart, name='remove-single-from-cart'),
]
