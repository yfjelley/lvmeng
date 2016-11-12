# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0098_product_contract'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='province',
            field=models.CharField(max_length=30, null=True, verbose_name='\u6240\u5728\u7701\u4efd', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='structure',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u7ed3\u6784\u5316'),
        ),
    ]
