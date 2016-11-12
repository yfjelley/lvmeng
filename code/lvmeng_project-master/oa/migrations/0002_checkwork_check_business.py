# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0048_auto_20160316_1531'),
        ('oa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkwork',
            name='check_business',
            field=models.ForeignKey(default=4, verbose_name=b'\xe5\x85\xb3\xe8\x81\x94\xe6\x9c\xba\xe6\x9e\x84', to='erp.Business'),
            preserve_default=False,
        ),
    ]
