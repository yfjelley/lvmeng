# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_customer', '0002_auto_20160509_1558'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lv_announcement',
            old_name='picture',
            new_name='lv_picture',
        ),
    ]
