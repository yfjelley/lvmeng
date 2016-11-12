# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0052_auto_20160331_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='email',
            field=models.EmailField(max_length=30, null=True, verbose_name='\u90ae\u7bb1', blank=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=30, null=True, verbose_name='\u90ae\u7bb1', blank=True),
        ),
    ]
