# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0116_auto_20160526_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='on_top',
            field=models.BooleanField(default=False, verbose_name='\u8bf7\u9009\u62e9\u662f\u5426\u4e0a\u9996\u9875'),
        ),
    ]
