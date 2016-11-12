# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0072_auto_20160422_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='agent_num',
            field=models.CharField(unique=True, max_length=20, verbose_name='\u5458\u5de5\u7f16\u53f7(\u673a\u6784\u7f16\u53f7+\u5458\u5de5\u7f16\u53f7\u4e3a\u9080\u8bf7\u7801)'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='email',
            field=models.EmailField(default=166838092, max_length=30, verbose_name='\u90ae\u7bb1'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='agents',
            field=models.ManyToManyField(to='erp.Agent', null=True, verbose_name='\u6240\u5c5e\u5458\u5de5', blank=True),
        ),
        migrations.AlterField(
            model_name='customer_pending',
            name='agents',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u5458\u5de5', blank=True, to='erp.Agent', null=True),
        ),
        migrations.AlterField(
            model_name='real_purchase',
            name='real_agent',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u5458\u5de5', to='erp.Agent'),
        ),
    ]
