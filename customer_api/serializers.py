from rest_framework import serializers
from customer_api.models import Customer


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer

class CustomerListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('pk', 'full_name', 'email', 'mobile', 'alternate_mobile', 'address1')