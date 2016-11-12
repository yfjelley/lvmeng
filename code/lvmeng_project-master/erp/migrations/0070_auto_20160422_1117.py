# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0069_auto_20160422_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='email',
            field=models.EmailField(default=3, max_length=254, verbose_name='\u90ae\u7bb1'),
            preserve_default=False,
        ),
    ]
