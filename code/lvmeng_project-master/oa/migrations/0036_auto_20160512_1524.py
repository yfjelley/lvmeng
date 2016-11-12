# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oa', '0035_auto_20160512_1134'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='all_examine',
            options={'ordering': ['read_status']},
        ),
    ]
