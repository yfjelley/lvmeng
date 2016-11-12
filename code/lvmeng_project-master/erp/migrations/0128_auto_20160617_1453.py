# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0127_auto_20160616_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='abbreviation',
            field=models.CharField(max_length=100, verbose_name='\u4ea7\u54c1\u7b80\u79f0(\u663e\u793a\u5728app\u9875)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='\u672a\u547d\u540d', max_length=100, verbose_name='\u4ea7\u54c1\u5168\u540d(\u663e\u793a\u5728web\u9875)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='return_expected',
            field=models.DecimalField(verbose_name='\u9884\u671f\u5e74\u5316\u6536\u76ca(\u663e\u793a\u5728\u9996\u9875)', max_digits=6, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='product',
            name='subscription_fee',
            field=models.DecimalField(null=True, verbose_name='\u8ba4\u8d2d\u8d39', max_digits=6, decimal_places=4, blank=True),
        ),
    ]
