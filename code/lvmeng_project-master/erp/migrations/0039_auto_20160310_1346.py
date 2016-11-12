# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0038_auto_20160310_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='abbreviation',
            field=models.CharField(default=1, max_length=100, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe7\xae\x80\xe7\xa7\xb0(\xe6\x98\xbe\xe7\xa4\xba\xe5\x9c\xa8\xe9\xa6\x96\xe9\xa1\xb5)'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='mini_sub',
            field=models.BigIntegerField(default=1, verbose_name=b'\xe8\xae\xa4\xe8\xb4\xad\xe8\xb5\xb7\xe7\x82\xb9(\xe6\x98\xbe\xe7\xa4\xba\xe5\x9c\xa8\xe9\xa6\x96\xe9\xa1\xb5)'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default=b'\xe6\x9c\xaa\xe5\x91\xbd\xe5\x90\x8d', max_length=100, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\x85\xa8\xe5\x90\x8d(\xe6\x98\xbe\xe7\xa4\xba\xe5\x9c\xa8\xe9\xa6\x96\xe9\xa1\xb5)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='period',
            field=models.IntegerField(default=1, verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4\xe9\x95\xbf\xe5\xba\xa6/\xe6\x9c\x88(\xe6\x98\xbe\xe7\xa4\xba\xe5\x9c\xa8\xe9\xa6\x96\xe9\xa1\xb5)'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe7\xb1\xbb\xe5\x9e\x8b(\xe6\x98\xbe\xe7\xa4\xba\xe5\x9c\xa8\xe9\xa6\x96\xe9\xa1\xb5)', to='erp.Product_Type'),
        ),
        migrations.AlterField(
            model_name='product',
            name='return_expected',
            field=models.DecimalField(null=True, verbose_name=b'\xe9\xa2\x84\xe6\x9c\x9f\xe6\x94\xb6\xe7\x9b\x8a(\xe6\x98\xbe\xe7\xa4\xba\xe5\x9c\xa8\xe9\xa6\x96\xe9\xa1\xb5)', max_digits=6, decimal_places=4),
        ),
    ]
