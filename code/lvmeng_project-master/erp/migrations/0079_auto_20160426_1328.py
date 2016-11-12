# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0078_auto_20160426_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='register_date',
            field=models.DateField(default=datetime.datetime(2016, 4, 26, 13, 28, 43, 487000), verbose_name='\u6ce8\u518c\u65e5\u671f', auto_now_add=True),
            preserve_default=False,
        ),
    ]
