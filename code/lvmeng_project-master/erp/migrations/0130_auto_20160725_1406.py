# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0129_redister_business'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='entry_person',
            field=models.CharField(max_length=20, null=True, verbose_name='\u5f55\u5165\u5458', blank=True),
        ),
    ]
