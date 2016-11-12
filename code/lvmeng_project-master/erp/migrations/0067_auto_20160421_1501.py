# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.exceptions


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0066_auto_20160418_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='picture',
            field=models.ImageField(blank=True, upload_to=b'business/pictures/', null=True, verbose_name='\u673a\u6784\u56fe\u7247(\u5c3a\u5bf8\u5927\u5c0f\uff1a375*106)', validators=[django.core.exceptions.ValidationError]),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='show_text',
            field=models.BooleanField(default=True, verbose_name='\u662f\u5426\u663e\u793a\u5728app\u9996\u9875\u8f6e\u64ad\u56fe(\u9700\u8981\u63d2\u5165\u56fe\u7247)'),
        ),
    ]
