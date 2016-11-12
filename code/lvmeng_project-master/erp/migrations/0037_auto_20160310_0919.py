# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0036_auto_20160310_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='idCard_num',
            field=models.CharField(default=1, max_length=30, verbose_name=b'\xe8\xba\xab\xe4\xbb\xbd\xe8\xaf\x81\xe5\x8f\xb7'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='phoneNum',
            field=models.CharField(default=1, max_length=18, verbose_name=b'\xe7\x94\xb5\xe8\xaf\x9d'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='business',
            name='phoneNum',
            field=models.CharField(default=1, max_length=18, verbose_name=b'\xe7\x94\xb5\xe8\xaf\x9d'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='idCard_num',
            field=models.CharField(default=1, max_length=30, verbose_name=b'\xe8\xba\xab\xe4\xbb\xbd\xe8\xaf\x81\xe5\x8f\xb7'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='phoneNum',
            field=models.CharField(default=1, max_length=18, verbose_name=b'\xe7\x94\xb5\xe8\xaf\x9d'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='idCard_num',
            field=models.CharField(default=1, max_length=30, verbose_name=b'\xe8\xba\xab\xe4\xbb\xbd\xe8\xaf\x81\xe5\x8f\xb7'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='phoneNum',
            field=models.CharField(default=1, max_length=18, verbose_name=b'\xe7\x94\xb5\xe8\xaf\x9d(\xe4\xbd\x9c\xe4\xb8\xba\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d)'),
            preserve_default=False,
        ),
    ]
