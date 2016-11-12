# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_validsecond_verificationcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='verificationcode',
            name='purpose',
            field=models.CharField(max_length=18, null=True, verbose_name=b'\xe7\x94\xa8\xe9\x80\x94', blank=True),
        ),
    ]
