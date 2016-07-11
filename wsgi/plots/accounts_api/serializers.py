from rest_framework import serializers
from accounts_api.models import Sale, EMI, EMI_schedule
from customer_api.serializers import CustomerListSerializer
from booking_api.models import Booking


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
                  'total_intrest', 'duration', 'emi_day')


class ListSalesSerializer(serializers.ModelSerializer):
    customer = CustomerListSerializer(read_only=True)
    plot_no = serializers.IntegerField(source="plot_no.plot_no")

    class Meta:
        model = Sale
        fields = ('pk', 'customer', 'plot_no', 'booking', 'is_emi_enabled', 'basic_cost',
                  'sales_cost', 'remaning_cost')


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


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = (
            'pk', 'booking_amount', 'is_booking_cancled', 'booking_date', 'booking_txn_no', 'booking_amount_method', 'down_payment', 'down_payment_date', 'down_payment_method', 'down_payment_txn_no')


class DetailsSalesSerializer(serializers.ModelSerializer):

    booking = BookingSerializer(many=False)

    emi_sale = DetailsEMISerializer(many=True, read_only=True)

    class Meta:
        model = Sale
        fields = ('pk', 'customer', 'plot_no', 'booking', 'is_emi_enabled', 'basic_cost',
                  'sales_cost', 'remaning_cost','emi_sale')


class DetailsSalesSerializerForBooking(serializers.ModelSerializer):

    emi_sale = DetailsEMISerializer(many=True, read_only=True)

    class Meta:
        model = Sale
