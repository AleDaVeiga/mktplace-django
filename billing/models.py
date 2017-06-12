from django.contrib.auth.models import User
from django.db import models


class Order(models.Model):
    user = models.ForeignKey(User, related_name='order_user')
    merchant = models.ForeignKey(User, related_name='order_merchant')
    commission = models.DecimalField(max_digits=8, decimal_places=2)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Refused', 'Refused'),
        ('Approved', 'Approved'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Inactive")

    def __unicode__(self):
        return "#" + str(self.id)

