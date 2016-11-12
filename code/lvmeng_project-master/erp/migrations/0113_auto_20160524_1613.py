# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0112_auto_20160524_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='return_expected',
            field=models.DecimalField(default=0, verbose_name='\u9884\u671f\u6536\u76ca(\u663e\u793a\u5728\u9996\u9875)', max_digits=6, decimal_places=4),
            preserve_default=False,
        ),
    ]
