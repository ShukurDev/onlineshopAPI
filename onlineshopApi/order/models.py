from django.db import models
from accounts.models import Profile, Address
from products.models import Product


# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='order_user')
    ordered = models.BooleanField(default=False, null=True, blank=True)
    address = models.OneToOneField(Address, on_delete=models.SET_NULL, related_name='profile_addresss', null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    barcode = models.CharField(max_length=20, null=True, blank=True)
    region = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    district = models.CharField(max_length=300, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    target = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Order -> by {self.user}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderitems')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    quantity = models.BigIntegerField(null=True, blank=True, verbose_name='order_item_qantity')
    date_added = models.DateField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return str(self.quantity)

