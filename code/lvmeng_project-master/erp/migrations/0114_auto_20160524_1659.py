# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0113_auto_20160524_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='risk_preference',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='\u5ba2\u6237\u98ce\u9669\u504f\u597d', choices=[(b'1', '\u6781\u4f4e\u98ce\u9669\u578b'), (b'2', '\u6781\u4f4e\u98ce\u9669\u578b'), (b'3', '\u8f83\u4f4e\u98ce\u9669\u578b'), (b'4', '\u4e2d\u7b49\u98ce\u9669\u578b'), (b'5', '\u8f83\u9ad8\u98ce\u9669\u578b'), (b'6', '\u9ad8\u98ce\u9669\u578b')]),
        ),
        migrations.AlterField(
            model_name='customer_pending',
            name='risk_preference',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='\u5ba2\u6237\u98ce\u9669\u504f\u597d', choices=[(b'1', '\u6781\u4f4e\u98ce\u9669\u578b'), (b'2', '\u6781\u4f4e\u98ce\u9669\u578b'), (b'3', '\u8f83\u4f4e\u98ce\u9669\u578b'), (b'4', '\u4e2d\u7b49\u98ce\u9669\u578b'), (b'5', '\u8f83\u9ad8\u98ce\u9669\u578b'), (b'6', '\u9ad8\u98ce\u9669\u578b')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='risk_preference',
            field=models.CharField(default=b'3', max_length=10, verbose_name='\u98ce\u9669\u7c7b\u578b', choices=[(b'1', '\u6781\u4f4e\u98ce\u9669\u578b'), (b'2', '\u6781\u4f4e\u98ce\u9669\u578b'), (b'3', '\u8f83\u4f4e\u98ce\u9669\u578b'), (b'4', '\u4e2d\u7b49\u98ce\u9669\u578b'), (b'5', '\u8f83\u9ad8\u98ce\u9669\u578b'), (b'6', '\u9ad8\u98ce\u9669\u578b')]),
        ),
    ]
