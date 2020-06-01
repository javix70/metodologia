from django.shortcuts import render
from .models import Customer,Product,Order,OrderItem,ShippingAddress


# Create your views here.

def store(request):
    template = 'store/store.html'
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request,template,context)

def cart(request):
    template = 'store/cart.html'
    context = {}
    return render(request,template,context)

def checkout(request):
    template = 'store/checkout.html'
    context = {}
    return render(request,template,context)
