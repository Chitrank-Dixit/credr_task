from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from models import Invoice, Transaction
from serializers import InvoiceSerializer, TransactionSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
	queryset = Invoice.objects.all()
	serializer_class = InvoiceSerializer


class TransactionViewSet(viewsets.ModelViewSet):
	queryset = Transaction.objects.all()
	serializer_class = TransactionSerializer

# class InvoiceTransactionViewSet(viewsets.ModelViewSet):
# 	queryset = Invoice.objects.all()
# 	serializer_class = InvoiceTransactionViewSet


