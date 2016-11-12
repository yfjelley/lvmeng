# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0016_auto_20160225_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='entry_person',
            field=models.CharField(default=1, max_length=20, verbose_name=b'\xe5\xbd\x95\xe5\x85\xa5\xe4\xba\xba'),
            preserve_default=False,
        ),
    ]
