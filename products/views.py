from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, OrderProduct, Order
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

def dynamic_lookup_view(request, slug):
    obj = get_object_or_404(Product, slug=slug)
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

@login_required(login_url='/account/login/')
def add_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    order_product, created = OrderProduct.objects.get_or_create(product=product, user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.products.filter(product__slug=product.slug).exists():
            order_product.quantity += 1
            order_product.save()
            messages.info(request, "Zaktualizowano stan koszyka")
            return redirect("cart")
        else:
            order.products.add(order_product)
            messages.info(request, "Produkt dodany do koszyka")
            return redirect("cart")
    else:
        order = Order.objects.create(user=request.user)
        order.products.add(order_product)
        messages.info(request, "Produkt dodany do koszyka")
        return redirect("cart")
    
      
@login_required(login_url='/account/login/')
def remove_from_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.products.filter(product__slug=product.slug).exists():
            order_product = OrderProduct.objects.filter(product=product, user=request.user, ordered=False)[0]
            order.products.remove(order_product)
            order_product.delete()
            messages.info(request, "Produkt usunięty z koszyka")
            return redirect("cart")
        else:
            #addidional message - product does not exist in this order
            messages.info(request, "Produkt nie był w koszyku")
            return redirect("cart")
    else:
        #addidional message - order does not exist
        messages.info(request, "Brak koszyka")
        return redirect("products:product-detail", slug=slug)

@login_required(login_url='/account/login/')
def remove_single_from_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.products.filter(product__slug=product.slug).exists():
            order_product = OrderProduct.objects.filter(product=product, user=request.user, ordered=False)[0]
            if order_product.quantity == 1:
                order.products.remove(order_product)
                order_product.delete()
                messages.info(request, "Produkt usunięty z koszyka")
                return redirect("cart")
            else:
                order_product.quantity -= 1
                order_product.save()
                messages.info(request, "Zaktualizowano stan koszyka")
                return redirect("cart")
        else:
            #addidional message - product does not exist in this order
            messages.info(request, "Produkt nie był w koszyku")
            return redirect("cart")
    else:
        #addidional message - order does not exist
        messages.info(request, "Brak koszyka")
        return redirect("products:product-detail", slug=slug)
    