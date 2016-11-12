# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0025_auto_20160302_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='manager',
            field=models.CharField(max_length=30, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe7\xae\xa1\xe7\x90\x86\xe4\xba\xba'),
        ),
    ]
