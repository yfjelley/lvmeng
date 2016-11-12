# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0089_auto_20160428_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='due_time',
            field=models.DateField(null=True, verbose_name='\u8d26\u6237\u5230\u671f\u65f6\u95f4', blank=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='idCard_negative',
            field=models.ImageField(upload_to=b'idCard/image', null=True, verbose_name='\u6cd5\u4eba\u8eab\u4efd\u8bc1\u53cd\u9762', blank=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='idCard_positive',
            field=models.ImageField(upload_to=b'idCard/image', null=True, verbose_name='\u6cd5\u4eba\u8eab\u4efd\u8bc1\u6b63\u9762', blank=True),
        ),
    ]
