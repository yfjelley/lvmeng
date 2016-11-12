# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agent_api', '0002_agent_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cell_records_customer',
            name='agent',
            field=models.ForeignKey(verbose_name='\u5ba2\u6237\u7ecf\u7406', to='erp.Agent'),
        ),
        migrations.AlterField(
            model_name='cell_records_pcustomer',
            name='agent',
            field=models.ForeignKey(verbose_name='\u5ba2\u6237\u7ecf\u7406', to='erp.Agent'),
        ),
    ]
