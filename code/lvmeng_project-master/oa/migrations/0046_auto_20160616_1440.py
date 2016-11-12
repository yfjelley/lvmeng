# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oa', '0045_auto_20160603_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cost_application',
            name='cost',
            field=models.BigIntegerField(verbose_name='\u91d1\u989d(\u5143)'),
        ),
        migrations.AlterField(
            model_name='travel_apply',
            name='cost',
            field=models.BigIntegerField(verbose_name='\u91d1\u989d(\u5143)'),
        ),
    ]
