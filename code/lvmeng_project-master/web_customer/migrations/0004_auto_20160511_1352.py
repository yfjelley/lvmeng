# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('web_customer', '0003_auto_20160510_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lv_announcement',
            name='text',
            field=tinymce.models.HTMLField(null=True, verbose_name='\u5185\u5bb9\u8bf4\u660e', blank=True),
        ),
    ]
