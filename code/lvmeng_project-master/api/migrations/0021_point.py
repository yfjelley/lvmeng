# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_auto_20160525_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=10, verbose_name='\u79ef\u5206\u7c7b\u578b', choices=[(b'0', '\u624b\u673a\u8ba4\u8bc1'), (b'1', '\u5b9e\u540d\u8ba4\u8bc1'), (b'2', '\u90ae\u7bb1\u8ba4\u8bc1')])),
                ('points', models.IntegerField(verbose_name='\u79ef\u5206')),
            ],
        ),
    ]
