from django.shortcuts import render
from datetime import datetime
# Create your views here.
from products.models import ProductCategory, Product

def index(request):
    context = {
        'title': 'GeekShop',
        'today': datetime.now(),
    }
    return render(request, 'products/index.html', context)

def products(request):
    db_categories = ProductCategory.objects.all()
    db_products = Product.objects.all()
    context = {'title': 'GeekShop - Каталог',
                'products': db_products,
                'categories': db_categories,
               }

    return render(request,'products/products.html', context)

