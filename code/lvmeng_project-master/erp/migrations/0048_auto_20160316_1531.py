# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0047_auto_20160316_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='amount',
            field=models.IntegerField(default=1, verbose_name=b'\xe8\xb4\xad\xe4\xb9\xb0\xe9\x87\x91\xe9\xa2\x9d'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='customer',
            field=models.ForeignKey(default=1, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7', to='erp.Customer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2016, 3, 16, 15, 30, 57, 569000), verbose_name=b'\xe7\xbb\x93\xe6\x9d\x9f\xe6\x97\xa5\xe6\x9c\x9f'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='product',
            field=models.ForeignKey(default=1, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81', to='erp.Product'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='register_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 16, 15, 30, 57, 569000), verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2016, 3, 16, 15, 30, 57, 569000), verbose_name=b'\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xa5\xe6\x9c\x9f'),
            preserve_default=False,
        ),
    ]
