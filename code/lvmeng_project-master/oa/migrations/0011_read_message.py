# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0049_auto_20160323_1757'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oa', '0010_auto_20160325_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='Read_message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('model_name', models.CharField(max_length=30, null=True, verbose_name='\u6a21\u5757\u540d', blank=True)),
                ('record_id', models.IntegerField(max_length=10, null=True, verbose_name='\u5173\u8054\u8bb0\u5f55\u7684ID', blank=True)),
                ('read_time', models.DateTimeField(auto_now_add=True, verbose_name='\u67e5\u770b\u65f6\u95f4')),
                ('read_business', models.ForeignKey(verbose_name='\u5173\u8054\u673a\u6784', blank=True, to='erp.Business', null=True)),
                ('read_user', models.ForeignKey(verbose_name='\u5df2\u8bfb\u7528\u6237', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
