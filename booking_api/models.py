from __future__ import unicode_literals

from django.db import models
from projects_api.models import Plots
from customer_api.models import Customer
from plots.lib.utils import AutoDateTimeField
from django.utils import timezone
from datetime import datetime


class Booking(models.Model):

    plot_no = models.ForeignKey(Plots, related_name="plots")

    updated_at = AutoDateTimeField(default=datetime.now())

    is_booking_cancled = models.CharField(max_length=254, blank=True)

    customer = models.ForeignKey(Customer, related_name="customer")

    booking_date = models.CharField(max_length=254)

    booking_amount = models.CharField(max_length=254, blank=True)

    booking_txn_no = models.CharField(max_length=254, blank=True)

    booking_amount_method = models.CharField(max_length=254, blank=True)

    down_payment = models.CharField(max_length=254, blank=True)

    down_payment_date = models.CharField(max_length=254, blank=True)

    down_payment_method = models.CharField(max_length=254, blank=True)

    down_payment_txn_no = models.CharField(max_length=254, blank=True)
