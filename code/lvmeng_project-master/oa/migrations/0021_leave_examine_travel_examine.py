# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0049_auto_20160323_1757'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oa', '0020_cost_examine_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave_examine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('examine_status', models.CharField(default=b'3', max_length=1, verbose_name='\u5ba1\u6838\u7ed3\u679c\u9009\u62e9', choices=[(b'1', '\u901a\u8fc7'), (b'2', '\u9a73\u56de'), (b'3', '\u5f85\u5ba1\u6838')])),
                ('read_status', models.CharField(default=b'1', max_length=1, verbose_name='\u8bfb\u53d6\u72b6\u6001', choices=[(b'1', '\u672a\u8bfb'), (b'2', '\u5df2\u8bfb')])),
                ('examine_message', models.TextField(null=True, verbose_name='\u5ba1\u6279\u5907\u6ce8', blank=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='\u662f\u5426\u6709\u6548')),
                ('examine_time', models.DateTimeField(null=True, verbose_name='\u5ba1\u6279\u65f6\u95f4', blank=True)),
                ('examine_business', models.ForeignKey(verbose_name='\u5173\u8054\u673a\u6784', blank=True, to='erp.Business', null=True)),
                ('examine_user', models.ForeignKey(verbose_name='\u5ba1\u6279\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('leave_examine', models.ForeignKey(verbose_name='\u5173\u8054\u8bf7\u5047\u7ba1\u7406\u7533\u8bf7', to='oa.Leave_management')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Travel_examine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('examine_status', models.CharField(default=b'3', max_length=1, verbose_name='\u5ba1\u6838\u7ed3\u679c\u9009\u62e9', choices=[(b'1', '\u901a\u8fc7'), (b'2', '\u9a73\u56de'), (b'3', '\u5f85\u5ba1\u6838')])),
                ('read_status', models.CharField(default=b'1', max_length=1, verbose_name='\u8bfb\u53d6\u72b6\u6001', choices=[(b'1', '\u672a\u8bfb'), (b'2', '\u5df2\u8bfb')])),
                ('examine_message', models.TextField(null=True, verbose_name='\u5ba1\u6279\u5907\u6ce8', blank=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='\u662f\u5426\u6709\u6548')),
                ('examine_time', models.DateTimeField(null=True, verbose_name='\u5ba1\u6279\u65f6\u95f4', blank=True)),
                ('examine_business', models.ForeignKey(verbose_name='\u5173\u8054\u673a\u6784', blank=True, to='erp.Business', null=True)),
                ('examine_user', models.ForeignKey(verbose_name='\u5ba1\u6279\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('travel_examine', models.ForeignKey(verbose_name='\u5173\u8054\u51fa\u5dee\u7533\u8bf7', to='oa.Travel_apply')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
