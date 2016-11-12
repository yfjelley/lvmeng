# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0074_auto_20160425_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='position',
            field=models.ForeignKey(verbose_name='\u804c\u4f4d', blank=True, to='erp.Position', null=True),
        ),
    ]
