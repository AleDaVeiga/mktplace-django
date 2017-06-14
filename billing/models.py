from django.contrib.auth.models import User
from django.db import models

from portal.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, related_name='order_user')
    merchant = models.ForeignKey(User, related_name='order_merchant')
    product = models.ForeignKey(Product, null=True, blank=True, related_name='order_product')
    commission = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Refused', 'Refused'),
        ('Approved', 'Approved'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Inactive")
    ORDER_STATUS_CHOICES = (
        ('Received', 'Received'),
        ('Packing', 'Packing'),
        ('Posted', 'Posted'),
        ('Delivered', 'Delivered'),
    )
    order_status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default="Received")
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "#" + str(self.id)

    @property
    def get_product(self):
        return self.product

