# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0013_transaction__line_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='_line_total',
        ),
    ]
