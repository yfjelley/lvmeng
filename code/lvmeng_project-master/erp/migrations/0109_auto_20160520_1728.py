# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0108_auto_20160520_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='phoneNum',
            field=models.CharField(max_length=18, verbose_name='\u7535\u8bdd(\u767b\u5f55\u7528\u6237\u540d)'),
        ),
        migrations.AlterField(
            model_name='business',
            name='business_email',
            field=models.EmailField(max_length=254, null=True, verbose_name='\u673a\u6784\u5bf9\u5916\u90ae\u7bb1(\u5c55\u793a\u5728\u5ba2\u6237\u7aef\u9996\u9875)', blank=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='\u4e2a\u4eba\u90ae\u7bb1(\u767b\u5f55\u7528\u6237\u540d)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='contract',
            field=models.FileField(upload_to=b'product/contract/', null=True, verbose_name='\u4ea7\u54c1\u5408\u540c(word\u6216\u8005pdf)', blank=True),
        ),
    ]
