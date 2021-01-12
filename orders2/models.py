from django.db import models
from clients2.models import Client
from products2.models import Product

class Order(models.Model):
    class Meta():
        db_table = 'orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    client = models.ForeignKey(Client, blank=False, null=True, verbose_name='Client', on_delete=models.CASCADE)
    date = models.DateTimeField(blank=False, null=True, verbose_name="Date")
    payment_method = models.CharField(blank=False, null=True, max_length=60, verbose_name="Payment Method")
    delivery_method = models.CharField(blank=False, null=True, max_length=60, verbose_name="Delivery Method")
    delivery_date = models.DateTimeField(blank=False, null=False, verbose_name="Delivery Date")
    total_price = models.FloatField(blank=False, null=False, verbose_name="Total Price")

class Cart(models.Model):
    class Meta():
        db_table = 'carts'
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    order = models.ForeignKey(Order, blank=False, null=True, verbose_name='Order', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=False, null=True, verbose_name='Good', on_delete=models.CASCADE)
    date = models.DateTimeField(blank=False, null=True, verbose_name="Date")
    item_price = models.FloatField(blank=False, null=True, verbose_name="Item Price")
    product_quantity = models.IntegerField(blank=False, null=True, verbose_name="Product Quantity")
    sub_total = models.FloatField(blank=False, null=True, verbose_name="Sub Total Price")


