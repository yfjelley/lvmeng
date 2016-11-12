# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_auto_20160617_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headline',
            name='title',
            field=models.CharField(default=b'', unique=True, max_length=30, verbose_name='\u6807\u9898'),
        ),
    ]
