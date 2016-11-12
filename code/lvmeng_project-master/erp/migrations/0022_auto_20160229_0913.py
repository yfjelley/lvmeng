# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0021_auto_20160226_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='agent_num',
            field=models.CharField(unique=True, max_length=20, verbose_name=b'\xe7\x90\x86\xe8\xb4\xa2\xe5\xb8\x88\xe7\xbc\x96\xe5\x8f\xb7'),
        ),
    ]
