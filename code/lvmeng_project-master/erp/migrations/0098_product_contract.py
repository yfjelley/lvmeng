# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0097_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='contract',
            field=models.FileField(default=1, upload_to=b'product/contract/', verbose_name='\u4ea7\u54c1\u5408\u540c'),
            preserve_default=False,
        ),
    ]
