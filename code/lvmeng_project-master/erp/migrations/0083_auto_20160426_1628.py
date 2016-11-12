# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0082_auto_20160426_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='job_type',
            field=models.CharField(default=2, choices=[(b'1', '\u517c\u804c'), (b'2', '\u5168\u804c')], max_length=2, blank=True, null=True, verbose_name='\u804c\u4f4d\u7c7b\u578b'),
        ),
    ]
