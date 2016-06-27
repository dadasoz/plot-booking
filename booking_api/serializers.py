from rest_framework import serializers
from booking_api.models import Booking


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ('pk', 'plot_no', 'customer', 'booking_amount', 'is_booking_cancled',)
