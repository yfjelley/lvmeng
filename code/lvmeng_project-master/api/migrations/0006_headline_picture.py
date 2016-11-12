# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20160316_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='headline',
            name='picture',
            field=models.ImageField(upload_to=b'api/headlines/', null=True, verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe5\x9b\xbe\xe7\x89\x87', blank=True),
        ),
    ]
