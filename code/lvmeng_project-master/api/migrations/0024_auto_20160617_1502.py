# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_auto_20160617_1500'),
    ]

    operations = [
        migrations.RenameField(
            model_name='headline',
            old_name='add_time',
            new_name='add_date',
        ),
    ]
