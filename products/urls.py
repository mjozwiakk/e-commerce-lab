from django.urls import path
from .views import product_create_view, dynamic_lookup_view, product_list_view, product_list_view_filter

app_name='products'

urlpatterns = [
    path('', product_list_view, name='product-list'),
    path('category/<str:category>/', product_list_view_filter, name='product-list-filter'),
    path('<int:id>/', dynamic_lookup_view, name='product-detail'),
    path('create/', product_create_view, name='product-create'),
]
