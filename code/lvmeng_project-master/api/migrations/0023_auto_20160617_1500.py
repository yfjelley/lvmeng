# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_auto_20160531_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='headline',
            name='add_time',
            field=models.DateField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65e5\u671f', null=True),
        ),
        migrations.AlterField(
            model_name='headline',
            name='register_date',
            field=models.DateTimeField(null=True, verbose_name='\u65f6\u95f4', blank=True),
        ),
    ]
