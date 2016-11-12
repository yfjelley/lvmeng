# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0088_auto_20160427_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='business_license_copy',
            field=models.ImageField(upload_to=b'business/license', null=True, verbose_name='\u8425\u4e1a\u6267\u7167\uff08\u590d\u5370\u4ef6\u76d6\u7ae0\uff09', blank=True),
        ),
        migrations.AddField(
            model_name='business',
            name='business_license_original',
            field=models.ImageField(upload_to=b'business/license', null=True, verbose_name='\u8425\u4e1a\u6267\u7167\uff08\u539f\u4ef6\u626b\u63cf\uff09', blank=True),
        ),
        migrations.AddField(
            model_name='business',
            name='contact_name',
            field=models.CharField(max_length=20, null=True, verbose_name='\u76f4\u63a5\u8054\u7cfb\u4eba\u59d3\u540d', blank=True),
        ),
        migrations.AddField(
            model_name='business',
            name='contact_position',
            field=models.CharField(max_length=20, null=True, verbose_name='\u76f4\u63a5\u8054\u7cfb\u4eba\u804c\u4f4d', blank=True),
        ),
        migrations.AddField(
            model_name='business',
            name='idCard_negative',
            field=models.ImageField(upload_to=b'idCard/image', null=True, verbose_name='\u8eab\u4efd\u8bc1\u53cd\u9762', blank=True),
        ),
        migrations.AddField(
            model_name='business',
            name='idCard_positive',
            field=models.ImageField(upload_to=b'idCard/image', null=True, verbose_name='\u8eab\u4efd\u8bc1\u6b63\u9762', blank=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='address',
            field=models.CharField(max_length=30, verbose_name='\u5458\u5de5\u5730\u5740'),
        ),
    ]
