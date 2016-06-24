from django.db import models
import datetime


class AutoDateTimeField(models.DateTimeField):

    def pre_save(self, model_instance, add):
        return datetime.datetime.now()
