from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Customer(models.Model):
    """
    Customer model
    """
    first_name = models.CharField(max_length=254, blank=True)

    middle_name = models.CharField(max_length=254, blank=True)

    last_name = models.CharField(max_length=254, blank=True)

    email = models.CharField(max_length=254, blank=True)

    mobile = models.CharField(max_length=254, blank=True)

    alternet_mobile = models.CharField(max_length=254, blank=True)

    address1 = models.CharField(max_length=254, blank=True)

    address2 = models.CharField(max_length=254, blank=True)

    pin_code = models.CharField(max_length=254, blank=True)
