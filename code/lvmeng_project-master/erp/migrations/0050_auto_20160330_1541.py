# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0049_auto_20160323_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_Pending',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=30, verbose_name='\u59d3\u540d')),
                ('phoneNum', models.CharField(max_length=18, verbose_name='\u7535\u8bdd')),
                ('sex', models.CharField(default=1, choices=[(b'1', '\u7537'), (b'2', '\u5973')], max_length=2, blank=True, null=True, verbose_name='\u6027\u522b')),
                ('address', models.CharField(max_length=30, null=True, verbose_name='\u5ba2\u6237\u5730\u5740', blank=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='\u662f\u5426\u6709\u6548')),
                ('register_date', models.DateField(null=True, verbose_name='\u6ce8\u518c\u65e5\u671f', blank=True)),
                ('idCard_num', models.CharField(max_length=30, null=True, verbose_name='\u8eab\u4efd\u8bc1\u53f7', blank=True)),
                ('note', models.TextField(max_length=300, null=True, verbose_name='\u5907\u6ce8', blank=True)),
                ('industry', models.CharField(max_length=30, null=True, verbose_name='\u884c\u4e1a', blank=True)),
                ('city', models.CharField(max_length=30, null=True, verbose_name='\u57ce\u5e02', blank=True)),
                ('agents', models.ForeignKey(verbose_name='\u6240\u5c5e\u7406\u8d22\u5e08', blank=True, to='erp.Agent', null=True)),
            ],
            options={
                'ordering': ['-register_date'],
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.CharField(max_length=30, null=True, verbose_name='\u57ce\u5e02', blank=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='industry',
            field=models.CharField(max_length=30, null=True, verbose_name='\u884c\u4e1a', blank=True),
        ),
    ]
