# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0083_auto_20160426_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='business',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u673a\u6784', blank=True, to='erp.Business', null=True),
        ),
    ]
