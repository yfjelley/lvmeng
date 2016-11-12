# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0006_auto_20160223_0843'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='on_top',
            field=models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe4\xb8\x8a\xe9\xa6\x96\xe9\xa1\xb5'),
        ),
    ]
