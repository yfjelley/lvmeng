# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0056_customer_customer_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='brief',
            field=models.TextField(max_length=150, null=True, verbose_name='\u5907\u6ce8', blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='agents',
            field=models.ManyToManyField(to='erp.Agent', verbose_name='\u6240\u5c5e\u7406\u8d22\u5e08'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_type',
            field=models.CharField(default=b'2', max_length=2, verbose_name='\u5ba2\u6237\u7c7b\u578b', choices=[(b'1', '\u771f\u5b9e\u5ba2\u6237'), (b'2', '\u610f\u5411\u5ba2\u6237')]),
        ),
    ]
