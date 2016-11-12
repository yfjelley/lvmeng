# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('push', '0002_jpushdevice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apnsdevice',
            name='registration_id',
            field=models.CharField(max_length=200, verbose_name='Registration ID'),
        ),
        migrations.AlterField(
            model_name='jpushdevice',
            name='registration_id',
            field=models.CharField(max_length=200, verbose_name='Registration ID'),
        ),
        migrations.AlterUniqueTogether(
            name='apnsdevice',
            unique_together=set([('registration_id', 'user')]),
        ),
        migrations.AlterUniqueTogether(
            name='jpushdevice',
            unique_together=set([('registration_id', 'user')]),
        ),
    ]
