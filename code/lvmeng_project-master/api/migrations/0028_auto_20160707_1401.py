# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0027_comment_is_valid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkin',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='history_checkin',
            name='customer',
        ),
        migrations.AddField(
            model_name='checkin',
            name='user',
            field=models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237'),
        ),
        migrations.AddField(
            model_name='history_checkin',
            name='user',
            field=models.ForeignKey(verbose_name='\u7528\u6237', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='checkin',
            name='continuous_days',
            field=models.PositiveIntegerField(null=True, verbose_name='\u8fde\u7eed\u767b\u5f55\u5929\u6570', blank=True),
        ),
        migrations.AlterField(
            model_name='checkin',
            name='points',
            field=models.PositiveIntegerField(null=True, verbose_name='\u79ef\u5206', blank=True),
        ),
    ]
