# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20160302_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='ValidSecond',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seconds', models.IntegerField(null=True, verbose_name=b'\xe9\xaa\x8c\xe8\xaf\x81\xe7\xa0\x81\xe6\x9c\x89\xe6\x95\x88\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='VerificationCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phoneNum', models.CharField(max_length=18, verbose_name=b'\xe7\x94\xb5\xe8\xaf\x9d')),
                ('code', models.CharField(max_length=18, verbose_name=b'\xe9\xaa\x8c\xe8\xaf\x81\xe7\xa0\x81')),
                ('register_date', models.DateTimeField(verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xa5\xe6\x9c\x9f')),
            ],
            options={
                'ordering': ['-register_date'],
            },
        ),
    ]
