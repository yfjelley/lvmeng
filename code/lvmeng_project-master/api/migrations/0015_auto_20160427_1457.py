# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_attention_collection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attention',
            name='register_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u5173\u6ce8\u65f6\u95f4', null=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='register_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u6536\u85cf\u65f6\u95f4', null=True),
        ),
    ]
