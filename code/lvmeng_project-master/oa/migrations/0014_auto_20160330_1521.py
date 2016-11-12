# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oa', '0013_auto_20160330_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='cost_application',
            name='read_status',
            field=models.CharField(max_length=10, null=True, verbose_name='\u8bfb\u53d6\u72b6\u6001', blank=True),
        ),
        migrations.AddField(
            model_name='cost_examine',
            name='read_status',
            field=models.CharField(default=b'1', max_length=1, verbose_name='\u8bfb\u53d6\u72b6\u6001', choices=[(b'1', '\u672a\u8bfb'), (b'2', '\u5df2\u8bfb')]),
        ),
        migrations.AddField(
            model_name='leave_management',
            name='read_status',
            field=models.CharField(max_length=10, null=True, verbose_name='\u8bfb\u53d6\u72b6\u6001', blank=True),
        ),
        migrations.AddField(
            model_name='travel_apply',
            name='read_status',
            field=models.CharField(max_length=10, null=True, verbose_name='\u8bfb\u53d6\u72b6\u6001', blank=True),
        ),
        migrations.AlterField(
            model_name='cost_examine',
            name='examine_status',
            field=models.CharField(default=b'3', max_length=1, verbose_name='\u5ba1\u6838\u7ed3\u679c\u9009\u62e9', choices=[(b'1', '\u901a\u8fc7'), (b'2', '\u9a73\u56de'), (b'3', '\u5f85\u5ba1\u6838')]),
        ),
        migrations.AlterField(
            model_name='cost_examine',
            name='examine_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u5ba1\u6279\u65f6\u95f4', null=True),
        ),
    ]
