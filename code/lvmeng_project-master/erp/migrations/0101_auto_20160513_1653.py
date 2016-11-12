# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0100_auto_20160513_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='text',
            field=tinymce.models.HTMLField(null=True, verbose_name='\u5185\u5bb9\u8bf4\u660e', blank=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='note',
            field=tinymce.models.HTMLField(null=True, verbose_name='\u516c\u53f8\u8be6\u60c5', blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='note',
            field=tinymce.models.HTMLField(null=True, verbose_name='\u5907\u6ce8', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='contract',
            field=models.FileField(upload_to=b'product/contract/', verbose_name='\u4ea7\u54c1\u5408\u540c(word\u6216\u8005pdf)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='invest_scope',
            field=tinymce.models.HTMLField(null=True, verbose_name='\u6295\u8d44\u8303\u56f4', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='strategy',
            field=tinymce.models.HTMLField(null=True, verbose_name='\u5b9e\u65bd\u7b56\u7565', blank=True),
        ),
    ]
