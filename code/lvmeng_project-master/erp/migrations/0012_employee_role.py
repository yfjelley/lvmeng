# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0011_auto_20160224_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='role',
            field=models.ForeignKey(default=1, verbose_name=b'\xe8\xa7\x92\xe8\x89\xb2', to='erp.Role'),
            preserve_default=False,
        ),
    ]
