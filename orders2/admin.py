from django.contrib import admin
from .models import *


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'client',
        'date',
        'payment_method',
        'delivery_method',
        'delivery_date',
        'total_price'
    ]


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = [
        'order',
        'product',
        'date',
        'item_price',
        'product_quantity',
        'sub_total'
    ]