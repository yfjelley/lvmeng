# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0110_auto_20160523_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='business_qrcode',
            field=models.ImageField(upload_to=b'business/qrcode/', null=True, verbose_name='\u673a\u6784\u5fae\u4fe1\u516c\u4f17\u53f7(\u5c55\u793a\u5728\u5ba2\u6237\u7aef\u9996\u9875)', blank=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='logo',
            field=models.ImageField(upload_to=b'business/logo/', null=True, verbose_name='\u673a\u6784\u6807\u5fd7(\u5c3a\u5bf8\u5927\u5c0f:50*50,png\u683c\u5f0f)', blank=True),
        ),
    ]
