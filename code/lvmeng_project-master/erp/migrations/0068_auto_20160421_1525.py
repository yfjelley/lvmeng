# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.exceptions


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0067_auto_20160421_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='avatar',
            field=models.ImageField(upload_to=b'agent/avatar/', null=True, verbose_name='\u5934\u50cf\u56fe\u7247(\u5c3a\u5bf8\u5927\u5c0f:50*50)', blank=True),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='picture',
            field=models.ImageField(blank=True, upload_to=b'business/pictures/', null=True, verbose_name='\u673a\u6784\u56fe\u7247(\u5c3a\u5bf8\u5927\u5c0f:375*106)', validators=[django.core.exceptions.ValidationError]),
        ),
        migrations.AlterField(
            model_name='business',
            name='logo',
            field=models.ImageField(upload_to=b'business/logo/', verbose_name='\u673a\u6784\u6807\u5fd7(\u5c3a\u5bf8\u5927\u5c0f:50*50)'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='avatar',
            field=models.ImageField(upload_to=b'customer/avatar/', null=True, verbose_name='\u5934\u50cf\u56fe\u7247(\u5c3a\u5bf8\u5927\u5c0f:50*50)', blank=True),
        ),
        migrations.AlterField(
            model_name='customer_pending',
            name='calling_card',
            field=models.ImageField(upload_to=b'customer/calling_card/', null=True, verbose_name='\u540d\u7247(\u5c3a\u5bf8\u5927\u5c0f:50*50)', blank=True),
        ),
    ]
