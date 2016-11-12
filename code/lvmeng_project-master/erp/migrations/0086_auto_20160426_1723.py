# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.exceptions


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0085_auto_20160426_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='order',
            field=models.PositiveIntegerField(verbose_name='\u987a\u5e8f'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='picture',
            field=models.ImageField(blank=True, upload_to=b'business/pictures/', null=True, verbose_name='\u673a\u6784\u516c\u544a\u56fe\u7247(\u5c3a\u5bf8\u5927\u5c0f:375*106)', validators=[django.core.exceptions.ValidationError]),
        ),
    ]
