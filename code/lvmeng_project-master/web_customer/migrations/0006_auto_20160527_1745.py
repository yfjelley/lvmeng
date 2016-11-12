# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_customer', '0005_business_carousel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business_carousel',
            name='carousel',
            field=models.ImageField(upload_to=b'business/carousel/', null=True, verbose_name='\u8f6e\u64ad\u56fe', blank=True),
        ),
    ]
