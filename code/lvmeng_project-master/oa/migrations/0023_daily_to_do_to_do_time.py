# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oa', '0022_daily_to_do'),
    ]

    operations = [
        migrations.AddField(
            model_name='daily_to_do',
            name='to_do_time',
            field=models.DateTimeField(null=True, verbose_name='\u5f85\u529e\u4e8b\u65f6\u95f4', blank=True),
        ),
    ]
