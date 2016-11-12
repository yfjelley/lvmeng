# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phoneNum', models.CharField(max_length=18, verbose_name=b'\xe7\x94\xb5\xe8\xaf\x9d')),
                ('sex', models.CharField(default=1, max_length=2, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(b'1', b'\xe7\x94\xb7'), (b'2', b'\xe5\xa5\xb3')])),
                ('address', models.CharField(max_length=30, verbose_name=b'\xe5\xae\xa2\xe6\x88\xb7\xe5\x9c\xb0\xe5\x9d\x80')),
                ('register_date', models.DateTimeField(null=True, verbose_name=b'\xe6\xb3\xa8\xe5\x86\x8c\xe6\x97\xa5\xe6\x9c\x9f', blank=True)),
                ('idCard_num', models.CharField(max_length=30, verbose_name=b'\xe8\xba\xab\xe4\xbb\xbd\xe8\xaf\x81\xe5\x8f\xb7')),
                ('note', models.TextField(max_length=300, null=True, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
                ('user', models.OneToOneField(verbose_name=b'\xe5\x85\xb3\xe8\x81\x94\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-register_date'],
            },
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phoneNum', models.CharField(max_length=18, verbose_name=b'\xe7\x94\xb5\xe8\xaf\x9d')),
                ('address', models.CharField(max_length=30, verbose_name=b'\xe5\xae\xa2\xe6\x88\xb7\xe5\x9c\xb0\xe5\x9d\x80')),
                ('register_date', models.DateTimeField(null=True, verbose_name=b'\xe6\xb3\xa8\xe5\x86\x8c\xe6\x97\xa5\xe6\x9c\x9f', blank=True)),
                ('note', models.TextField(max_length=300, null=True, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
                ('user', models.OneToOneField(verbose_name=b'\xe5\x85\xb3\xe8\x81\x94\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-register_date'],
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phoneNum', models.CharField(max_length=18, verbose_name=b'\xe7\x94\xb5\xe8\xaf\x9d')),
                ('sex', models.CharField(default=1, max_length=2, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(b'1', b'\xe7\x94\xb7'), (b'2', b'\xe5\xa5\xb3')])),
                ('address', models.CharField(max_length=30, verbose_name=b'\xe5\xae\xa2\xe6\x88\xb7\xe5\x9c\xb0\xe5\x9d\x80')),
                ('register_date', models.DateTimeField(null=True, verbose_name=b'\xe6\xb3\xa8\xe5\x86\x8c\xe6\x97\xa5\xe6\x9c\x9f', blank=True)),
                ('idCard_num', models.CharField(max_length=30, verbose_name=b'\xe8\xba\xab\xe4\xbb\xbd\xe8\xaf\x81\xe5\x8f\xb7')),
                ('note', models.TextField(max_length=300, null=True, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
                ('user', models.OneToOneField(verbose_name=b'\xe5\x85\xb3\xe8\x81\x94\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-register_date'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'\xe6\x9c\xaa\xe5\x91\xbd\xe5\x90\x8d', max_length=100, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\x85\xa8\xe5\x90\x8d')),
                ('abbreviation', models.CharField(max_length=100, null=True, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe7\xae\x80\xe7\xa7\xb0', blank=True)),
                ('strategy', models.CharField(max_length=2000, null=True, verbose_name=b'\xe5\xae\x9e\xe6\x96\xbd\xe7\xad\x96\xe7\x95\xa5', blank=True)),
                ('custodian', models.CharField(max_length=100, null=True, verbose_name=b'\xe6\x89\x98\xe7\xae\xa1\xe6\x9c\xba\xe6\x9e\x84', blank=True)),
                ('term_footnote', models.CharField(max_length=2000, null=True, verbose_name=b'\xe5\x90\x88\xe5\x90\x8c\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
                ('manager', models.CharField(max_length=30, verbose_name=b'\xe6\x8a\x95\xe8\xb5\x84\xe7\xbb\x8f\xe7\x90\x86')),
                ('begin_date', models.DateField(null=True, verbose_name=b'\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xa5\xe6\x9c\x9f', blank=True)),
                ('end_date', models.DateField(null=True, verbose_name=b'\xe7\xbb\x93\xe6\x9d\x9f\xe6\x97\xa5\xe6\x9c\x9f', blank=True)),
                ('period', models.IntegerField(null=True, verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4\xe9\x95\xbf\xe5\xba\xa6\xef\xbc\x88\xe6\x9c\x88\xe4\xbb\xbd\xef\xbc\x89', blank=True)),
                ('mini_sub', models.BigIntegerField(null=True, verbose_name=b'\xe8\xae\xa4\xe8\xb4\xad\xe8\xb5\xb7\xe7\x82\xb9', blank=True)),
                ('addition', models.BigIntegerField(null=True, verbose_name=b'\xe8\xbf\xbd\xe5\x8a\xa0\xe9\xa2\x9d\xe5\xba\xa6', blank=True)),
                ('invest_scope', models.CharField(max_length=1000, null=True, verbose_name=b'\xe6\x8a\x95\xe8\xb5\x84\xe8\x8c\x83\xe5\x9b\xb4', blank=True)),
                ('alert_line', models.DecimalField(null=True, verbose_name=b'\xe9\xa2\x84\xe8\xad\xa6\xe7\xba\xbf', max_digits=6, decimal_places=4, blank=True)),
                ('clearance_line', models.DecimalField(null=True, verbose_name=b'\xe6\xb8\x85\xe7\x9b\x98\xe7\xba\xbf', max_digits=6, decimal_places=4, blank=True)),
                ('risk_preference', models.CharField(max_length=1000, null=True, verbose_name=b'\xe9\xa3\x8e\xe9\x99\xa9\xe5\x81\x8f\xe5\xa5\xbd', blank=True)),
                ('return_expected', models.DecimalField(null=True, verbose_name=b'\xe9\xa2\x84\xe6\x9c\x9f\xe6\x94\xb6\xe7\x9b\x8a', max_digits=6, decimal_places=4)),
                ('subscription_fee', models.DecimalField(null=True, verbose_name=b'\xe8\xae\xa2\xe9\x98\x85\xe8\xb4\xb9', max_digits=6, decimal_places=4, blank=True)),
                ('custody_fee', models.DecimalField(null=True, verbose_name=b'\xe6\x89\x98\xe7\xae\xa1\xe8\xb4\xb9', max_digits=6, decimal_places=4, blank=True)),
                ('service_fee', models.DecimalField(null=True, verbose_name=b'\xe7\xbb\xbc\xe5\x90\x88\xe6\x9c\x8d\xe5\x8a\xa1\xe8\xb4\xb9', max_digits=6, decimal_places=4, blank=True)),
                ('redemption_fee', models.DecimalField(null=True, verbose_name=b'\xe6\x8f\x90\xe5\x89\x8d\xe8\xb5\x8e\xe5\x9b\x9e\xe8\xb4\xb9', max_digits=6, decimal_places=4, blank=True)),
                ('management_fee', models.DecimalField(null=True, verbose_name=b'\xe7\xae\xa1\xe7\x90\x86\xe8\xb4\xb9', max_digits=6, decimal_places=4, blank=True)),
                ('compensation', models.DecimalField(null=True, verbose_name=b'\xe4\xb8\x9a\xe7\xbb\xa9\xe6\x8a\xa5\xe9\x85\xac\xef\xbc\x88\xe7\x9b\x88\xe5\x88\xa9\xe9\x83\xa8\xe5\x88\x86\xef\xbc\x89', max_digits=6, decimal_places=4, blank=True)),
                ('compensation_distribution', models.CharField(max_length=2000, null=True, verbose_name=b'\xe6\x94\xb6\xe7\x9b\x8a\xe5\x88\x86\xe9\x85\x8d\xef\xbc\x88\xe7\xbb\x93\xe6\x9e\x84\xe5\x8c\x96\xef\xbc\x89', blank=True)),
            ],
        ),
    ]
