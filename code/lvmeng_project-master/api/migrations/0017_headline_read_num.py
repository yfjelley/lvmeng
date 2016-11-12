# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20160517_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='headline',
            name='read_num',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name='\u9605\u8bfb\u6b21\u6570', blank=True),
        ),
    ]
