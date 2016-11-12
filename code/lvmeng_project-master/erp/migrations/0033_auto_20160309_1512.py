# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0032_auto_20160308_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='business',
            field=models.ForeignKey(related_name='Agent_Business', verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe6\x9c\xba\xe6\x9e\x84', blank=True, to='erp.Business', null=True),
        ),
    ]
