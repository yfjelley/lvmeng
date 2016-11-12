# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oa', '0027_auto_20160401_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_to_do',
            name='to_do_time',
            field=models.DateTimeField(verbose_name='\u5f85\u529e\u4e8b\u65f6\u95f4'),
        ),
    ]
