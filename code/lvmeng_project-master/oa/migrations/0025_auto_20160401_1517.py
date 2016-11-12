# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oa', '0024_auto_20160401_1515'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='daily_to_do',
            options={'ordering': ['to_do_time']},
        ),
        migrations.AddField(
            model_name='daily_to_do',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='\u662f\u5426\u6709\u6548'),
        ),
    ]
