# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0064_auto_20160411_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='avatar',
            field=models.ImageField(upload_to=b'customer/avatar/', null=True, verbose_name='\u5934\u50cf\u56fe\u7247', blank=True),
        ),
    ]
