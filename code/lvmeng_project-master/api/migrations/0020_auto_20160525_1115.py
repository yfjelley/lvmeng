# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20160525_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verificationcode',
            name='purpose',
            field=models.CharField(blank=True, max_length=18, null=True, verbose_name='\u7528\u9014', choices=[(b'0', '\u6ce8\u518c\u9a8c\u8bc1'), (b'1', '\u4fee\u6539\u5bc6\u7801'), (b'2', '\u4fe1\u606f\u4fee\u6539')]),
        ),
    ]
