# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0087_agent_qrcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='entry_person',
            field=models.CharField(max_length=20, verbose_name='\u5f55\u5165\u5458'),
        ),
        migrations.AlterField(
            model_name='business',
            name='entry_person',
            field=models.CharField(max_length=20, verbose_name='\u5f55\u5165\u5458'),
        ),
        migrations.AlterField(
            model_name='position',
            name='entry_person',
            field=models.CharField(max_length=20, verbose_name='\u5f55\u5165\u5458'),
        ),
        migrations.AlterField(
            model_name='product',
            name='manager',
            field=models.CharField(max_length=30, verbose_name='\u4ea7\u54c1\u7ba1\u7406\u5458'),
        ),
    ]
