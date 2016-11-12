# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0121_agent_wechat'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='qq_number',
            field=models.PositiveIntegerField(max_length=20, null=True, verbose_name='QQ\u53f7', blank=True),
        ),
    ]
