# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oa', '0038_auto_20160516_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_work',
            name='business',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u673a\u6784', blank=True, to='erp.Business', null=True),
        ),
    ]
