# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0026_auto_20160302_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='logo',
            field=models.ImageField(default=1, upload_to=b'', verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe6\xa0\x87\xe5\xbf\x97'),
            preserve_default=False,
        ),
    ]
