from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from plots.lib.utils import AutoDateTimeField
from projects_api.models import Project

# Create your models here.


class Feedback(models.Model):

    """
    Feedback model
    """

    # Personal Details

    name = models.CharField(max_length=254, blank=True)

    email = models.CharField(max_length=254, blank=True)

    mobile = models.CharField(max_length=254, blank=True)

    message = models.TextField(max_length=1000, blank=True)

    created_at = models.DateTimeField(default=timezone.now)

    updated_at = AutoDateTimeField(default=timezone.now)

    parent = models.ForeignKey("self", null=True, related_name="parent_feedback")

    project = models.ForeignKey(Project, related_name="project_feedback", null=True)

    def __unicode__(self):
        return self.name()
