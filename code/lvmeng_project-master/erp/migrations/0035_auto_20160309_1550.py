# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0034_auto_20160309_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='business',
            field=models.ForeignKey(verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe6\x9c\xba\xe6\x9e\x84', blank=True, to='erp.Business', null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='agents',
            field=models.ManyToManyField(to='erp.Agent', verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe7\x90\x86\xe8\xb4\xa2\xe5\xb8\x88'),
        ),
    ]
