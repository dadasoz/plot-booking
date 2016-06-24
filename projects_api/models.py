from __future__ import unicode_literals

from plots.lib.utils import AutoDateTimeField

from django.db import models
from django.utils import timezone
# Create your models here.

class Project(models.Model):

    """
    Project model
    """
    name = models.CharField(max_length=254, blank=False)

    description = models.CharField(max_length=254, blank=True)

    address = models.TextField(max_length=254, blank=False)

    area = models.CharField(max_length=254, blank=False)

    plot_no = models.CharField(max_length=254, blank=True)

    gat_no = models.CharField(max_length=254, blank=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateField(default=timezone.now)

    updated_at = AutoDateTimeField(default=timezone.now)

    start_date = models.DateField(default=timezone.now)

    date_closed = models.DateField(blank=True, null=True)


class Plots(models.Model):

    """
    List of all plots

    """
    plot_no = models.IntegerField(blank=False)

    basic_cost = models.CharField(max_length=254, blank=True)

    is_booked = models.BooleanField(default=False)

    is_saled = models.BooleanField(default=False)

    facing = models.CharField(max_length=254, blank=True)

    width = models.CharField(max_length=254, blank=True)

    breadth = models.CharField(max_length=254, blank=True)

    area = models.CharField(max_length=254, blank=True)

    project = models.ForeignKey(Project, related_name="project")

    created_at = models.DateField(default=timezone.now)

    updated_at = AutoDateTimeField(default=timezone.now)
