from rest_framework import serializers
from booking_api.models import Booking


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

    class Meta:
        model = Booking
        fields = (
            'pk', 'plot_no', 'customer', 'booking_amount', 'is_booking_cancled')


class CreateBookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = (
            'plot_no', 'customer', 'booking_amount')
