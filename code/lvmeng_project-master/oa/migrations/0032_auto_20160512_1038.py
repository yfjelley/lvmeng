# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oa', '0031_all_examine'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cost_application',
            options={'ordering': ['-time']},
        ),
        migrations.AlterModelOptions(
            name='leave_management',
            options={'ordering': ['-time']},
        ),
        migrations.AlterModelOptions(
            name='travel_apply',
            options={'ordering': ['-time']},
        ),
        migrations.RenameField(
            model_name='cost_application',
            old_name='cost_business',
            new_name='business',
        ),
        migrations.RenameField(
            model_name='cost_application',
            old_name='apply_content',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='cost_application',
            old_name='apply_time',
            new_name='time',
        ),
        migrations.RenameField(
            model_name='cost_application',
            old_name='apply_topic',
            new_name='topic',
        ),
        migrations.RenameField(
            model_name='cost_application',
            old_name='cost_user',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='leave_management',
            old_name='leave_business',
            new_name='business',
        ),
        migrations.RenameField(
            model_name='leave_management',
            old_name='apply_time',
            new_name='time',
        ),
        migrations.RenameField(
            model_name='leave_management',
            old_name='leave_user',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='travel_apply',
            old_name='travel_business',
            new_name='business',
        ),
        migrations.RenameField(
            model_name='travel_apply',
            old_name='apply_time',
            new_name='time',
        ),
        migrations.RenameField(
            model_name='travel_apply',
            old_name='travel_user',
            new_name='user',
        ),
    ]
