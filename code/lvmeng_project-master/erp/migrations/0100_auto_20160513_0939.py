# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0099_auto_20160512_1146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='avatar',
            new_name='portrait',
        ),
    ]
