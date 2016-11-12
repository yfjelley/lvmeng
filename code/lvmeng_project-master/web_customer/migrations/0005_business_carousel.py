# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0117_auto_20160526_1321'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web_customer', '0004_auto_20160511_1352'),
    ]

    operations = [
        migrations.CreateModel(
            name='business_carousel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('carousel', models.ImageField(upload_to=b'business/carousel/', verbose_name='\u8f6e\u64ad\u56fe')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('add_user', models.ForeignKey(verbose_name='\u6dfb\u52a0\u4eba', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('business', models.ForeignKey(verbose_name='\u6240\u5c5e\u673a\u6784', blank=True, to='erp.Business', null=True)),
            ],
            options={
                'ordering': ['-add_time'],
            },
        ),
    ]
