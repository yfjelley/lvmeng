# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0046_announcement_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='register_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4', null=True),
        ),
    ]
