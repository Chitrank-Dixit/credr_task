# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20151122_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='total_quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='line_total',
            field=models.DecimalField(max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='price',
            field=models.DecimalField(max_digits=10, decimal_places=2),
        ),
        migrations.AlterUniqueTogether(
            name='invoice',
            unique_together=set([('customer', 'date')]),
        ),
    ]
