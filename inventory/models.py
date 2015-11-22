from django.db import models

# Create your models here.

class Invoice(models.Model):
	customer = models.CharField(max_length=50)
	date = models.DateTimeField(auto_now=True)
	total_quantity = models.IntegerField(null=True)
	total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)

	class Meta:
		unique_together = ('customer', 'date')

	def __unicode__(self):
		return '%s: %s' % (self.customer, self.date)

class Transaction(models.Model):
	product = models.CharField(max_length = 50)
	quantity = models.IntegerField(default=0, null=True)
	price = models.DecimalField(max_digits=10,decimal_places=2, null=True)
	#line_total = models.DecimalField(max_digits=10, decimal_places=2)
	invoice = models.ForeignKey(Invoice, related_name='transactions')

	@property
	def line_total(self):
	    return (self.quantity * self.price)

	class Meta:
		unique_together =  ('invoice', 'product')

	def __unicode__(self):
		return '%s: %d' % (self.product, self.quantity)