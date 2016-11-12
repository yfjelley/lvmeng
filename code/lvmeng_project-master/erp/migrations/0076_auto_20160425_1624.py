# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0075_agent_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='permissions',
            field=models.ManyToManyField(to='auth.Permission', null=True, verbose_name='\u804c\u4f4d\u6743\u9650', blank=True),
        ),
    ]
