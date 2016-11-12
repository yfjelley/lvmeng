# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0050_auto_20160330_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='calling_card',
            field=models.ImageField(upload_to=b'customer/calling_card/', null=True, verbose_name='\u540d\u7247', blank=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='company',
            field=models.CharField(max_length=30, null=True, verbose_name='\u6240\u5c5e\u516c\u53f8', blank=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=30, null=True, verbose_name='\u90ae\u7bb1', blank=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='risk_preference',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='\u5ba2\u6237\u98ce\u9669\u504f\u597d', choices=[(1, '1-\u975e\u5e38\u4fdd\u5b88'), (2, '2-\u4fdd\u5b88'), (3, '3-\u6bd4\u8f83\u4fdd\u5b88'), (4, '4-\u6bd4\u8f83\u6fc0\u8fdb'), (5, '5-\u6fc0\u8fdb'), (6, '6-\u975e\u5e38\u6fc0\u8fdb')]),
        ),
        migrations.AddField(
            model_name='customer_pending',
            name='calling_card',
            field=models.ImageField(upload_to=b'customer/calling_card/', null=True, verbose_name='\u540d\u7247', blank=True),
        ),
        migrations.AddField(
            model_name='customer_pending',
            name='company',
            field=models.CharField(max_length=30, null=True, verbose_name='\u6240\u5c5e\u516c\u53f8', blank=True),
        ),
        migrations.AddField(
            model_name='customer_pending',
            name='email',
            field=models.EmailField(max_length=30, null=True, verbose_name='\u90ae\u7bb1', blank=True),
        ),
        migrations.AddField(
            model_name='customer_pending',
            name='estimate_purchase_total',
            field=models.IntegerField(null=True, verbose_name='\u9884\u8ba1\u603b\u5171\u53ef\u8d2d\u4e70\u89c4\u6a21', blank=True),
        ),
        migrations.AddField(
            model_name='customer_pending',
            name='product_target',
            field=models.ManyToManyField(to='erp.Product', null=True, verbose_name='\u76ee\u6807\u8d2d\u4e70\u4ea7\u54c1', blank=True),
        ),
        migrations.AddField(
            model_name='customer_pending',
            name='risk_preference',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='\u5ba2\u6237\u98ce\u9669\u504f\u597d', choices=[(1, '1-\u975e\u5e38\u4fdd\u5b88'), (2, '2-\u4fdd\u5b88'), (3, '3-\u6bd4\u8f83\u4fdd\u5b88'), (4, '4-\u6bd4\u8f83\u6fc0\u8fdb'), (5, '5-\u6fc0\u8fdb'), (6, '6-\u975e\u5e38\u6fc0\u8fdb')]),
        ),
    ]
