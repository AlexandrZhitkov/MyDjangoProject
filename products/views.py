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

def products(request, category_id=None):
    db_categories = ProductCategory.objects.all()
    db_products = Product.objects.all()
    context = {'title': 'GeekShop - Каталог',
                'products': db_products,
                'categories': db_categories,
               }
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    context['products'] = products

    return render(request,'products/products.html', context)

