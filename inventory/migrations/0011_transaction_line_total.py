# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_auto_20151122_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='line_total',
            field=models.DecimalField(default=0.0, max_digits=10, decimal_places=2),
        ),
    ]
