# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0020_auto_20160226_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='business_num',
            field=models.CharField(unique=True, max_length=20, verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe7\xbc\x96\xe5\x8f\xb7'),
        ),
    ]
