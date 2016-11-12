# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('erp', '0128_auto_20160617_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='Online_chat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=500, verbose_name='\u5185\u5bb9')),
                ('send_time', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u9001\u65f6\u95f4')),
                ('business', models.ForeignKey(verbose_name='\u6240\u5c5e\u673a\u6784', to='erp.Business')),
                ('recipient', models.ForeignKey(related_name='recipient', verbose_name='\u63a5\u6536\u4eba', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(related_name='sender', verbose_name='\u53d1\u9001\u4eba', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
