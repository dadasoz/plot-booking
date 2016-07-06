from rest_framework import serializers
from accounts_api.models import Sale
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
