from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from products.models import Product, Order
from .forms import CheckoutForm, ConfirmOrderForm
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

    if request.method == "POST":
        form = CheckoutForm(request.POST or None)
        if form.is_valid():
            order.first_name = form.cleaned_data.get('first_name')
            order.last_name = form.cleaned_data.get('last_name')
            order.company = form.cleaned_data.get('company')
            order.city = form.cleaned_data.get('city')
            order.zip_code = form.cleaned_data.get('zip_code')
            order.address = form.cleaned_data.get('address')
            if form.cleaned_data.get('payment') == 'P':
                order.payment = 'Przelew bankowy'
            elif form.cleaned_data.get('payment') == 'O':
                order.payment = 'Płatnośc przy odbiorze'
            order.save()
            return redirect("order-summary")
            
    else:
        form = CheckoutForm()
    
    context = { 
        'order': order, 
        'form': form,
    }
    return render(request, 'checkout.html', context)
    

def order_summary_view(request, *args, **kwargs):
    order = Order.objects.get(user=request.user, ordered=False)

    if request.method == "POST":
        form = ConfirmOrderForm(request.POST or None)
        if form.is_valid():

            order.ordered = True
            order_products = order.products.all()
            order_products.update(ordered=True)
            for product in order_products:
                product.save()
            order.save()
            messages.info(request, "Twoje zamówienie zostało potwierdzone")
            return redirect("home")
            
    else:
        form = ConfirmOrderForm()
    
    context = { 
        'order': order, 
        'form': form,
    }
    return render(request, 'order-summary.html', context)
    
