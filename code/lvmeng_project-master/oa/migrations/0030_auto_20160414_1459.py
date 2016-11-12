# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oa', '0029_auto_20160407_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cost_application',
            name='cost',
            field=models.BigIntegerField(verbose_name='\u91d1\u989d'),
        ),
        migrations.AlterField(
            model_name='travel_apply',
            name='travel_cost',
            field=models.BigIntegerField(verbose_name='\u91d1\u989d'),
        ),
    ]
