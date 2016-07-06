from accounts_api import serializers
from rest_framework import generics
from rest_framework.response import Response
from accounts_api.models import Sale, EMI, EMI_schedule
from plots.lib.utils import calculateEMI
from dateutil import rrule
from datetime import datetime, date



class CreateSales(generics.CreateAPIView):

    serializer_class = serializers.CreateSalesSerializer

    def perform_create(self, serializer):
        serializer.save()


class ListSales(generics.ListAPIView):
    queryset = Sale.objects.all()
    serializer_class = serializers.ListSalesSerializer

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = serializers.ListSalesSerializer(queryset, many=True)
        return Response(serializer.data)


class CreateEMI(generics.CreateAPIView):

    serializer_class = serializers.CreateEMISerializer

    def perform_create(self, serializer):
        emi = serializer.save()
        self.createEMI(emi)

    def createEMI(self, emi):
        monthly_emi = calculateEMI(
            emi.total_amount, emi.intrest_rate, emi.duration)
        months = int(emi.duration)

        now = date(datetime.now().year, datetime.now().month, 7)
        tm = 0
        for dt in rrule.rrule(rrule.MONTHLY, dtstart=now):
            tm = tm + 1
            EMI_schedule(
                emi=emi, emi_schedule_date=dt, amount=monthly_emi).save()
            if tm == months:
                break


class ListEMI(generics.ListAPIView):

    def list(self, request, sales_id):
        sale = Sale.objects.get(pk=sales_id)
        queryset = EMI.objects.filter(sale=sale)
        serializer = serializers.ListSalesSerializer(queryset, many=True)
        return Response(serializer.data)
