# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20160324_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='version',
            name='context',
            field=models.CharField(max_length=100, null=True, verbose_name=b'\xe7\x89\x88\xe6\x9c\xac\xe4\xbf\xa1\xe6\x81\xaf', blank=True),
        ),
    ]
