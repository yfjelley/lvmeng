# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0104_auto_20160517_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='risk_preference',
            field=models.CharField(default=b'3', max_length=10, verbose_name='\u98ce\u9669\u504f\u597d', choices=[(b'1', '1-\u975e\u5e38\u4fdd\u5b88'), (b'2', '2-\u4fdd\u5b88'), (b'3', '3-\u6bd4\u8f83\u4fdd\u5b88'), (b'4', '4-\u6bd4\u8f83\u6fc0\u8fdb'), (b'5', '5-\u6fc0\u8fdb'), (b'6', '6-\u975e\u5e38\u6fc0\u8fdb')]),
        ),
    ]
