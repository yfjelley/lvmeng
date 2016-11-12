# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0053_auto_20160331_1246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cell_Records_Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField(verbose_name='\u901a\u8bdd\u5f00\u59cb\u65f6\u95f4')),
                ('end_time', models.DateTimeField(verbose_name='\u901a\u8bdd\u7ed3\u675f\u65f6\u95f4')),
                ('agent', models.ForeignKey(verbose_name='\u7406\u8d22\u5e08', to='erp.Agent')),
                ('customer', models.ForeignKey(verbose_name='\u5ba2\u6237', to='erp.Customer')),
            ],
            options={
                'ordering': ['-start_time'],
            },
        ),
        migrations.CreateModel(
            name='Cell_Records_PCustomer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField(verbose_name='\u901a\u8bdd\u5f00\u59cb\u65f6\u95f4')),
                ('end_time', models.DateTimeField(verbose_name='\u901a\u8bdd\u7ed3\u675f\u65f6\u95f4')),
                ('agent', models.ForeignKey(verbose_name='\u7406\u8d22\u5e08', to='erp.Agent')),
                ('customer', models.ForeignKey(verbose_name='\u5ba2\u6237', to='erp.Customer')),
            ],
            options={
                'ordering': ['-start_time'],
            },
        ),
    ]
