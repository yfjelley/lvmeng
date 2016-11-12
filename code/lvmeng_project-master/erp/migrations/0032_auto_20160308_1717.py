# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0031_auto_20160308_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='permissions',
            field=models.ManyToManyField(to='auth.Permission', null=True, verbose_name=b'\xe8\xa7\x92\xe8\x89\xb2\xe6\x9d\x83\xe9\x99\x90', blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='permissions',
            field=models.ManyToManyField(to='auth.Permission', null=True, verbose_name=b'\xe8\xa7\x92\xe8\x89\xb2\xe6\x9d\x83\xe9\x99\x90', blank=True),
        ),
    ]
