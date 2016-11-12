# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0029_auto_20160304_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='brief_introduction',
            field=models.CharField(max_length=300, null=True, verbose_name=b'\xe7\xae\x80\xe4\xbb\x8b', blank=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='note',
            field=models.TextField(max_length=300, null=True, verbose_name=b'\xe8\xaf\xa6\xe6\x83\x85', blank=True),
        ),
    ]
