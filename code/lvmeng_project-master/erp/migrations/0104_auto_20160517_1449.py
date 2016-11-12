# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0103_auto_20160516_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='order',
            field=models.PositiveIntegerField(verbose_name='\u987a\u5e8f(\u6570\u5b57\u5c0f\u7684\u6392\u5728\u524d\u9762\uff0c\u5927\u4e8e1\u7684\u6570\u5b57)'),
        ),
    ]
