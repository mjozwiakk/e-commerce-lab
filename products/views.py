from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm, RawProductForm

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
    context = {
        'object': obj,
    }
    return render(request, "products/product-detail.html", context)


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "products/product-list.html", context)