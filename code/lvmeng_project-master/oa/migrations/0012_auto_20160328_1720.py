# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oa', '0011_read_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='read_message',
            name='record_id',
            field=models.IntegerField(null=True, verbose_name='\u5173\u8054\u8bb0\u5f55\u7684ID', blank=True),
        ),
    ]
