# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oa', '0037_auto_20160513_1655'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='daily_work',
            options={'ordering': ['-time']},
        ),
        migrations.RenameField(
            model_name='daily_work',
            old_name='daily_business',
            new_name='business',
        ),
        migrations.RenameField(
            model_name='daily_work',
            old_name='daily_time',
            new_name='time',
        ),
        migrations.RenameField(
            model_name='daily_work',
            old_name='daily_user',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='daily_work',
            name='summary',
        ),
        migrations.RemoveField(
            model_name='daily_work',
            name='tomorrow_plan',
        ),
        migrations.AddField(
            model_name='daily_work',
            name='content',
            field=models.CharField(default=1, max_length=300, verbose_name='\u660e\u65e5\u8ba1\u5212'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='daily_work',
            name='examine_user',
            field=models.ManyToManyField(related_name='daily_examine_user', null=True, verbose_name='\u5ba1\u6279\u4eba', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='daily_work',
            name='topic',
            field=models.CharField(default=1, max_length=300, verbose_name='\u5f53\u5929\u603b\u7ed3'),
            preserve_default=False,
        ),
    ]
