# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_point'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='attention',
            unique_together=set([('customer', 'product')]),
        ),
        migrations.AlterUniqueTogether(
            name='collection',
            unique_together=set([('customer', 'product')]),
        ),
    ]
