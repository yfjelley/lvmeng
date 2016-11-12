# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0014_auto_20160225_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='business',
            field=models.ForeignKey(verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe6\x9c\xba\xe6\x9e\x84', blank=True, to='erp.Business', null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='address',
            field=models.CharField(max_length=30, verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe5\x9c\xb0\xe5\x9d\x80'),
        ),
    ]
