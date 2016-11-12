# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0049_auto_20160323_1757'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oa', '0006_internal_announcement_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cost_application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('apply_topic', models.CharField(max_length=20, verbose_name=b'\xe7\x94\xb3\xe8\xaf\xb7\xe6\x9d\xa1\xe7\x9b\xae')),
                ('apply_content', models.CharField(max_length=100, verbose_name=b'\xe7\x94\xb3\xe8\xaf\xb7\xe5\x86\x85\xe5\xae\xb9')),
                ('cost', models.DecimalField(verbose_name=b'\xe9\x87\x91\xe9\xa2\x9d', max_digits=6, decimal_places=2)),
                ('apply_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe7\x94\xb3\xe8\xaf\xb7\xe6\x97\xb6\xe9\x97\xb4')),
                ('cost_business', models.ForeignKey(verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe6\x9c\xba\xe6\x9e\x84', to='erp.Business')),
                ('cost_user', models.ForeignKey(verbose_name=b'\xe7\x94\xb3\xe8\xaf\xb7\xe4\xba\xba', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Daily_work',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('summary', models.CharField(max_length=100, verbose_name=b'\xe5\xbd\x93\xe5\xa4\xa9\xe6\x80\xbb\xe7\xbb\x93')),
                ('tomorrow_plan', models.CharField(max_length=100, verbose_name=b'\xe6\x98\x8e\xe6\x97\xa5\xe8\xae\xa1\xe5\x88\x92')),
                ('daily_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\xa1\xab\xe6\x8a\xa5\xe6\x97\xb6\xe9\x97\xb4')),
                ('daily_business', models.ForeignKey(verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe6\x9c\xba\xe6\x9e\x84', to='erp.Business')),
                ('daily_user', models.ForeignKey(verbose_name=b'\xe5\xa1\xab\xe6\x8a\xa5\xe4\xba\xba', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Leave_management',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('leave_type', models.CharField(max_length=20, verbose_name=b'\xe8\xaf\xb7\xe5\x81\x87\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('leave_reason', models.CharField(max_length=100, verbose_name=b'\xe8\xaf\xb7\xe5\x81\x87\xe5\x8e\x9f\xe5\x9b\xa0')),
                ('leave_start', models.DateField(verbose_name=b'\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xb6\xe9\x97\xb4')),
                ('leave_end', models.DateField(verbose_name=b'\xe7\xbb\x93\xe6\x9d\x9f\xe6\x97\xb6\xe9\x97\xb4')),
                ('apply_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe7\x94\xb3\xe8\xaf\xb7\xe6\x97\xb6\xe9\x97\xb4')),
                ('leave_business', models.ForeignKey(verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe6\x9c\xba\xe6\x9e\x84', to='erp.Business')),
                ('leave_user', models.ForeignKey(verbose_name=b'\xe8\xaf\xb7\xe5\x81\x87\xe4\xba\xba', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Travel_apply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('travel_reason', models.CharField(max_length=30, verbose_name=b'\xe5\x87\xba\xe5\xb7\xae\xe4\xba\x8b\xe7\x94\xb1')),
                ('travel_place', models.CharField(max_length=30, verbose_name=b'\xe5\x87\xba\xe5\xb7\xae\xe5\x9c\xb0\xe7\x82\xb9')),
                ('travel_cost', models.DecimalField(verbose_name=b'\xe9\x87\x91\xe9\xa2\x9d', max_digits=6, decimal_places=2)),
                ('travel_start', models.DateField(verbose_name=b'\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xb6\xe9\x97\xb4')),
                ('travel_end', models.DateField(verbose_name=b'\xe7\xbb\x93\xe6\x9d\x9f\xe6\x97\xb6\xe9\x97\xb4')),
                ('apply_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe7\x94\xb3\xe8\xaf\xb7\xe6\x97\xb6\xe9\x97\xb4')),
                ('travel_business', models.ForeignKey(verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe6\x9c\xba\xe6\x9e\x84', to='erp.Business')),
                ('travel_user', models.ForeignKey(verbose_name=b'\xe7\x94\xb3\xe8\xaf\xb7\xe4\xba\xba', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
