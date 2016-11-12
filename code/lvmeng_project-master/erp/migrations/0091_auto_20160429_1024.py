# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0090_auto_20160429_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='logo',
            field=models.ImageField(upload_to=b'business/logo/', null=True, verbose_name='\u673a\u6784\u6807\u5fd7(\u5c3a\u5bf8\u5927\u5c0f:50*50)', blank=True),
        ),
    ]
