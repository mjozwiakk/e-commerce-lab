from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from products.models import Product, Order
from .forms import CheckoutForm
# Create your views here.

def home_view(request, *args, **kwargs):
    queryset = Product.objects.all()[:8]
    context = {
        "new_products": queryset
    }
    return render(request, 'home.html', context)
    
def contact_view(request, *args, **kwargs):
    my_context = {
    }
    return render(request, 'contact.html', my_context)
    

def cart_view(request, *args, **kwargs):
    if Order.objects.filter(user=request.user, ordered=False).exists():
        order = Order.objects.get(user=request.user, ordered=False)
        context = {
            'order': order,
        }
        return render(request, 'cart.html', context)
    else:
        order = Order.objects.create(user=request.user, ordered=False)
        context = {
            'order': order,
        }
        return render(request, 'cart.html', context)
    
def checkout_view(request, *args, **kwargs):
    order = Order.objects.get(user=request.user, ordered=False)
    form = CheckoutForm()

    context = {
        'order': order,
        'form': form,
    }
    return render(request, 'checkout.html', context)
    