# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0081_auto_20160426_1426'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agent',
            options={'ordering': ['-register_date']},
        ),
    ]
