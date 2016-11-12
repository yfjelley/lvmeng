# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0117_auto_20160526_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='note',
            field=models.TextField(max_length=300, null=True, verbose_name='\u5907\u6ce8', blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='note',
            field=models.TextField(max_length=300, null=True, verbose_name='\u5907\u6ce8', blank=True),
        ),
    ]
