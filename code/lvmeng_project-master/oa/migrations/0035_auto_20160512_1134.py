# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oa', '0034_auto_20160512_1119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leave_management',
            old_name='leave_reason',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='leave_management',
            old_name='leave_end',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='leave_management',
            old_name='leave_start',
            new_name='start',
        ),
        migrations.RenameField(
            model_name='leave_management',
            old_name='leave_type',
            new_name='topic',
        ),
        migrations.RenameField(
            model_name='travel_apply',
            old_name='travel_place',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='travel_apply',
            old_name='travel_cost',
            new_name='cost',
        ),
        migrations.RenameField(
            model_name='travel_apply',
            old_name='travel_end',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='travel_apply',
            old_name='travel_start',
            new_name='start',
        ),
        migrations.RenameField(
            model_name='travel_apply',
            old_name='travel_reason',
            new_name='topic',
        ),
    ]
