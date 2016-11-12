# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oa', '0019_auto_20160331_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='cost_examine',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='\u662f\u5426\u6709\u6548'),
        ),
    ]
