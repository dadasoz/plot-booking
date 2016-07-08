from rest_framework import serializers
from booking_api.models import Booking
from customer_api.serializers import CustomerDetailsSerializer
from accounts_api.serializers import DetailsSalesSerializerForBooking
from projects_api.serializers import PlotDetailsSerializer


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = (
            'pk', 'plot_no', 'customer', 'booking_amount', 'is_booking_cancled',)


class BookingListSerializer(serializers.ModelSerializer):

    customer_name = serializers.CharField(
        source='customer.full_name', read_only=True)

    plot_no = serializers.CharField(source='plot_no.plot_no', read_only=True)

    plot_id = serializers.CharField(source='plot_no.pk', read_only=True)

    basic_amount = serializers.CharField(
        source='plot_no.basic_cost', read_only=True)

    customer_email = serializers.CharField(
        source='customer.email', read_only=True)

    customer_mobile = serializers.CharField(
        source='customer.mobile', read_only=True)

    class Meta:

        model = Booking
        fields = (
            'pk', 'plot_no', 'customer', 'booking_amount', 'is_booking_cancled', 'customer_name', 'plot_id', 'basic_amount', 'customer_email', 'customer_mobile')


class BookingDetailsSerializer(serializers.ModelSerializer):

    customer = CustomerDetailsSerializer(read_only=True)

    plot_no = PlotDetailsSerializer(read_only=True)

    sale_booking = DetailsSalesSerializerForBooking(many=True, read_only=True)

    class Meta:
        model = Booking
        fields = (
            'pk', 'plot_no', 'customer', 'booking_amount', 'is_booking_cancled', 'booking_date', 'sale_booking', 'booking_txn_no', 'booking_amount_method', 'down_payment', 'down_payment_date', 'down_payment_method', 'down_payment_txn_no')


class CreateBookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = (
            'pk', 'plot_no', 'customer', 'booking_amount', 'booking_date', 'booking_txn_no', 'booking_amount_method', 'down_payment', 'down_payment_date', 'down_payment_method', 'down_payment_txn_no')
