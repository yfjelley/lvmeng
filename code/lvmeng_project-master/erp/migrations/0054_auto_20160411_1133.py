# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0053_auto_20160331_1246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Real_purchase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('customer_type', models.CharField(default=b'1', max_length=2, verbose_name='\u5ba2\u6237\u7c7b\u578b', choices=[(b'1', '\u771f\u5b9e\u5ba2\u6237'), (b'2', '\u610f\u5411\u5ba2\u6237')])),
                ('amount', models.IntegerField(verbose_name='\u5b9e\u6536\u91d1\u989d')),
                ('income_date', models.DateField(verbose_name='\u6536\u6b3e\u65e5\u671f')),
                ('end_date', models.DateField(verbose_name='\u4ea7\u54c1\u7ed3\u675f\u65e5\u671f')),
                ('pay_type', models.CharField(default=b'1', max_length=3, verbose_name='\u4ed8\u6b3e\u65b9\u5f0f', choices=[(b'1', '\u73b0\u91d1'), (b'2', '\u6c47\u7968'), (b'3', '\u652f\u7968')])),
                ('department', models.CharField(max_length=10, null=True, verbose_name='\u90e8\u95e8', blank=True)),
                ('bill_number', models.CharField(max_length=50, null=True, verbose_name='\u7968\u636e\u5355\u53f7', blank=True)),
                ('register_time', models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('brief', models.TextField(max_length=150, null=True, verbose_name='\u7b80\u4ecb', blank=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='\u662f\u5426\u6709\u6548')),
                ('business', models.ForeignKey(verbose_name='\u6240\u5c5e\u673a\u6784', to='erp.Business')),
            ],
            options={
                'ordering': ['-income_date'],
            },
        ),
        migrations.AlterField(
            model_name='customer',
            name='risk_preference',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='\u5ba2\u6237\u98ce\u9669\u504f\u597d', choices=[(b'1', '1-\u975e\u5e38\u4fdd\u5b88'), (b'2', '2-\u4fdd\u5b88'), (b'3', '3-\u6bd4\u8f83\u4fdd\u5b88'), (b'4', '4-\u6bd4\u8f83\u6fc0\u8fdb'), (b'5', '5-\u6fc0\u8fdb'), (b'6', '6-\u975e\u5e38\u6fc0\u8fdb')]),
        ),
        migrations.AlterField(
            model_name='customer_pending',
            name='risk_preference',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='\u5ba2\u6237\u98ce\u9669\u504f\u597d', choices=[(b'1', '1-\u975e\u5e38\u4fdd\u5b88'), (b'2', '2-\u4fdd\u5b88'), (b'3', '3-\u6bd4\u8f83\u4fdd\u5b88'), (b'4', '4-\u6bd4\u8f83\u6fc0\u8fdb'), (b'5', '5-\u6fc0\u8fdb'), (b'6', '6-\u975e\u5e38\u6fc0\u8fdb')]),
        ),
        migrations.AddField(
            model_name='real_purchase',
            name='customer',
            field=models.ForeignKey(verbose_name='\u771f\u5b9e\u5ba2\u6237\u59d3\u540d', blank=True, to='erp.Customer', null=True),
        ),
        migrations.AddField(
            model_name='real_purchase',
            name='customer_pend',
            field=models.ForeignKey(verbose_name='\u610f\u5411\u5ba2\u6237\u59d3\u540d', blank=True, to='erp.Customer_Pending', null=True),
        ),
        migrations.AddField(
            model_name='real_purchase',
            name='product',
            field=models.ForeignKey(verbose_name='\u4ea7\u54c1', to='erp.Product'),
        ),
        migrations.AddField(
            model_name='real_purchase',
            name='real_agent',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u7406\u8d22\u5e08', to='erp.Agent'),
        ),
    ]
