# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0025_auto_20160302_1348'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('register_date', models.DateTimeField(null=True, verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xa5\xe6\x9c\x9f', blank=True)),
                ('announcement', models.CharField(default=b'', max_length=30, verbose_name=b'\xe5\x85\xac\xe5\x91\x8a')),
                ('url', models.URLField(verbose_name=b'\xe5\x85\xac\xe5\x91\x8a\xe9\x93\xbe\xe6\x8e\xa5')),
                ('business', models.ForeignKey(verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe6\x9c\xba\xe6\x9e\x84', blank=True, to='erp.Business', null=True)),
            ],
            options={
                'ordering': ['-register_date'],
            },
        ),
        migrations.CreateModel(
            name='Headline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('register_date', models.DateTimeField(null=True, verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f', blank=True)),
                ('title', models.CharField(default=b'', max_length=30, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('context', models.TextField(max_length=300, null=True, verbose_name=b'\xe5\x86\x85\xe5\xae\xb9', blank=True)),
                ('url', models.URLField(verbose_name=b'\xe8\xaf\xa6\xe6\x83\x85\xe9\x93\xbe\xe6\x8e\xa5')),
            ],
            options={
                'ordering': ['-register_date'],
            },
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('register_date', models.DateField(null=True, verbose_name=b'\xe7\xad\xbe\xe5\x88\xb0\xe6\x97\xa5\xe6\x9c\x9f', blank=True)),
                ('customer', models.ForeignKey(verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7', blank=True, to='erp.Customer', null=True)),
            ],
            options={
                'ordering': ['-register_date'],
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.CharField(max_length=10, verbose_name=b'\xe7\x89\x88\xe6\x9c\xac\xe5\x8f\xb7')),
                ('url', models.URLField(verbose_name=b'\xe4\xb8\x8b\xe8\xbd\xbd\xe9\x93\xbe\xe6\x8e\xa5')),
                ('date', models.DateTimeField(null=True, verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xa5\xe6\x9c\x9f', blank=True)),
            ],
        ),
    ]
