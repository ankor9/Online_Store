from django.db import models

class Client(models.Model):
    class Meta():
        db_table = 'clients'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    first_name = models.CharField(blank=False, null=True, max_length=60, verbose_name="First Name")
    last_name = models.CharField(blank=False, null=True, max_length=60, verbose_name="Last Name")
    email = models.EmailField(blank=False, null=False, max_length=60, verbose_name="Email")
    address = models.CharField(blank=False, null=True, max_length=40, verbose_name="Address")
    city = models.CharField(blank=False, null=True, max_length=40, verbose_name="City")
    province = models.CharField(blank=False, null=True, max_length=40, verbose_name="Province")
    country = models.CharField(blank=False, null=True, max_length=40, verbose_name="Country")
    postal_code = models.CharField(blank=False, null=True, max_length=40, verbose_name="Postal Code")

# Create your models here.
