# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_headline_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headline',
            name='picture',
            field=models.ImageField(upload_to=b'api/headlines/', null=True, verbose_name=b'\xe7\xae\x80\xe5\x9b\xbe', blank=True),
        ),
    ]
