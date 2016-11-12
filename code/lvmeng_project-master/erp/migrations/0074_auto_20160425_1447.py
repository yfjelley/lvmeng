# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('erp', '0073_auto_20160422_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name='\u804c\u4f4d\u540d\u79f0')),
                ('register_date', models.DateField(null=True, verbose_name='\u6dfb\u52a0\u65e5\u671f', blank=True)),
                ('entry_person', models.CharField(max_length=20, verbose_name='\u5f55\u5165\u4eba')),
                ('business', models.ForeignKey(verbose_name='\u6240\u5c5e\u673a\u6784', to='erp.Business')),
                ('permissions', models.ManyToManyField(to='auth.Permission', verbose_name='\u804c\u4f4d\u6743\u9650')),
            ],
        ),
        migrations.RemoveField(
            model_name='agent',
            name='job',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='role',
        ),
    ]
