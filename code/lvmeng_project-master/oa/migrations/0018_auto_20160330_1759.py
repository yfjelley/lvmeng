# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oa', '0017_auto_20160330_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cost_application',
            name='read_status',
            field=models.CharField(default=b'1', max_length=1, verbose_name='\u8bfb\u53d6\u72b6\u6001', choices=[(b'1', '\u672a\u8bfb'), (b'2', '\u5df2\u8bfb')]),
        ),
        migrations.AlterField(
            model_name='leave_management',
            name='read_status',
            field=models.CharField(default=b'1', max_length=1, verbose_name='\u8bfb\u53d6\u72b6\u6001', choices=[(b'1', '\u672a\u8bfb'), (b'2', '\u5df2\u8bfb')]),
        ),
        migrations.AlterField(
            model_name='travel_apply',
            name='read_status',
            field=models.CharField(default=b'1', max_length=1, verbose_name='\u8bfb\u53d6\u72b6\u6001', choices=[(b'1', '\u672a\u8bfb'), (b'2', '\u5df2\u8bfb')]),
        ),
    ]
