from booking_api.models import Booking
from accounts_api import serializers
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from accounts_api.models import Sale, EMI, SaleTransaction

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

class ListEMI(generics.ListAPIView):
    
    def list(self, request, sales_id):
        sale = Sale.objects.get(pk=sales_id)
        queryset = EMI.objects.filter(sale=sale)
        serializer = serializers.ListSalesSerializer(queryset, many=True)
        return Response(serializer.data)