# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0114_auto_20160524_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ahead_end',
            field=models.BooleanField(default=False, verbose_name='\u53ef\u63d0\u524d\u7ed3\u675f(\u4ea7\u54c1\u72b6\u6001)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='finished',
            field=models.BooleanField(default=False, verbose_name='\u5df2\u5b8c\u6210(\u4ea7\u54c1\u72b6\u6001)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='structure',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u7ed3\u6784\u5316(\u4ea7\u54c1\u7c7b\u578b)'),
        ),
    ]
