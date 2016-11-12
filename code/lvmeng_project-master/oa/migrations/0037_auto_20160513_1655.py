# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('oa', '0036_auto_20160512_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_to_do',
            name='remark',
            field=tinymce.models.HTMLField(null=True, verbose_name='\u5907\u6ce8', blank=True),
        ),
        migrations.AlterField(
            model_name='internal_announcement',
            name='content',
            field=tinymce.models.HTMLField(null=True, verbose_name='\u901a\u77e5\u5185\u5bb9', blank=True),
        ),
    ]
