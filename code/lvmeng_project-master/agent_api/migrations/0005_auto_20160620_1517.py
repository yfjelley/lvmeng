# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('agent_api', '0004_temporary_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temporary_file',
            name='user',
            field=models.ForeignKey(verbose_name='\u7528\u6237', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
