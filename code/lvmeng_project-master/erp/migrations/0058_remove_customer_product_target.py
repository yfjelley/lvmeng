# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0057_auto_20160411_1422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='product_target',
        ),
    ]
