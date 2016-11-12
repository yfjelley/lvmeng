# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agent_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent_Version',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.CharField(max_length=10, verbose_name='\u7248\u672c\u53f7')),
                ('url', models.URLField(verbose_name='\u4e0b\u8f7d\u94fe\u63a5')),
                ('context', models.CharField(max_length=100, null=True, verbose_name='\u7248\u672c\u4fe1\u606f', blank=True)),
                ('date', models.DateTimeField(null=True, verbose_name='\u6dfb\u52a0\u65e5\u671f', blank=True)),
            ],
        ),
    ]
