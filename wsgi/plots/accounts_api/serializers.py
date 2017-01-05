from rest_framework import serializers
from accounts_api.models import Sale, EMI, EMI_schedule, SaleTransaction, Expenses
from booking_api.models import Booking
from customer_api.serializers import CustomerDetailsSerializer, CustomerListSerializer
from projects_api.serializers import PlotDetailsSerializer

# Default serializers


class SalesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sale


class EMISerializer(serializers.ModelSerializer):

    class Meta:
        model = EMI


# Create View serializers

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


class CreateTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = SaleTransaction
        fields = ('pk', 'sale', 'amount', 'trasaction_type', 'trasaction_type_no', 'is_emi',
                  'emi_txn', 'status')

# List View serializers


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


class ListTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = SaleTransaction
        fields = ('pk', 'sale', 'amount', 'trasaction_type', 'trasaction_type_no', 'is_emi',
                  'emi_txn', 'status', 'created_at')


# Detail View serializers

class DetailsTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = SaleTransaction
        fields = ('pk', 'sale', 'amount', 'trasaction_type', 'trasaction_type_no', 'is_emi',
                  'emi_txn', 'status', 'created_at', 'source')


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

    customer = CustomerDetailsSerializer(many=False)

    plot_no = PlotDetailsSerializer(many=False)

    emi_sale = DetailsEMISerializer(many=True, read_only=True)

    sales_transactions = DetailsTransactionSerializer(
        many=True, read_only=True)

    class Meta:
        model = Sale
        fields = ('pk', 'customer', 'plot_no', 'booking', 'is_emi_enabled', 'basic_cost',
                  'sales_cost', 'remaning_cost', 'emi_sale', 'sales_transactions')


class DetailsSalesSerializerForBooking(serializers.ModelSerializer):

    emi_sale = DetailsEMISerializer(many=True, read_only=True)

    sales_transactions = DetailsTransactionSerializer(
        many=True, read_only=True)

    class Meta:
        model = Sale


# Update view serializers


class SalesUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sale
        fields = ('pk', 'plot_no', 'booking', 'is_emi_enabled', 'basic_cost',
                  'sales_cost', 'remaning_cost')


class EMIUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = EMI
        fields = ('pk', 'total_amount', 'paid_amount', 'intrest_rate',
                  'paid_status', 'duration', 'emi_day')


class PayEMISerializer(serializers.ModelSerializer):

    class Meta:
        model = EMI
        fields = ('pk', 'paid_status', )


class ListTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = SaleTransaction
        fields = ('sale', 'amount', 'trasaction_type', 'trasaction_type_no', 'is_emi',
                  'emi_txn', 'status', 'created_at', 'source')


class CreateTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = SaleTransaction
        fields = ('sale', 'amount', 'trasaction_type', 'trasaction_type_no', 'is_emi',
                  'emi_txn', 'status', 'created_at', 'source')


class UpdateTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = SaleTransaction
        fields = ('pk', 'sale', 'amount', 'trasaction_type', 'trasaction_type_no', 'is_emi',
                  'emi_txn', 'status', 'created_at', 'source')


class UpdateTransactionStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = SaleTransaction
        fields = ('pk', 'status')


class DetailsTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = SaleTransaction
        fields = ('pk', 'sale', 'amount', 'trasaction_type', 'trasaction_type_no', 'is_emi',
                  'emi_txn', 'status', 'created_at', 'source')



# Expenses serializers

class ListExpensesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expenses

class CreateExpensesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expenses


class UpdateExpensesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expenses


class DetailsExpensesSerializer(serializers.ModelSerializer):

    class Meta:
        model = SaleTransaction
