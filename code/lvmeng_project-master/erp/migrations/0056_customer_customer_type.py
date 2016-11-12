# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0055_auto_20160411_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='customer_type',
            field=models.CharField(default=b'1', max_length=2, verbose_name='\u5ba2\u6237\u7c7b\u578b', choices=[(b'1', '\u771f\u5b9e\u5ba2\u6237'), (b'2', '\u610f\u5411\u5ba2\u6237')]),
        ),
    ]
