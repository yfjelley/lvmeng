# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0054_auto_20160411_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='product_target',
            field=models.ManyToManyField(to='erp.Product', null=True, verbose_name='\u76ee\u6807\u8d2d\u4e70\u4ea7\u54c1', blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='idCard_num',
            field=models.CharField(max_length=30, null=True, verbose_name='\u8eab\u4efd\u8bc1\u53f7', blank=True),
        ),
    ]
