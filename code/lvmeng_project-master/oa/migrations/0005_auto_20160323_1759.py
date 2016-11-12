# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0049_auto_20160323_1757'),
        ('oa', '0004_announcementemployee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Internal_announcement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic', models.CharField(max_length=30, verbose_name=b'\xe4\xb8\xbb\xe9\xa2\x98')),
                ('content', models.TextField(max_length=300, verbose_name=b'\xe9\x80\x9a\xe7\x9f\xa5\xe5\x86\x85\xe5\xae\xb9')),
                ('on_top', models.CharField(default=b'1', max_length=1, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe7\xbd\xae\xe9\xa1\xb6', choices=[(b'1', b'\xe5\x90\xa6'), (b'2', b'\xe6\x98\xaf')])),
                ('onTop_start', models.DateField(null=True, verbose_name=b'\xe7\xbd\xae\xe9\xa1\xb6\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('onTop_end', models.DateField(null=True, verbose_name=b'\xe7\xbd\xae\xe9\xa1\xb6\xe7\xbb\x93\xe6\x9d\x9f\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('publish', models.CharField(default=b'1', max_length=1, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x8f\x91\xe5\xb8\x83', choices=[(b'1', b'\xe4\xb8\x8d\xe5\x8f\x91\xe5\xb8\x83'), (b'2', b'\xe5\x8f\x91\xe5\xb8\x83')])),
                ('publish_start', models.DateField(null=True, verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('publish_end', models.DateField(null=True, verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe7\xbb\x93\xe6\x9d\x9f\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('add_time', models.DateField(auto_now_add=True, verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4')),
                ('announcement_business', models.ForeignKey(verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe6\x9c\xba\xe6\x9e\x84', to='erp.Business')),
            ],
        ),
        migrations.RemoveField(
            model_name='announcementemployee',
            name='announcement_business',
        ),
        migrations.DeleteModel(
            name='AnnouncementEmployee',
        ),
    ]
