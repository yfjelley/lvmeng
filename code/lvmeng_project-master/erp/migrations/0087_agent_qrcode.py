# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0086_auto_20160426_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='qrcode',
            field=models.ImageField(upload_to=b'agent/qrcode/', null=True, verbose_name='\u5458\u5de5\u4e8c\u7ef4\u7801', blank=True),
        ),
    ]
