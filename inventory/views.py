from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from models import Invoice, Transaction
from serializers import InvoiceSerializer, TransactionSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
	queryset = Invoice.objects.all()
	serializer_class = InvoiceSerializer

	# def create(self, request, *args, **kwargs):
	# 	data = request.DATA

	# 	#invoice_instance = Invoice.objects.create()
	# 	return Response(serializer.data, status=status.HTTP_201_CREATED,headers=headers)


class TransactionViewSet(viewsets.ModelViewSet):
	queryset = Transaction.objects.all()
	serializer_class = TransactionSerializer

# class InvoiceTransactionViewSet(viewsets.ModelViewSet):
# 	queryset = Invoice.objects.all()
# 	serializer_class = InvoiceTransactionViewSet


