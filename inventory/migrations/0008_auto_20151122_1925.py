# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_auto_20151122_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='total_amount',
            field=models.DecimalField(default=0.0, max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='total_quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='price',
            field=models.DecimalField(default=0.0, max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
