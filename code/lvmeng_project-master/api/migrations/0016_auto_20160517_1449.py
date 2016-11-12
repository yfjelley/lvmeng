# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20160427_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headline',
            name='context',
            field=tinymce.models.HTMLField(null=True, verbose_name='\u5185\u5bb9', blank=True),
        ),
    ]
