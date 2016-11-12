# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0130_auto_20160725_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='redister_business',
            name='status',
            field=models.CharField(default=b'3', max_length=2, verbose_name='\u5ba1\u6838\u72b6\u6001', choices=[(b'1', '\u901a\u8fc7'), (b'2', '\u9a73\u56de'), (b'3', '\u6ce8\u518c\u5ba1\u6838')]),
        ),
    ]
