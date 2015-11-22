from rest_framework import serializers

from models import Invoice, Transaction


# read this to fix the issue
# http://www.django-rest-framework.org/api-guide/relations/

class TransactionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Transaction
		fields = ('product','quantity','price','line_total','invoice')

class InvoiceSerializer(serializers.ModelSerializer):
	transactions = TransactionSerializer(many=True, read_only=True)
	
	class Meta:
		model = Invoice
		fields = ('customer','date','total_quantity','total_amount','transactions')

	# def create(self, validated_data):
	# 	transactions_data = validated_data.pop('transactions')
	# 	invoice = Invoice.objects.create(**validated_data)
	# 	for transaction_data in transactions_data:
	# 		Transaction.objects.create(invoice=invoice, **track_data)
	# 	return invoice

