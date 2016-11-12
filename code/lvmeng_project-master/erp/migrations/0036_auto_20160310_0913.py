# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0035_auto_20160309_1550'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='idCard_num',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='phoneNum',
        ),
        migrations.RemoveField(
            model_name='business',
            name='phoneNum',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='idCard_num',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='phoneNum',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='idCard_num',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='phoneNum',
        ),
    ]
