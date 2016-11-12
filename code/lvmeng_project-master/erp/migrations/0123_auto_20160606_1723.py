# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0122_agent_qq_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='qq_number',
            field=models.PositiveIntegerField(null=True, verbose_name='QQ\u53f7', blank=True),
        ),
    ]
