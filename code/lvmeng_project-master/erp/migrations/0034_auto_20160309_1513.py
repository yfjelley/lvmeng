# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0033_auto_20160309_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='agents',
            field=models.ManyToManyField(related_name='Customer_Agent', verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe7\x90\x86\xe8\xb4\xa2\xe5\xb8\x88', to='erp.Agent'),
        ),
    ]
