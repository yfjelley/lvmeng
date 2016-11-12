# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0028_auto_20160303_1711'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='purchase',
            options={'ordering': ['-register_time']},
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='buy_time',
        ),
        migrations.AddField(
            model_name='purchase',
            name='register_time',
            field=models.DateTimeField(null=True, verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4', blank=True),
        ),
    ]
