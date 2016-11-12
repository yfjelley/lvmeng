# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oa', '0032_auto_20160512_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkwork',
            name='address',
            field=models.CharField(max_length=30, null=True, verbose_name='\u5730\u5740', blank=True),
        ),
        migrations.AddField(
            model_name='checkwork',
            name='area',
            field=models.CharField(max_length=30, null=True, verbose_name='\u5730\u533a', blank=True),
        ),
    ]
