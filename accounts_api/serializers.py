from rest_framework import serializers
from accounts_api.models import Sale, EMI, EMI_schedule


class SalesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sale


class EMISerializer(serializers.ModelSerializer):

    class Meta:
        model = EMI


class CreateSalesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sale
        fields = ('pk', 'customer', 'plot_no', 'booking', 'is_emi_enabled', 'basic_cost',
                  'sales_cost', 'remaning_cost')


class CreateEMISerializer(serializers.ModelSerializer):

    class Meta:
        model = EMI
        fields = ('pk', 'sale', 'total_amount', 'paid_amount', 'intrest_rate',
                  'total_intrest', 'duration')


class ListSalesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sale


class ListEMI_scheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = EMI_schedule
        fields = ('pk', 'emi', 'created_at', 'updated_at', 'emi_schedule_date',
                  'amount', 'paid_status')


class ListEMISerializer(serializers.ModelSerializer):

    class Meta:
        model = EMI


class DetailsEMISerializer(serializers.ModelSerializer):

    emi_data = ListEMI_scheduleSerializer(many=True, read_only=True)

    class Meta:
        model = EMI


class DetailsSalesSerializer(serializers.ModelSerializer):

    emi_sale = DetailsEMISerializer(many=True, read_only=True)

    class Meta:
        model = Sale
