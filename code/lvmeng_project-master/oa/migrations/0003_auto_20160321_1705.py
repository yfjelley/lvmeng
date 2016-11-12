# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('erp', '0048_auto_20160316_1531'),
        ('oa', '0002_checkwork_check_business'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckWork_history',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('abscissa', models.CharField(max_length=30, verbose_name=b'\xe6\xa8\xaa\xe5\x9d\x90\xe6\xa0\x87')),
                ('ordinate', models.CharField(max_length=30, verbose_name=b'\xe7\xba\xb5\xe5\x9d\x90\xe6\xa0\x87')),
                ('check_time', models.DateTimeField(verbose_name=b'\xe8\x80\x83\xe5\x8b\xa4\xe6\x97\xb6\xe9\x97\xb4')),
                ('check_business_history', models.ForeignKey(verbose_name=b'\xe5\x85\xb3\xe8\x81\x94\xe6\x9c\xba\xe6\x9e\x84', to='erp.Business')),
                ('check_history', models.ForeignKey(verbose_name=b'\xe5\x85\xb3\xe8\x81\x94\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='checkwork',
            name='check_user',
            field=models.OneToOneField(verbose_name=b'\xe5\x85\xb3\xe8\x81\x94\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL),
        ),
    ]
