# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('erp', '0128_auto_20160617_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='Redister_Business',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('logo', models.ImageField(upload_to=b'business/logo/', null=True, verbose_name='\u673a\u6784logo(\u5c3a\u5bf8\u5927\u5c0f:50*50,png\u683c\u5f0f)', blank=True)),
                ('business_qrcode', models.ImageField(upload_to=b'business/qrcode/', null=True, verbose_name='\u673a\u6784\u5fae\u4fe1\u516c\u4f17\u53f7(\u5c55\u793a\u5728\u5ba2\u6237\u7aef\u9996\u9875)', blank=True)),
                ('business_license_original', models.ImageField(upload_to=b'business/license', null=True, verbose_name='\u8425\u4e1a\u6267\u7167\uff08\u539f\u4ef6\u626b\u63cf\uff09', blank=True)),
                ('business_license_copy', models.ImageField(upload_to=b'business/license', null=True, verbose_name='\u8425\u4e1a\u6267\u7167\uff08\u590d\u5370\u4ef6\u76d6\u7ae0\uff09', blank=True)),
                ('idCard_positive', models.ImageField(upload_to=b'idCard/image', null=True, verbose_name='\u6cd5\u4eba\u8eab\u4efd\u8bc1\u6b63\u9762', blank=True)),
                ('idCard_negative', models.ImageField(upload_to=b'idCard/image', null=True, verbose_name='\u6cd5\u4eba\u8eab\u4efd\u8bc1\u53cd\u9762', blank=True)),
                ('name', models.CharField(default=b'', max_length=50, verbose_name='\u673a\u6784\u540d\u79f0')),
                ('phoneNum', models.CharField(max_length=18, verbose_name='\u7535\u8bdd')),
                ('business_phone', models.CharField(max_length=18, verbose_name='\u673a\u6784\u516c\u4f17\u7535\u8bdd(\u5c55\u793a\u5728\u5ba2\u6237\u7aef\u9996\u9875)')),
                ('email', models.EmailField(max_length=254, verbose_name='\u7ba1\u7406\u5458\u90ae\u7bb1(\u767b\u5f55\u7528\u6237\u540d)')),
                ('business_email', models.EmailField(max_length=254, null=True, verbose_name='\u673a\u6784\u5bf9\u5916\u90ae\u7bb1(\u5c55\u793a\u5728\u5ba2\u6237\u7aef\u9996\u9875)', blank=True)),
                ('address', models.CharField(max_length=30, verbose_name='\u673a\u6784\u5730\u5740')),
                ('work_address', models.CharField(max_length=18, verbose_name='\u673a\u6784\u529e\u516c\u5730\u5740(\u5c55\u793a\u5728\u5ba2\u6237\u7aef\u9996\u9875)')),
                ('register_date', models.DateField(null=True, verbose_name='\u6ce8\u518c\u65e5\u671f', blank=True)),
                ('contact_name', models.CharField(max_length=20, null=True, verbose_name='\u76f4\u63a5\u8054\u7cfb\u4eba\u59d3\u540d', blank=True)),
                ('contact_position', models.CharField(max_length=20, null=True, verbose_name='\u76f4\u63a5\u8054\u7cfb\u4eba\u804c\u4f4d', blank=True)),
                ('brief_introduction', models.CharField(max_length=15, null=True, verbose_name='\u516c\u53f8\u7b80\u4ecb(15\u4e2a\u5b57\u4ee5\u5185,\u663e\u793a\u5728APP\u9996\u9875)', blank=True)),
                ('note', tinymce.models.HTMLField(null=True, verbose_name='\u516c\u53f8\u8be6\u60c5', blank=True)),
                ('is_active', models.BooleanField(default=False, verbose_name='\u662f\u5426\u6709\u6548')),
                ('user', models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL, verbose_name='\u5173\u8054\u7528\u6237')),
            ],
        ),
    ]
