# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('erp', '0097_merge'),
        ('oa', '0030_auto_20160414_1459'),
    ]

    operations = [
        migrations.CreateModel(
            name='All_Examine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField()),
                ('examine_status', models.CharField(default=b'3', max_length=1, verbose_name='\u5ba1\u6838\u7ed3\u679c\u9009\u62e9', choices=[(b'1', '\u901a\u8fc7'), (b'2', '\u9a73\u56de'), (b'3', '\u5f85\u5ba1\u6838')])),
                ('read_status', models.CharField(default=b'1', max_length=1, verbose_name='\u8bfb\u53d6\u72b6\u6001', choices=[(b'1', '\u672a\u8bfb'), (b'2', '\u5df2\u8bfb')])),
                ('examine_message', models.TextField(null=True, verbose_name='\u5ba1\u6279\u5907\u6ce8', blank=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='\u662f\u5426\u6709\u6548')),
                ('examine_time', models.DateTimeField(null=True, verbose_name='\u5ba1\u6279\u65f6\u95f4', blank=True)),
                ('content_type', models.ForeignKey(related_name='content_type_timelines', blank=True, to='contenttypes.ContentType', null=True)),
                ('examine_business', models.ForeignKey(verbose_name='\u5173\u8054\u673a\u6784', blank=True, to='erp.Business', null=True)),
                ('examine_user', models.ForeignKey(verbose_name='\u5ba1\u6279\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]