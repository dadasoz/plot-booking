from customer_api.models import Customer
from customer_api.serializers import CustomerSerializer, CustomerListSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class CustomerList(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerListSerializer

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = CustomerListSerializer(queryset, many=True)
        return Response(serializer.data)


class CreateCustomer(generics.CreateAPIView):
    serializer_class = CustomerSerializer

    def perform_create(self, serializer):
        serializer.save()


class DestroyCustomer(generics.DestroyAPIView):
    serializer_class = CustomerSerializer

    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        customer = self.get_object(pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomerDetail(generics.RetrieveAPIView):
    serializer_class = CustomerSerializer

    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)


class CustomerUpdate(generics.UpdateAPIView):
    serializer_class = CustomerSerializer
    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def patch(self, request, pk, format=None):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
