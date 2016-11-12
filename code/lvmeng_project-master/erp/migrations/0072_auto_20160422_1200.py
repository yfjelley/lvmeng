# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0071_auto_20160422_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='bank_account',
            field=models.CharField(max_length=30, null=True, verbose_name='\u5f00\u6237\u94f6\u884c', blank=True),
        ),
        migrations.AddField(
            model_name='agent',
            name='graduated_school',
            field=models.CharField(max_length=30, null=True, verbose_name='\u6bd5\u4e1a\u9662\u6821', blank=True),
        ),
        migrations.AddField(
            model_name='agent',
            name='graduated_time',
            field=models.DateField(null=True, verbose_name='\u6bd5\u4e1a\u65f6\u95f4', blank=True),
        ),
        migrations.AddField(
            model_name='agent',
            name='job',
            field=models.CharField(max_length=30, null=True, verbose_name='\u804c\u4f4d', blank=True),
        ),
        migrations.AddField(
            model_name='agent',
            name='job_type',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='\u804c\u4f4d\u7c7b\u578b', choices=[(b'1', '\u517c\u804c'), (b'2', '\u5168\u804c')]),
        ),
        migrations.AddField(
            model_name='agent',
            name='major',
            field=models.CharField(max_length=20, null=True, verbose_name='\u4e13\u4e1a', blank=True),
        ),
        migrations.AddField(
            model_name='agent',
            name='salary_num',
            field=models.CharField(max_length=30, null=True, verbose_name='\u5de5\u8d44\u5361\u53f7', blank=True),
        ),
    ]
