# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20160413_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headline',
            name='context',
            field=models.TextField(max_length=15000, null=True, verbose_name='\u5185\u5bb9', blank=True),
        ),
    ]
