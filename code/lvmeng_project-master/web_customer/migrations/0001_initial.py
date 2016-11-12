# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lv_Announcement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.ImageField(upload_to=b'lvmeng/announcement/', null=True, verbose_name='\u673a\u6784\u516c\u544a\u56fe\u7247(\u5c3a\u5bf8\u5927\u5c0f:375*106)', blank=True)),
                ('title', models.CharField(max_length=30, verbose_name='\u6807\u9898')),
                ('date', models.DateField(verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('text', models.TextField(max_length=500, null=True, verbose_name='\u5185\u5bb9\u8bf4\u660e', blank=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='\u662f\u5426\u6709\u6548')),
            ],
        ),
    ]
