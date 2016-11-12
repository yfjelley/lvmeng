# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0025_auto_20160302_1348'),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('register_date', models.DateField(null=True, verbose_name=b'\xe7\xad\xbe\xe5\x88\xb0\xe6\x97\xa5\xe6\x9c\x9f', blank=True)),
                ('customer', models.ForeignKey(verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7', blank=True, to='erp.Customer', null=True)),
            ],
            options={
                'ordering': ['-register_date'],
            },
        ),
        migrations.RemoveField(
            model_name='register',
            name='customer',
        ),
        migrations.DeleteModel(
            name='Register',
        ),
    ]
