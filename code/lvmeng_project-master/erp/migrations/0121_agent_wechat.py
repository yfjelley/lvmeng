# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0120_auto_20160531_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='wechat',
            field=models.CharField(max_length=20, null=True, verbose_name='\u5fae\u4fe1\u53f7', blank=True),
        ),
    ]
