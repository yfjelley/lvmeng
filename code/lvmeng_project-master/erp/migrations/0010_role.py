# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('erp', '0009_auto_20160223_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'\xe8\xa7\x92\xe8\x89\xb2\xe5\x90\x8d')),
                ('register_date', models.DateField(null=True, verbose_name=b'\xe6\xb3\xa8\xe5\x86\x8c\xe6\x97\xa5\xe6\x9c\x9f', blank=True)),
                ('entry_person', models.CharField(max_length=20, verbose_name=b'\xe5\xbd\x95\xe5\x85\xa5\xe4\xba\xba')),
                ('remark', models.TextField(max_length=300, null=True, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
                ('role', models.ManyToManyField(to='auth.Permission')),
            ],
        ),
    ]
