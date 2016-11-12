# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('oa', '0039_auto_20160516_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cost_application',
            name='user',
            field=models.ForeignKey(verbose_name='\u7533\u8bf7\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='daily_work',
            name='user',
            field=models.ForeignKey(verbose_name='\u586b\u62a5\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='leave_management',
            name='user',
            field=models.ForeignKey(verbose_name='\u8bf7\u5047\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='travel_apply',
            name='user',
            field=models.ForeignKey(verbose_name='\u7533\u8bf7\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
