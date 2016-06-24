from __future__ import unicode_literals

from django.db import models
from projects_api.models import Plots
from customer_api.models import Customer
from booking_api.models import Booking
from plots.lib.utils import AutoDateTimeField
from django.utils import timezone

# Create your models here.


class Sale(models.Model):

    customer = models.ForeignKey(Customer, related_name="customer")

    plot_no = models.ForeignKey(Plots, related_name="plots")

    booking = models.ForeignKey(Booking, related_name="Booking", null=True)

    is_emi_enabled = models.CharField(max_length=254, blank=True)

    created_at = models.DateField(default=timezone.now)

    updated_at = AutoDateTimeField(default=timezone.now)

    sale_completed = models.BooleanField(default=False)

    basic_cost = models.CharField(max_length=254, blank=True)

    sales_cost = models.CharField(max_length=254, blank=True)

    remaning_cost = models.CharField(max_length=254, blank=True)


class EMI(models.Model):

    sale = models.ForeignKey(Customer, related_name="Sale")

    created_at = models.DateField(default=timezone.now)

    updated_at = AutoDateTimeField(default=timezone.now)

    emi_schedule_date = models.DateField(null=True)

    paid = models.BooleanField(default=False)


class SaleTransaction(models.Model):

    sale = models.ForeignKey(Customer, related_name="Sale")

    amount = models.CharField(max_length=254, blank=True)

    trasaction_type = models.CharField(max_length=254, blank=True)

    trasaction_type_no = models.CharField(max_length=254, blank=True)

    created_at = models.DateField(default=timezone.now)

    is_emi = models.BooleanField(default=False)

    emi = models.ForeignKey(EMI, related_name="EMI")

    status = models.BooleanField(default=True)
