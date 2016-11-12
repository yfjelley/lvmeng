# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0105_auto_20160519_1119'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='announcement',
            options={'ordering': ['order']},
        ),
        migrations.AlterField(
            model_name='customer',
            name='risk_preference',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='\u5ba2\u6237\u98ce\u9669\u504f\u597d', choices=[(b'1', '\u975e\u5e38\u4fdd\u5b88'), (b'2', '\u4fdd\u5b88'), (b'3', '\u6bd4\u8f83\u4fdd\u5b88'), (b'4', '\u6bd4\u8f83\u6fc0\u8fdb'), (b'5', '\u6fc0\u8fdb'), (b'6', '\u975e\u5e38\u6fc0\u8fdb')]),
        ),
        migrations.AlterField(
            model_name='customer_pending',
            name='risk_preference',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='\u5ba2\u6237\u98ce\u9669\u504f\u597d', choices=[(b'1', '\u975e\u5e38\u4fdd\u5b88'), (b'2', '\u4fdd\u5b88'), (b'3', '\u6bd4\u8f83\u4fdd\u5b88'), (b'4', '\u6bd4\u8f83\u6fc0\u8fdb'), (b'5', '\u6fc0\u8fdb'), (b'6', '\u975e\u5e38\u6fc0\u8fdb')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='risk_preference',
            field=models.CharField(default=b'3', max_length=10, verbose_name='\u98ce\u9669\u504f\u597d', choices=[(b'1', '\u975e\u5e38\u4fdd\u5b88'), (b'2', '\u4fdd\u5b88'), (b'3', '\u6bd4\u8f83\u4fdd\u5b88'), (b'4', '\u6bd4\u8f83\u6fc0\u8fdb'), (b'5', '\u6fc0\u8fdb'), (b'6', '\u975e\u5e38\u6fc0\u8fdb')]),
        ),
    ]
