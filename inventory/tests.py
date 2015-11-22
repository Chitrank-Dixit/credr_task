from django.test import TestCase
from inventory.models import Invoice, Transaction
# Create your tests here.

class InvoiceTestCase(TestCase):
	def setUp(self):
		Invoice.objects.create(customer="Ram")
        Invoice.objects.create(customer="Shyam")

class Transaction(TestCase):
	def setUp(self):
		invoice = Invoice.objects.get(pk=1)
		Transaction.objects.create(product='Maggi Noodles', quantity=12, price=5.00, invoice=invoice)
		Transaction.objects.create(product='Pizza', quantity=4, price=90.00, invoice=invoice)