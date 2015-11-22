from django.db import models

# Create your models here.

class Invoice(models.Model):
	customer = models.CharField(max_length=50)
	date = models.DateTimeField(auto_now=True)
	total_quantity = models.IntegerField(blank=True, default=0)
	total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, blank=True)

	class Meta:
		unique_together = ('customer', 'date')

	def __unicode__(self):
		return '%s: %s' % (self.customer, self.date)

class Transaction(models.Model):
	product = models.CharField(max_length = 50)
	quantity = models.IntegerField(default=0)
	price = models.DecimalField(max_digits=10,decimal_places=2, default=0.0)
	line_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
	invoice = models.ForeignKey(Invoice, related_name='transactions')

	@property
	def line_total(self):
		# line_total = float(self.quantity * self.price)
		# self.line_total = line_total
		# return self.line_total
		# self.line_total = (self.quantity * self.price)
		return float(self.quantity * self.price)

	# @line_total.setter
	# def line_total(self, value):
	# 	self._line_total = self.quantity * self.price

	# also we can try this out

	# line_total = property(line_total)


	class Meta:
		unique_together =  ('invoice', 'product')

	def __unicode__(self):
		return '%s: %d' % (self.product, self.quantity)