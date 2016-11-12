# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0119_position_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='manager',
            field=models.CharField(max_length=30, verbose_name='\u4ea7\u54c1\u7ba1\u7406\u4eba'),
        ),
    ]
