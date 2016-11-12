# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oa', '0028_auto_20160401_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_to_do',
            name='remark',
            field=models.TextField(max_length=300, null=True, verbose_name='\u5907\u6ce8', blank=True),
        ),
    ]
