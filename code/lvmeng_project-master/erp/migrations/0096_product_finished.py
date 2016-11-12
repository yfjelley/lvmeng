# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0095_auto_20160504_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='finished',
            field=models.BooleanField(default=False, verbose_name='\u5df2\u5b8c\u6210'),
        ),
    ]
