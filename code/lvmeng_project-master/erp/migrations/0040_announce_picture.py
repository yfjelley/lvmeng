# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.exceptions


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0039_auto_20160310_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announce_picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('logo_1', models.ImageField(blank=True, upload_to=b'business/pictures/', null=True, verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe6\xa0\x87\xe5\xbf\x97\xe5\x9b\xbe\xe7\x89\x87_1', validators=[django.core.exceptions.ValidationError])),
                ('logo_2', models.ImageField(blank=True, upload_to=b'business/pictures/', null=True, verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe6\xa0\x87\xe5\xbf\x97\xe5\x9b\xbe\xe7\x89\x87_2', validators=[django.core.exceptions.ValidationError])),
                ('logo_3', models.ImageField(blank=True, upload_to=b'business/pictures/', null=True, verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe6\xa0\x87\xe5\xbf\x97\xe5\x9b\xbe\xe7\x89\x87_3', validators=[django.core.exceptions.ValidationError])),
                ('logo_4', models.ImageField(blank=True, upload_to=b'business/pictures/', null=True, verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe6\xa0\x87\xe5\xbf\x97\xe5\x9b\xbe\xe7\x89\x87_4', validators=[django.core.exceptions.ValidationError])),
                ('logo_5', models.ImageField(blank=True, upload_to=b'business/pictures/', null=True, verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe6\xa0\x87\xe5\xbf\x97\xe5\x9b\xbe\xe7\x89\x87_5', validators=[django.core.exceptions.ValidationError])),
                ('business', models.OneToOneField(verbose_name=b'\xe5\x85\xb3\xe8\x81\x94\xe6\x9c\xba\xe6\x9e\x84', to='erp.Business')),
            ],
        ),
    ]
