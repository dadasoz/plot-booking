from django.db import models
import datetime


class AutoDateTimeField(models.DateTimeField):

    def pre_save(self, model_instance, add):
        return datetime.datetime.now()


def calculateEMI(loan_amount, interest_rate, payment_period):
    loan_amount = float(loan_amount)
    interest_rate = float(interest_rate)
    payment_period = float(payment_period)
    if interest_rate == 0:
        return loan_amount/payment_period
    else:
        return (
            loan_amount*pow((interest_rate/12)+1, (payment_period))*interest_rate/12)/(pow(interest_rate/12+1, (payment_period)) - 1)
