# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_emailcode_emailvalidsecond'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verificationcode',
            name='purpose',
            field=models.CharField(blank=True, max_length=18, null=True, verbose_name='\u7528\u9014', choices=[(b'0', '\u6ce8\u518c\u9a8c\u8bc1'), (b'1', '\u8eab\u4efd\u9a8c\u8bc1')]),
        ),
    ]
