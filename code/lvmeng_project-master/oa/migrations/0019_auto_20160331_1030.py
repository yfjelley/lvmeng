# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oa', '0018_auto_20160330_1759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cost_application',
            name='read_status',
        ),
        migrations.RemoveField(
            model_name='leave_management',
            name='read_status',
        ),
        migrations.RemoveField(
            model_name='travel_apply',
            name='read_status',
        ),
    ]
