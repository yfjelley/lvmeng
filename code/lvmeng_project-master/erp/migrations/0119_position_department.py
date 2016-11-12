# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0118_auto_20160527_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='department',
            field=models.CharField(default=1, max_length=20, verbose_name='\u90e8\u95e8'),
            preserve_default=False,
        ),
    ]
