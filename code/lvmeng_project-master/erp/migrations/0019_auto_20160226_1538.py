# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0018_auto_20160226_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='register_date',
            field=models.DateField(null=True, verbose_name=b'\xe6\xb3\xa8\xe5\x86\x8c\xe6\x97\xa5\xe6\x9c\x9f', blank=True),
        ),
    ]
