from django.db import models

# Create your models here.

class Invoice(models.Model):
	customer = models.CharField(max_length=50)
	date = models.DateTimeField(auto_now=True)
	total_quantity = models.IntegerField(default=0)
	total_amount = models.DecimalField(max_digits=5, decimal_places=2)

	def __unicode__(self):
		return self.customer

class Transaction(models.Model):
	product = models.CharField(max_length = 50)
	quantity = models.IntegerField(default=0)
	price = models.DecimalField(max_digits=5,decimal_places=2)
	line_total = models.DecimalField(max_digits=5, decimal_places=2)
	invoice = models.ForeignKey(Invoice, related_name='transactions')


	class Meta:
		unique_together =  ('invoice', 'product')

	def __unicode__(self):
		return '%s: %d' % (self.product, self.quantity)