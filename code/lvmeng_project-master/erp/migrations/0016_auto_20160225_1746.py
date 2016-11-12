# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0015_auto_20160225_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='avatar',
            field=models.ImageField(upload_to=b'agent/avatar/', null=True, verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f\xe5\x9b\xbe\xe7\x89\x87', blank=True),
        ),
    ]
