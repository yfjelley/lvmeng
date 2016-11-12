# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.exceptions


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0043_auto_20160314_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.ImageField(blank=True, upload_to=b'business/pictures/', null=True, verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe5\x9b\xbe\xe7\x89\x87', validators=[django.core.exceptions.ValidationError])),
                ('title', models.CharField(max_length=30, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('order', models.IntegerField(verbose_name=b'\xe9\xa1\xba\xe5\xba\x8f')),
                ('date', models.DateField(verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4')),
                ('show_text', models.BooleanField(default=True, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x98\xbe\xe7\xa4\xba\xe5\x86\x85\xe5\xae\xb9')),
                ('text', models.TextField(max_length=500, null=True, verbose_name=b'\xe5\x86\x85\xe5\xae\xb9\xe8\xaf\xb4\xe6\x98\x8e', blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='announce_picture',
            name='business',
        ),
        migrations.DeleteModel(
            name='Announce_picture',
        ),
    ]
