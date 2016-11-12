# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_verificationcode_purpose'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='business',
        ),
        migrations.DeleteModel(
            name='Announcement',
        ),
    ]
