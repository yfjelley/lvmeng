# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0065_customer_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='brief_introduction',
            field=models.CharField(max_length=15, null=True, verbose_name='\u516c\u53f8\u7b80\u4ecb(15\u4e2a\u5b57\u4ee5\u5185,\u663e\u793a\u5728APP\u9996\u9875)', blank=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='note',
            field=models.TextField(max_length=3000, null=True, verbose_name='\u516c\u53f8\u8be6\u60c5', blank=True),
        ),
    ]
