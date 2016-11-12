# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0063_auto_20160411_1536'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='real_purchase',
            options={'ordering': ['customer', '-register_time']},
        ),
    ]
