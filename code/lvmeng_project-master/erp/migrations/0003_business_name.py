# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0002_auto_20160205_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='name',
            field=models.CharField(max_length=50, verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
    ]
