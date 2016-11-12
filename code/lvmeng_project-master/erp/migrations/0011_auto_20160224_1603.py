# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('erp', '0010_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='role',
        ),
        migrations.AddField(
            model_name='role',
            name='permissions',
            field=models.ManyToManyField(to='auth.Permission', verbose_name=b'\xe8\xa7\x92\xe8\x89\xb2\xe6\x9d\x83\xe9\x99\x90'),
        ),
    ]
