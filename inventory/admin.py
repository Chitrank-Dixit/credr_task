from django.contrib import admin
from models import Invoice, Transaction

class InvoiceAdmin(admin.ModelAdmin):
	list_display = ['customer', 'date', 'total_quantity', 'total_amount']
	list_filter = ['customer', 'date', 'total_quantity', 'total_amount']
	search_fields = ['customer', 'date', 'total_quantity', 'total_amount']

admin.site.register(Invoice, InvoiceAdmin)

class TransactionAdmin(admin.ModelAdmin):
	list_display = ['product','quantity', 'price']
	list_filter = ['product','quantity', 'price']
	search_fields = ['product','quantity', 'price']

admin.site.register(Transaction, TransactionAdmin)

