# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0062_auto_20160411_1509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='real_purchase',
            name='customer_pend',
        ),
        migrations.RemoveField(
            model_name='real_purchase',
            name='customer_type',
        ),
        migrations.AlterField(
            model_name='real_purchase',
            name='customer',
            field=models.ForeignKey(default=1, verbose_name='\u5ba2\u6237\u59d3\u540d', to='erp.Customer'),
            preserve_default=False,
        ),
    ]
