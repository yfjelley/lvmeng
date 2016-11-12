# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0012_employee_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='email',
            field=models.EmailField(default=1, max_length=254, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='business',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x9c\x89\xe6\x95\x88'),
        ),
        migrations.AddField(
            model_name='role',
            name='business',
            field=models.ForeignKey(default=1, to='erp.Business'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='business',
            name='register_date',
            field=models.DateField(null=True, verbose_name=b'\xe6\xb3\xa8\xe5\x86\x8c\xe6\x97\xa5\xe6\x9c\x9f', blank=True),
        ),
    ]
