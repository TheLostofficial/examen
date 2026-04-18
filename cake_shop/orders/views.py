from django.shortcuts import render
from .models import Product

def product_list(request):
    """Список товаров"""
    
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'orders/product_list.html', context)
