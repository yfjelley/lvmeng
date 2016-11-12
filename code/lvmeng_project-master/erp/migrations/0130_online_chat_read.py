# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0129_online_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='online_chat',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]
