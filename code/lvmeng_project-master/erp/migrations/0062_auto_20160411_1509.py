# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0061_customer_product_target'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ahead_end',
            field=models.BooleanField(default=False, verbose_name='\u53ef\u63d0\u524d\u7ed3\u675f'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_sum',
            field=models.PositiveIntegerField(null=True, verbose_name='\u4ea7\u54c1\u603b\u989d', blank=True),
        ),
    ]
