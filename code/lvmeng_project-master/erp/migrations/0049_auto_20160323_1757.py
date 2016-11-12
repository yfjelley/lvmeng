# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0048_auto_20160316_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='agent_num',
            field=models.CharField(unique=True, max_length=20, verbose_name=b'\xe7\x90\x86\xe8\xb4\xa2\xe5\xb8\x88\xe7\xbc\x96\xe5\x8f\xb7(\xe6\x9c\xba\xe6\x9e\x84\xe7\xbc\x96\xe5\x8f\xb7+\xe7\x90\x86\xe8\xb4\xa2\xe5\xb8\x88\xe7\xbc\x96\xe5\x8f\xb7\xe4\xb8\xba\xe9\x82\x80\xe8\xaf\xb7\xe7\xa0\x81)'),
        ),
    ]
