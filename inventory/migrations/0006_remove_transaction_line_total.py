# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20151122_1613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='line_total',
        ),
    ]
