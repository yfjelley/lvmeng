# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('oa', '0040_auto_20160517_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_examine',
            name='examine_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 27, 16, 1, 6, 174000), verbose_name='\u5ba1\u6279\u65f6\u95f4', auto_now_add=True),
            preserve_default=False,
        ),
    ]
