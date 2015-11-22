# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20151122_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='invoice',
            field=models.ForeignKey(related_name='transactions', to='inventory.Invoice'),
        ),
    ]
