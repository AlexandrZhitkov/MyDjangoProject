from django.contrib import admin

from baskets.models import Basket

class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity',)
    extra = 0
