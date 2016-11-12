# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_auto_20160707_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='max_points',
            field=models.IntegerField(null=True, verbose_name='\u5c01\u9876\u79ef\u5206', blank=True),
        ),
        migrations.AlterField(
            model_name='point',
            name='type',
            field=models.CharField(unique=True, max_length=10, verbose_name='\u79ef\u5206\u7c7b\u578b', choices=[(b'0', '\u624b\u673a\u8ba4\u8bc1'), (b'1', '\u5b9e\u540d\u8ba4\u8bc1'), (b'2', '\u90ae\u7bb1\u8ba4\u8bc1'), (b'3', '\u6bcf\u65e5\u7b7e\u5230'), (b'4', '\u8fde\u7eed7\u5929\u7b7e\u5230'), (b'5', '\u65b0\u589e\u5ba2\u6237'), (b'6', '\u5206\u4eab\u8f6c\u53d1'), (b'7', 'OA\u5904\u7406'), (b'8', '\u65b0\u589e\u4ea7\u54c1')]),
        ),
    ]
