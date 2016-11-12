# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oa', '0021_leave_examine_travel_examine'),
    ]

    operations = [
        migrations.CreateModel(
            name='daily_to_do',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic', models.CharField(max_length=30, verbose_name='\u4e3b\u9898')),
                ('content', models.CharField(max_length=100, verbose_name='\u4e8b\u4ef6')),
                ('remark', models.CharField(max_length=100, null=True, verbose_name='\u5907\u6ce8', blank=True)),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('todo_user', models.ForeignKey(verbose_name='\u4ee3\u529e\u4eba', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-add_time'],
            },
        ),
    ]
