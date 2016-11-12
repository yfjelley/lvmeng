# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0051_auto_20160330_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_pending',
            name='register_date',
            field=models.DateField(auto_now_add=True, verbose_name='\u6ce8\u518c\u65e5\u671f', null=True),
        ),
    ]
