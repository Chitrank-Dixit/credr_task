# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_remove_transaction_line_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='total_amount',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='total_quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='price',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='quantity',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
