# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0049_auto_20160323_1757'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oa', '0012_auto_20160328_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cost_examine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('examine_status', models.CharField(default=b'1', max_length=1, verbose_name='\u5ba1\u6838\u7ed3\u679c\u9009\u62e9', choices=[(b'1', '\u901a\u8fc7'), (b'2', '\u9a73\u56de')])),
                ('examine_message', models.TextField(null=True, verbose_name='\u5ba1\u6279\u5907\u6ce8', blank=True)),
                ('examine_time', models.DateTimeField(auto_now_add=True, verbose_name='\u5ba1\u6279\u65f6\u95f4')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='cost_application',
            name='examine_user',
            field=models.ManyToManyField(related_name='cost_examine_user', null=True, verbose_name='\u5ba1\u6279\u4eba', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='leave_management',
            name='examine_user',
            field=models.ManyToManyField(related_name='leave_examine_user', null=True, verbose_name='\u5ba1\u6279\u4eba', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='travel_apply',
            name='examine_user',
            field=models.ManyToManyField(related_name='travel_examine_user', null=True, verbose_name='\u5ba1\u6279\u4eba', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='cost_examine',
            name='cost_examine',
            field=models.ForeignKey(verbose_name='\u5173\u8054\u8d39\u7528\u7533\u8bf7', to='oa.Cost_application'),
        ),
        migrations.AddField(
            model_name='cost_examine',
            name='examine_business',
            field=models.ForeignKey(verbose_name='\u5173\u8054\u673a\u6784', blank=True, to='erp.Business', null=True),
        ),
        migrations.AddField(
            model_name='cost_examine',
            name='examine_user',
            field=models.ForeignKey(verbose_name='\u5ba1\u6279\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
