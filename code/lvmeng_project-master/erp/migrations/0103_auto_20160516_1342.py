# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0102_auto_20160516_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='return_expected',
            field=models.DecimalField(null=True, verbose_name='\u9884\u671f\u6536\u76ca(\u663e\u793a\u5728\u9996\u9875)', max_digits=6, decimal_places=4, blank=True),
        ),
    ]
