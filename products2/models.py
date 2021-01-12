from django.db import models

class Product(models.Model):
    class Meta():
        db_table = 'products'
        verbose_name = 'Good'
        verbose_name_plural = 'Goods'

    product_name = models.CharField(blank=False, null=True, max_length=50, verbose_name="Product Name")
    product_brand = models.CharField(blank=False, null=True, max_length=50, verbose_name="Product Brand")
    year_of_manufacturer = models.IntegerField(blank=False, null=True, verbose_name="Year of Manufacturer")
    color = models.CharField(blank=False, null=True, max_length=20, verbose_name="Color")
    description = models.CharField(blank=False, null=True, max_length=200, verbose_name="Description")
    price = models.FloatField(blank=False, null=False, verbose_name="Price")


class Category(models.Model):
    class Meta():
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    category_name = models.CharField(blank=False, null=True, max_length=100, verbose_name="Category Name")
    category_description = models.CharField(blank=True, null=True, max_length=200, verbose_name="Category Description")

class ProductCategory(models.Model):
    class Meta():
        db_table = 'products_categories'
        verbose_name = 'Product Category'
        verbose_name_plural = 'Products Categories'

    product = models.ForeignKey(Product, blank=False, null=False, verbose_name='Good', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, blank=False, null=False, verbose_name='Category', on_delete=models.CASCADE)













