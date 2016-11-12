# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0092_auto_20160429_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='idCard_num',
            field=models.CharField(max_length=30, null=True, verbose_name='\u8eab\u4efd\u8bc1\u53f7', blank=True),
        ),
    ]
