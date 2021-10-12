from django.shortcuts import render
from datetime import datetime
# Create your views here.

def index(request):
    context = {
        'title': 'GeekShop',
        'today': datetime.now(),
    }
    return render(request, 'products/index.html', context)

def products(request):
    context = {'title': 'GeekShop - Каталог',
               'products': [
                   {
                       'image': 'vendor/img/products/Adidas-hoodie.png',
                       'name': 'Худи черного цвета с монограммами adidas Originals',
                       'price': '6 090,00 руб.',
                       'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'
                   },
                   {
                       'image': 'vendor/img/products/Blue-jacket-The-North-Face.png',
                       'name': 'Синяя куртка The North Face',
                       'price': '23 725,00 руб.',
                       'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'
                   },
                   {
                       'image': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
                       'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                       'price': '3 390,00 руб.',
                       'description': 'Материал с плюшевой текстурой. Удобный и мягкий.'
                   },
                   {
                       'image': 'vendor/img/products/Black-Nike-Heritage-backpack.png',
                       'name': 'Черный рюкзак Nike Heritage',
                       'price': '2 340,00 руб.',
                       'description': 'Плотная ткань. Легкий материал.'
                   },
                   {
                       'image': 'vendor/img/products/Black-Dr-Martens-shoes.png',
                       'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
                       'price': '13 590,00 руб.',
                       'description': 'Гладкий кожаный верх. Натуральный материал.'
                   },
                   {
                       'image': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
                       'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
                       'price': '2 890,00 руб.',
                       'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.'
                   },

               ]}
    return render(request,'products/products.html', context)

# def test_context(request):
#     context = {
#         'title': 'GeekShop',
#         'header': 'Добро пожаловать на сайт!',
#         'user': 'Иван Иванов',
#         'products': [
#             {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090},
#             {'name': 'Синяя куртка The North Face', 'price': 23725},
#             {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390},
#         ],
#         'is_promotion': False,
#
#     }
#     return render(request, 'products/test-context.html')