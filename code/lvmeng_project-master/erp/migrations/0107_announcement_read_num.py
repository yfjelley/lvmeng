# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0106_auto_20160519_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='read_num',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name='\u9605\u8bfb\u6b21\u6570', blank=True),
        ),
    ]
