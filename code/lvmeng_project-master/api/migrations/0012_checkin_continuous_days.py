# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20160415_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkin',
            name='continuous_days',
            field=models.IntegerField(null=True, verbose_name='\u8fde\u7eed\u767b\u5f55\u5929\u6570', blank=True),
        ),
    ]
