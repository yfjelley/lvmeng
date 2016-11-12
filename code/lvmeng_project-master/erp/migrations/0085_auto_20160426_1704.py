# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0084_auto_20160426_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='announce_business',
            field=models.ForeignKey(related_name='announce_business', verbose_name='\u5173\u8054\u673a\u6784', blank=True, to='erp.Business', null=True),
        ),
    ]
