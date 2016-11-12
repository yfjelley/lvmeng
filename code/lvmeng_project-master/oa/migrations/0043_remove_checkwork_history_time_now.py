# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oa', '0042_auto_20160602_1329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkwork_history',
            name='time_now',
        ),
    ]
