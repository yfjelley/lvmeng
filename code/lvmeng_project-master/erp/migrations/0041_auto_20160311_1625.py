# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0040_announce_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=30, null=True, verbose_name=b'\xe5\xae\xa2\xe6\x88\xb7\xe5\x9c\xb0\xe5\x9d\x80', blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='sex',
            field=models.CharField(default=1, choices=[(b'1', b'\xe7\x94\xb7'), (b'2', b'\xe5\xa5\xb3')], max_length=2, blank=True, null=True, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab'),
        ),
    ]
