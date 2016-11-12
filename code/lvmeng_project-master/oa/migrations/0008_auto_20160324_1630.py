# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oa', '0007_cost_application_daily_work_leave_management_travel_apply'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cost_application',
            options={'ordering': ['-apply_time']},
        ),
        migrations.AlterModelOptions(
            name='daily_work',
            options={'ordering': ['-daily_time']},
        ),
        migrations.AlterModelOptions(
            name='internal_announcement',
            options={'ordering': ['-add_time']},
        ),
        migrations.AlterModelOptions(
            name='leave_management',
            options={'ordering': ['-apply_time']},
        ),
        migrations.AlterModelOptions(
            name='travel_apply',
            options={'ordering': ['-apply_time']},
        ),
    ]
