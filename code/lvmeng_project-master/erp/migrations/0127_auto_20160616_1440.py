# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0126_agent_device_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='addition',
            field=models.BigIntegerField(null=True, verbose_name='\u8ffd\u52a0\u989d\u5ea6(\u5143)', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='mini_sub',
            field=models.BigIntegerField(verbose_name='\u8ba4\u8d2d\u8d77\u70b9/\u5143(\u663e\u793a\u5728\u9996\u9875)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_sum',
            field=models.PositiveIntegerField(null=True, verbose_name='\u4ea7\u54c1\u603b\u989d(\u5143)', blank=True),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='amount',
            field=models.IntegerField(verbose_name='\u8d2d\u4e70\u91d1\u989d(\u5143)'),
        ),
        migrations.AlterField(
            model_name='real_purchase',
            name='amount',
            field=models.IntegerField(verbose_name='\u5b9e\u6536\u91d1\u989d(\u5143)'),
        ),
    ]
