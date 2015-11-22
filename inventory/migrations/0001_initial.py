# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('customer', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now=True)),
                ('total_quantity', models.IntegerField(default=0)),
                ('total_amount', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product', models.CharField(max_length=50)),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('line_total', models.DecimalField(max_digits=5, decimal_places=2)),
                ('invoice', models.ForeignKey(to='inventory.Invoice')),
            ],
        ),
    ]
