from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from plots.lib.utils import AutoDateTimeField
# Create your models here.

class Customer(models.Model):
    """
    Customer model
    """

    # Personal Details

    first_name = models.CharField(max_length=254, blank=True)

    middle_name = models.CharField(max_length=254, blank=True)

    last_name = models.CharField(max_length=254, blank=True)

    occupation = models.CharField(max_length=254, blank=True)

    dob = models.CharField(max_length=254, blank=True)

    age = models.CharField(max_length=254, blank=True)

    marriage_anniversary = models.CharField(max_length=254, blank=True)

    agriculture_status = models.CharField(max_length=254, blank=True)

    purpose_of_buying = models.TextField(max_length=254, blank=True)


    # Contact Details

    email = models.CharField(max_length=254, blank=True)

    mobile = models.CharField(max_length=254, blank=True)

    alternate_mobile = models.CharField(max_length=254, blank=True)

    address1 = models.TextField(max_length=254, blank=True)

    address2 = models.TextField(max_length=254, blank=True)

    pin_code = models.CharField(max_length=254, blank=True)

    photo = models.ImageField(upload_to='customers', null=True)

    # Nominee Details

    nominee_name = models.CharField(max_length=254, blank=True)

    nominee_address = models.TextField(max_length=254, blank=True)

    nominee_email = models.CharField(max_length=254, blank=True)

    nominee_mobile = models.CharField(max_length=254, blank=True)

    nominee_alternate_mobile = models.CharField(max_length=254, blank=True)

    nominee_photo = models.ImageField(upload_to='nominee', null=True)

    nominee_dob = models.CharField(max_length=254, blank=True)

    nominee_age = models.CharField(max_length=254, blank=True)

    nominee_occupation = models.CharField(max_length=254, blank=True)

    relation = models.CharField(max_length=254, blank=True)

    created_at = models.DateTimeField(default=timezone.now)

    updated_at = AutoDateTimeField(default=timezone.now)

    def full_name(self):
        return "{0} {1} {2}".format(self.first_name,self.middle_name,self.last_name)

    def __unicode__(self):
        return self.get_full_name()

