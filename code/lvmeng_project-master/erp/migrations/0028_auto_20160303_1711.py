# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0027_business_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField(null=True, verbose_name=b'\xe8\xb4\xad\xe4\xb9\xb0\xe9\x87\x91\xe9\xa2\x9d', blank=True)),
                ('start_date', models.DateField(null=True, verbose_name=b'\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xa5\xe6\x9c\x9f', blank=True)),
                ('end_date', models.DateField(null=True, verbose_name=b'\xe7\xbb\x93\xe6\x9d\x9f\xe6\x97\xa5\xe6\x9c\x9f', blank=True)),
                ('buy_time', models.DateTimeField(null=True, verbose_name=b'\xe8\xb4\xad\xe4\xb9\xb0\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('customer', models.ForeignKey(verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7', blank=True, to='erp.Customer', null=True)),
                ('product', models.ForeignKey(verbose_name=b'\xe4\xba\xa7\xe5\x93\x81', blank=True, to='erp.Product', null=True)),
            ],
            options={
                'ordering': ['-buy_time'],
            },
        ),
        migrations.AlterField(
            model_name='business',
            name='logo',
            field=models.ImageField(upload_to=b'business/logo/', verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe6\xa0\x87\xe5\xbf\x97'),
        ),
    ]
