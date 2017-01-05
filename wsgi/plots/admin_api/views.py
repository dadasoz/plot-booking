# Create your views here.
from admin_api.models import Company, CommissionSettings
from admin_api import serializers
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class CompanyDetail(generics.RetrieveAPIView):
    serializer_class = serializers.CompanyDetailsSerializer

    def get_object(self):
        try:
            return Company.objects.get_or_create(pk=1)[0]
        except Company.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        company = self.get_object()
        serializer = serializers.CompanyDetailsSerializer(company)
        return Response(serializer.data)


class CompanyUpdate(generics.UpdateAPIView):
    serializer_class = serializers.CompanyDetailsSerializer
    def get_object(self):
        try:
            return Company.objects.get_or_create(pk=1)[0]
        except Company.DoesNotExist:
            raise Http404

    def patch(self, request, format=None):
        company = self.get_object()
        serializer = serializers.CompanyDetailsSerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommissionSettingsDetail(generics.RetrieveAPIView):
    serializer_class = serializers.CommissionSettingsDetailsSerializer

    def get_object(self):
        try:
            return CommissionSettings.objects.get_or_create(pk=1)[0]
        except CommissionSettings.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        commission = self.get_object()
        serializer = serializers.CommissionSettingsDetailsSerializer(commission)
        return Response(serializer.data)


class CommissionSettingsUpdate(generics.UpdateAPIView):
    serializer_class = serializers.CompanyDetailsSerializer
    def get_object(self):
        try:
            return CommissionSettings.objects.get_or_create(pk=1)[0]
        except CommissionSettings.DoesNotExist:
            raise Http404

    def patch(self, request, format=None):
        commission = self.get_object()
        serializer = serializers.CommissionSettingsDetailsSerializer(commission, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
