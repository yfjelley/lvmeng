# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0107_announcement_read_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='business_email',
            field=models.EmailField(max_length=254, null=True, verbose_name='\u673a\u6784\u90ae\u7bb1(\u5c55\u793a\u5728\u5ba2\u6237\u7aef\u9996\u9875)', blank=True),
        ),
        migrations.AddField(
            model_name='business',
            name='business_phone',
            field=models.CharField(max_length=18, null=True, verbose_name='\u673a\u6784\u516c\u4f17\u7535\u8bdd(\u5c55\u793a\u5728\u5ba2\u6237\u7aef\u9996\u9875)', blank=True),
        ),
        migrations.AddField(
            model_name='business',
            name='business_qrcode',
            field=models.ImageField(upload_to=b'business/qrcode/', null=True, verbose_name='\u673a\u6784\u4e8c\u7ef4\u7801(\u5c55\u793a\u5728\u5ba2\u6237\u7aef\u9996\u9875)', blank=True),
        ),
        migrations.AddField(
            model_name='business',
            name='work_address',
            field=models.CharField(max_length=18, null=True, verbose_name='\u673a\u6784\u529e\u516c\u5730\u5740(\u5c55\u793a\u5728\u5ba2\u6237\u7aef\u9996\u9875)', blank=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='\u4e2a\u4eba\u90ae\u7bb1'),
        ),
    ]
