from rest_framework import serializers
from admin_api.models import Company, CommissionSettings


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company


class CompanyDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company

class CommissionSettingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommissionSettings


class CommissionSettingsDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommissionSettings

