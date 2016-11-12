# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.exceptions


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0042_auto_20160311_1736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announce_picture',
            name='logo_1',
        ),
        migrations.RemoveField(
            model_name='announce_picture',
            name='logo_2',
        ),
        migrations.RemoveField(
            model_name='announce_picture',
            name='logo_3',
        ),
        migrations.RemoveField(
            model_name='announce_picture',
            name='logo_4',
        ),
        migrations.RemoveField(
            model_name='announce_picture',
            name='logo_5',
        ),
        migrations.AddField(
            model_name='announce_picture',
            name='picture_1',
            field=models.ImageField(blank=True, upload_to=b'business/pictures/', null=True, verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe5\x9b\xbe\xe7\x89\x87_1', validators=[django.core.exceptions.ValidationError]),
        ),
        migrations.AddField(
            model_name='announce_picture',
            name='picture_2',
            field=models.ImageField(blank=True, upload_to=b'business/pictures/', null=True, verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe5\x9b\xbe\xe7\x89\x87_2', validators=[django.core.exceptions.ValidationError]),
        ),
        migrations.AddField(
            model_name='announce_picture',
            name='picture_3',
            field=models.ImageField(blank=True, upload_to=b'business/pictures/', null=True, verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe5\x9b\xbe\xe7\x89\x87_3', validators=[django.core.exceptions.ValidationError]),
        ),
        migrations.AddField(
            model_name='announce_picture',
            name='picture_4',
            field=models.ImageField(blank=True, upload_to=b'business/pictures/', null=True, verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe5\x9b\xbe\xe7\x89\x87_4', validators=[django.core.exceptions.ValidationError]),
        ),
        migrations.AddField(
            model_name='announce_picture',
            name='picture_5',
            field=models.ImageField(blank=True, upload_to=b'business/pictures/', null=True, verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe5\x9b\xbe\xe7\x89\x87_5', validators=[django.core.exceptions.ValidationError]),
        ),
    ]
