# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lv_announcement',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='lv_announcement',
            name='text',
            field=models.TextField(max_length=3000, null=True, verbose_name='\u5185\u5bb9\u8bf4\u660e', blank=True),
        ),
    ]
