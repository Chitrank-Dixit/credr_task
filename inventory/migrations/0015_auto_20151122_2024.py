# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_remove_transaction__line_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='total_quantity',
            field=models.IntegerField(default=0, blank=True),
        ),
    ]
