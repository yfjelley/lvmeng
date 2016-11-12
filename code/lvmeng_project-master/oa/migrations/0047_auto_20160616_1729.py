# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oa', '0046_auto_20160616_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_work',
            name='work_type',
            field=models.CharField(default=b'1', choices=[(b'1', '\u65e5\u62a5'), (b'2', '\u5468\u62a5'), (b'3', '\u6708\u62a5')], max_length=5, blank=True, null=True, verbose_name='\u5de5\u4f5c\u6c47\u62a5\u7c7b\u578b'),
        ),
    ]
