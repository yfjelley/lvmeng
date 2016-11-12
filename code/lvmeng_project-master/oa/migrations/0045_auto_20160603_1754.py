# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oa', '0044_auto_20160602_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_examine',
            name='examine_time',
            field=models.DateTimeField(null=True, verbose_name='\u5ba1\u6279\u65f6\u95f4', blank=True),
        ),
    ]
