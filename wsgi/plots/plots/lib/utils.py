from django.db import models
import datetime


class AutoDateTimeField(models.DateTimeField):

    def pre_save(self, model_instance, add):
        return datetime.datetime.now()


class EMI_CALCULATOR(object):

    def __init__(self, Loan_amount, Interest_rate, Payment_period):

        self.Loan_amount = float(Loan_amount)
        self.Interest_rate = float(Interest_rate)
        self.Payment_period = int(Payment_period)
        self.Month_Payment = None

    def calc_interest_rate(self):
        # To calculate the  interest rate"
        self.Interest_rate = (self.Interest_rate / 100.0)

    def calc_emi(self):
        try:
            self.calc_interest_rate()
        except NameError:
            return NameError

        try:
            self.Month_Payment = (self.Loan_amount*pow((self.Interest_rate/12)+1,
                                                       (self.Payment_period))*self.Interest_rate/12)/(pow(self.Interest_rate/12+1,
                                                                                                          (self.Payment_period)) - 1)
        except ZeroDivisionError:
            return self.Loan_amount / self.Payment_period
        else:
            return self.Month_Payment