# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0092_auto_20160429_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name=b'cropping',
            field=image_cropping.fields.ImageRatioField(b'picture', '430x360', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='cropping'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='picture',
            field=models.ImageField(upload_to=b'business/pictures/', null=True, verbose_name='\u673a\u6784\u516c\u544a\u56fe\u7247(\u5c3a\u5bf8\u5927\u5c0f:375*106)', blank=True),
        ),
    ]
