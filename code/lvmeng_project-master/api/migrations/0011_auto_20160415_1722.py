# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20160415_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headline',
            name='register_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u65e5\u671f', null=True),
        ),
        migrations.AlterField(
            model_name='headline',
            name='url',
            field=models.URLField(null=True, verbose_name='\u8be6\u60c5\u94fe\u63a5', blank=True),
        ),
    ]
