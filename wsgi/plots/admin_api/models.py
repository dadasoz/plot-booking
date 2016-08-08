from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Company(models.Model):

    """

        Company model

    """

    company_name = models.CharField(max_length=254, blank=True)

    slogan = models.CharField(max_length=254, blank=True)

    founded = models.CharField(max_length=254, blank=True)

    email = models.CharField(max_length=254, blank=True)

    phone = models.CharField(max_length=254, blank=True)

    mobile = models.CharField(max_length=254, blank=True)

    website = models.CharField(max_length=254, blank=True)

    # Address details

    alternate_mobile = models.CharField(max_length=254, blank=True)

    address = models.TextField(max_length=254, blank=True)

    pin_code = models.CharField(max_length=254, blank=True)

    logo = models.ImageField(upload_to='logo', null=True)

    created_at = models.DateTimeField(default=timezone.now)

    updated_at = models.DateTimeField(default=timezone.now)


class CommissionSettings(models.Model):

    """

        Commission model

    """

    company = models.CharField(max_length=50, blank=True)

    employee = models.CharField(max_length=50, blank=True)

    agent = models.CharField(max_length=50, blank=True)

