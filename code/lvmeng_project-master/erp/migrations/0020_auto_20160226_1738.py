# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0019_auto_20160226_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='agent_num',
            field=models.CharField(default=1, max_length=20, verbose_name=b'\xe7\x90\x86\xe8\xb4\xa2\xe5\xb8\x88\xe7\xbc\x96\xe5\x8f\xb7'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='business',
            name='business_num',
            field=models.CharField(default=1, max_length=20, verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe7\xbc\x96\xe5\x8f\xb7'),
            preserve_default=False,
        ),
    ]
