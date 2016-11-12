# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0065_customer_avatar'),
        ('api', '0012_checkin_continuous_days'),
    ]

    operations = [
        migrations.CreateModel(
            name='History_Checkin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('register_date', models.DateField(auto_now_add=True, verbose_name='\u7b7e\u5230\u65e5\u671f', null=True)),
                ('abscissa', models.CharField(max_length=30, verbose_name='\u6a2a\u5750\u6807')),
                ('ordinate', models.CharField(max_length=30, verbose_name='\u7eb5\u5750\u6807')),
                ('customer', models.ForeignKey(verbose_name='\u7528\u6237', blank=True, to='erp.Customer', null=True)),
            ],
            options={
                'ordering': ['-register_date'],
            },
        ),
        migrations.AlterModelOptions(
            name='checkin',
            options={'ordering': ['-latest_date']},
        ),
        migrations.RemoveField(
            model_name='checkin',
            name='register_date',
        ),
        migrations.AddField(
            model_name='checkin',
            name='abscissa',
            field=models.CharField(max_length=30, null=True, verbose_name='\u6a2a\u5750\u6807', blank=True),
        ),
        migrations.AddField(
            model_name='checkin',
            name='latest_date',
            field=models.DateField(null=True, verbose_name='\u6700\u540e\u7b7e\u5230\u65e5\u671f', blank=True),
        ),
        migrations.AddField(
            model_name='checkin',
            name='ordinate',
            field=models.CharField(max_length=30, null=True, verbose_name='\u7eb5\u5750\u6807', blank=True),
        ),
        migrations.AddField(
            model_name='checkin',
            name='points',
            field=models.IntegerField(null=True, verbose_name='\u79ef\u5206', blank=True),
        ),
        migrations.AlterField(
            model_name='checkin',
            name='customer',
            field=models.OneToOneField(null=True, blank=True, to='erp.Customer', verbose_name='\u7528\u6237'),
        ),
    ]
