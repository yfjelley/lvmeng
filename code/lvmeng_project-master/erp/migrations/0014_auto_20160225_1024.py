# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0013_auto_20160224_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='entry_person',
            field=models.CharField(default=1, max_length=20, verbose_name=b'\xe5\xbd\x95\xe5\x85\xa5\xe4\xba\xba'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='role',
            name='business',
            field=models.ForeignKey(verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe6\x9c\xba\xe6\x9e\x84', to='erp.Business'),
        ),
    ]
