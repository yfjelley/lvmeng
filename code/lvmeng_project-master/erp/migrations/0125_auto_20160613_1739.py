# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0124_auto_20160608_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='business_phone',
            field=models.CharField(default=1, max_length=18, verbose_name='\u673a\u6784\u516c\u4f17\u7535\u8bdd(\u5c55\u793a\u5728\u5ba2\u6237\u7aef\u9996\u9875)'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='business',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='\u7ba1\u7406\u5458\u90ae\u7bb1(\u767b\u5f55\u7528\u6237\u540d)'),
        ),
        migrations.AlterField(
            model_name='business',
            name='work_address',
            field=models.CharField(default=1, max_length=18, verbose_name='\u673a\u6784\u529e\u516c\u5730\u5740(\u5c55\u793a\u5728\u5ba2\u6237\u7aef\u9996\u9875)'),
            preserve_default=False,
        ),
    ]
