from django.shortcuts import render
from products.models import Product
# Create your views here.

def home_view(request, *args, **kwargs):
    queryset = Product.objects.all()[:8]
    context = {
        "new_products": queryset
    }
    return render(request, 'home.html', context)
    
def contact_view(request, *args, **kwargs):
    my_context = {
        "title": "contact page text",
        "this_is_true": True,
        "my_number": 123,
        "my_list": [123, 312, 1221, 123, "abc"],
        "my_html": "<h1>Hello World!</h1>",
    }
    return render(request, 'contact.html', my_context)
    