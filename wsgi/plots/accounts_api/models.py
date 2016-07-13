from __future__ import unicode_literals

from django.db import models
from projects_api.models import Plots
from customer_api.models import Customer
from booking_api.models import Booking
from plots.lib.utils import AutoDateTimeField
from django.utils import timezone

# Create your models here.


class Sale(models.Model):

    customer = models.ForeignKey(Customer, related_name="sale_customer")

    plot_no = models.ForeignKey(Plots, related_name="sale_plots")

    booking = models.ForeignKey(
        Booking, related_name="sale_booking", null=True)

    is_emi_enabled = models.BooleanField(default=False)

    created_at = models.DateField(default=timezone.now)

    updated_at = AutoDateTimeField(default=timezone.now)

    sale_completed = models.BooleanField(default=False)

    basic_cost = models.DecimalField(max_digits=19, decimal_places=10)

    sales_cost = models.DecimalField(max_digits=19, decimal_places=10)

    remaning_cost = models.DecimalField(max_digits=19, decimal_places=10)


class EMI(models.Model):

    sale = models.ForeignKey(Sale, related_name="emi_sale")

    created_at = models.DateField(default=timezone.now)

    updated_at = AutoDateTimeField(default=timezone.now)

    total_amount = models.DecimalField(
        default=0, max_digits=19, decimal_places=10)

    paid_amount = models.DecimalField(
        default=0, max_digits=19, decimal_places=10)

    intrest_rate = models.DecimalField(
        default=0, max_digits=19, decimal_places=2)

    total_intrest = models.DecimalField(
        default=0, max_digits=19, decimal_places=10)

    paid_status = models.BooleanField(default=False)

    duration = models.IntegerField(default=False)

    emi_day = models.IntegerField(default=False)


class EMI_schedule(models.Model):

    emi = models.ForeignKey(EMI, related_name="emi_data")

    created_at = models.DateField(default=timezone.now)

    updated_at = AutoDateTimeField(default=timezone.now)

    emi_schedule_date = models.DateField(null=True)

    amount = models.DecimalField(max_digits=19, decimal_places=10)

    paid_status = models.BooleanField(default=False)


class SaleTransaction(models.Model):

    sale = models.ForeignKey(Sale, related_name="sales_transactions")

    amount = models.DecimalField(max_digits=19, decimal_places=10)

    source = models.CharField(max_length=254, blank=True)

    trasaction_type = models.CharField(max_length=254, blank=True)

    trasaction_type_no = models.CharField(max_length=254, blank=True)

    created_at = models.DateField(default=timezone.now)

    is_emi = models.BooleanField(default=False)

    emi_txn = models.ForeignKey(
        EMI_schedule, related_name="sales_transaction_emi", null=True)

    status = models.BooleanField(default=True)
