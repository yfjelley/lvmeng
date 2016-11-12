# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0123_auto_20160606_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='first_pinyin',
            field=models.CharField(max_length=30, null=True, verbose_name='\u59d3\u540d\u62fc\u97f3\u9996\u5b57\u6bcd', blank=True),
        ),
        migrations.AddField(
            model_name='agent',
            name='pinyin',
            field=models.CharField(max_length=30, null=True, verbose_name='\u59d3\u540d\u62fc\u97f3', blank=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='first_pinyin',
            field=models.CharField(max_length=30, null=True, verbose_name='\u59d3\u540d\u62fc\u97f3\u9996\u5b57\u6bcd', blank=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='pinyin',
            field=models.CharField(max_length=30, null=True, verbose_name='\u59d3\u540d\u62fc\u97f3', blank=True),
        ),
    ]
