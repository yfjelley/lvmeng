# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0131_redister_business_status'),
        ('oa', '0048_auto_20160620_1404'),
    ]

    operations = [
        migrations.CreateModel(
            name='Check_Time_Setting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('check_in_time', models.TimeField(verbose_name='\u7b7e\u5230\u65f6\u95f4')),
                ('check_out_time', models.TimeField(verbose_name='\u7b7e\u9000\u65f6\u95f4')),
                ('check_in_remind', models.TimeField(verbose_name='\u7b7e\u5230\u63d0\u9192')),
                ('check_out_remind', models.TimeField(verbose_name='\u7b7e\u9000\u63d0\u9192')),
                ('business', models.ForeignKey(verbose_name='\u5173\u8054\u673a\u6784', to='erp.Business')),
            ],
        ),
    ]
