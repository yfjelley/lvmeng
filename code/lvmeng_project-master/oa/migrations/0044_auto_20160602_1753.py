# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('oa', '0043_remove_checkwork_history_time_now'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_to_do',
            name='todo_user',
            field=models.ForeignKey(verbose_name='\u5f85\u529e\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
