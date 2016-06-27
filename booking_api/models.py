from __future__ import unicode_literals

from django.db import models
from projects_api.models import Plots
from customer_api.models import Customer
from plots.lib.utils import AutoDateTimeField
from django.utils import timezone


class Booking(models.Model):

    plot_no = models.ForeignKey(Plots, related_name="plots")

    booking_date = models.DateField(default=timezone.now)

    updated_at = AutoDateTimeField(default=timezone.now)

    booking_amount = models.CharField(max_length=254, blank=True)

    is_booking_cancled = models.CharField(max_length=254, blank=True)

    customer = models.ForeignKey(Customer, related_name="customer")
