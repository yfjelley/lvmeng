# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oa', '0047_auto_20160616_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkwork',
            name='type',
            field=models.CharField(default=b'1', max_length=10, verbose_name='\u7b7e\u5230\u7c7b\u578b', choices=[(b'1', '\u7b7e\u5230'), (b'0', '\u7b7e\u9000')]),
        ),
        migrations.AddField(
            model_name='checkwork_history',
            name='type',
            field=models.CharField(default=b'1', max_length=10, verbose_name='\u7b7e\u5230\u7c7b\u578b', choices=[(b'1', '\u7b7e\u5230'), (b'0', '\u7b7e\u9000')]),
        ),
    ]
