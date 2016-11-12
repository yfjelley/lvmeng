# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oa', '0009_auto_20160324_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cost_application',
            name='cost',
            field=models.DecimalField(verbose_name=b'\xe9\x87\x91\xe9\xa2\x9d', max_digits=15, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='travel_apply',
            name='travel_cost',
            field=models.DecimalField(verbose_name=b'\xe9\x87\x91\xe9\xa2\x9d', max_digits=15, decimal_places=2),
        ),
    ]
