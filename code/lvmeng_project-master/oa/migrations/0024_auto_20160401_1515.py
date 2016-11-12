# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('oa', '0023_daily_to_do_to_do_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='daily_to_do',
            options={'ordering': ['-to_do_time']},
        ),
        migrations.AlterField(
            model_name='daily_to_do',
            name='to_do_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 1, 15, 15, 53, 811000), verbose_name='\u5f85\u529e\u4e8b\u65f6\u95f4'),
            preserve_default=False,
        ),
    ]
