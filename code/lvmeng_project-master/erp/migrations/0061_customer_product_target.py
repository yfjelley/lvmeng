# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0060_auto_20160411_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='product_target',
            field=models.ManyToManyField(to='erp.Product', null=True, verbose_name='\u76ee\u6807\u8d2d\u4e70\u4ea7\u54c1', blank=True),
        ),
    ]
