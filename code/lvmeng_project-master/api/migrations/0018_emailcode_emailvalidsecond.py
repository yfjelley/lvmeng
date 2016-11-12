# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_headline_read_num'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=100, verbose_name='\u90ae\u7bb1')),
                ('code', models.CharField(max_length=18, verbose_name='\u9a8c\u8bc1\u7801')),
                ('register_date', models.DateTimeField(verbose_name='\u6dfb\u52a0\u65e5\u671f')),
            ],
            options={
                'ordering': ['-register_date'],
            },
        ),
        migrations.CreateModel(
            name='EmailValidSecond',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seconds', models.IntegerField(null=True, verbose_name='\u9a8c\u8bc1\u7801\u6709\u6548\u65f6\u95f4', blank=True)),
            ],
        ),
    ]
