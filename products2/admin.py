from django.contrib import admin
from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'product_name',
        'product_brand',
        'year_of_manufacturer',
        'color',
        'description',
        'price'
    ]


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'product',
        'category'
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'category_name',
        'category_description'
    ]