# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0044_auto_20160316_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='announce_business',
            field=models.ForeignKey(related_name='announce_business', default=1, verbose_name=b'\xe5\x85\xb3\xe8\x81\x94\xe6\x9c\xba\xe6\x9e\x84', to='erp.Business'),
            preserve_default=False,
        ),
    ]
