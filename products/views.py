from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm

# Create your views here.


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'my_form': form
    }
    return render(request, "products/product-create.html", context)


def dynamic_lookup_view(request, id):
    obj = get_object_or_404(Product, id=id)
    latest_products = Product.objects.filter(category=obj.category)[:3]
    context = {
        'object': obj,
        'latest_products': latest_products,
    }
    return render(request, "products/product-detail.html", context)


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "products/product-list.html", context)

def product_list_view_filter(request, category):
    queryset = Product.objects.filter(category=category)
    context = {
        "object_list": queryset
    }
    return render(request, "products/product-list.html", context)