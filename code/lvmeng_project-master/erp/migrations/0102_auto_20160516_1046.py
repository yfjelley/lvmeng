# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0101_auto_20160513_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='note',
            field=tinymce.models.HTMLField(max_length=300, null=True, verbose_name='\u5907\u6ce8', blank=True),
        ),
    ]
