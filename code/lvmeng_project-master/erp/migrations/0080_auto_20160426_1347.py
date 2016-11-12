# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0079_auto_20160426_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='agent_num',
            field=models.PositiveIntegerField(null=True, verbose_name='\u5458\u5de5\u7f16\u53f7(\u673a\u6784\u7f16\u53f7+\u5458\u5de5\u7f16\u53f7\u4e3a\u9080\u8bf7\u7801)', blank=True),
        ),
    ]
