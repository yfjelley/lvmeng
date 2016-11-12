# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0068_auto_20160421_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='business',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='permissions',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='user',
        ),
        migrations.AddField(
            model_name='agent',
            name='role',
            field=models.CharField(max_length=30, null=True, verbose_name='\u89d2\u8272', blank=True),
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
