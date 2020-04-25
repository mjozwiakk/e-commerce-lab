from django.urls import path
from .views import product_create_view, dynamic_lookup_view, product_list_view

app_name='products'

urlpatterns = [
    path('', product_list_view, name='product-list'),
    path('<int:id>/', dynamic_lookup_view, name='product-detail'),
    path('create/', product_create_view, name='product-create'),
]
