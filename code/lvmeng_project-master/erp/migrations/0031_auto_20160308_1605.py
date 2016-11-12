# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('erp', '0030_auto_20160308_1453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='business',
        ),
        migrations.RemoveField(
            model_name='role',
            name='permissions',
        ),
        migrations.AddField(
            model_name='agent',
            name='permissions',
            field=models.ManyToManyField(to='auth.Permission', verbose_name=b'\xe8\xa7\x92\xe8\x89\xb2\xe6\x9d\x83\xe9\x99\x90'),
        ),
        migrations.AddField(
            model_name='employee',
            name='permissions',
            field=models.ManyToManyField(to='auth.Permission', verbose_name=b'\xe8\xa7\x92\xe8\x89\xb2\xe6\x9d\x83\xe9\x99\x90'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='role',
            field=models.CharField(max_length=30, verbose_name=b'\xe8\xa7\x92\xe8\x89\xb2'),
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]
