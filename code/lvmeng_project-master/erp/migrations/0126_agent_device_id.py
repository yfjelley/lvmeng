# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0125_auto_20160613_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='device_id',
            field=models.CharField(max_length=200, null=True, verbose_name='DEVICE_ID', blank=True),
        ),
    ]
