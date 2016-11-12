# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0087_agent_qrcode'),
        ('api', '0013_auto_20160419_1339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attention',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('register_time', models.DateTimeField(verbose_name='\u6536\u85cf\u65f6\u95f4')),
                ('customer', models.ForeignKey(verbose_name='\u7528\u6237', blank=True, to='erp.Customer', null=True)),
                ('product', models.ForeignKey(verbose_name='\u4ea7\u54c1', blank=True, to='erp.Product', null=True)),
            ],
            options={
                'ordering': ['-register_time'],
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('register_time', models.DateTimeField(verbose_name='\u6536\u85cf\u65f6\u95f4')),
                ('customer', models.ForeignKey(verbose_name='\u7528\u6237', blank=True, to='erp.Customer', null=True)),
                ('product', models.ForeignKey(verbose_name='\u4ea7\u54c1', blank=True, to='erp.Product', null=True)),
            ],
            options={
                'ordering': ['-register_time'],
            },
        ),
    ]
