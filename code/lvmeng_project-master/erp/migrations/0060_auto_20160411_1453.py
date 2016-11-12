# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0059_customer_product_target'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='product_target',
        ),
        migrations.AlterField(
            model_name='customer',
            name='agents',
            field=models.ManyToManyField(to='erp.Agent', null=True, verbose_name='\u6240\u5c5e\u7406\u8d22\u5e08', blank=True),
        ),
    ]
