# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oa', '0016_auto_20160330_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave_management',
            name='leave_business',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u673a\u6784', blank=True, to='erp.Business', null=True),
        ),
        migrations.AlterField(
            model_name='travel_apply',
            name='travel_business',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u673a\u6784', blank=True, to='erp.Business', null=True),
        ),
    ]
