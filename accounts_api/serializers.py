from rest_framework import serializers
from accounts_api.models import Sale, EMI, EMI_schedule
from projects_api.serializers import PlotDetailsSerializer


class CreateSalesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sale
        fields = ('pk', 'customer', 'plot_no', 'booking', 'is_emi_enabled', 'basic_cost',
                  'sales_cost', 'remaning_cost')


class ListSalesSerializer(serializers.ModelSerializer):
    plot_details = PlotDetailsSerializer

    class Meta:
        model = Sale


class CreateEMISerializer(serializers.ModelSerializer):

    class Meta:
        model = EMI
        fields = ('pk', 'sale', 'total_amount', 'paid_amount', 'intrest_rate',
                  'total_intrest', 'duration')


class ListEMISerializer(serializers.ModelSerializer):

    class Meta:
        model = EMI
