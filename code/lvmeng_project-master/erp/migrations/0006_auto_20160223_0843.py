# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('erp', '0005_agent_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d')),
                ('phoneNum', models.CharField(max_length=18, verbose_name=b'\xe7\x94\xb5\xe8\xaf\x9d')),
                ('sex', models.CharField(default=1, max_length=2, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(b'1', b'\xe7\x94\xb7'), (b'2', b'\xe5\xa5\xb3')])),
                ('address', models.CharField(max_length=30, verbose_name=b'\xe5\x9c\xb0\xe5\x9d\x80')),
                ('register_date', models.DateTimeField(null=True, verbose_name=b'\xe6\xb3\xa8\xe5\x86\x8c\xe6\x97\xa5\xe6\x9c\x9f', blank=True)),
                ('entry_person', models.CharField(max_length=20, verbose_name=b'\xe5\xbd\x95\xe5\x85\xa5\xe4\xba\xba')),
                ('idCard_num', models.CharField(max_length=30, verbose_name=b'\xe8\xba\xab\xe4\xbb\xbd\xe8\xaf\x81\xe5\x8f\xb7')),
                ('remark', models.TextField(max_length=300, null=True, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
                ('user', models.OneToOneField(verbose_name=b'\xe5\x85\xb3\xe8\x81\x94\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-register_date'],
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='agents',
            field=models.ManyToManyField(to='erp.Agent', verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe7\x90\x86\xe8\xb4\xa2\xe5\xb8\x88'),
        ),
    ]
