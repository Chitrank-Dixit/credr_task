# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='transaction',
            unique_together=set([('invoice', 'product')]),
        ),
    ]
