# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0111_auto_20160523_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='logo',
            field=models.ImageField(upload_to=b'business/logo/', null=True, verbose_name='\u673a\u6784logo(\u5c3a\u5bf8\u5927\u5c0f:50*50,png\u683c\u5f0f)', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='begin_date',
            field=models.DateField(null=True, verbose_name='\u52df\u96c6\u671f\u9650\u5f00\u59cb\u65e5\u671f', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='end_date',
            field=models.DateField(null=True, verbose_name='\u52df\u96c6\u671f\u9650\u7ed3\u675f\u65e5\u671f', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='period',
            field=models.IntegerField(verbose_name='\u4ea7\u54c1\u671f\u9650/\u6708(\u663e\u793a\u5728\u9996\u9875)'),
        ),
    ]
