# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0091_auto_20160429_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(default=3, verbose_name='\u4ea7\u54c1\u7c7b\u578b(\u663e\u793a\u5728\u9996\u9875)', to='erp.Product_Type'),
        ),
    ]
