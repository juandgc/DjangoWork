# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gediapp', '0011_auto_20150311_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='sitio_web',
            field=models.URLField(max_length=100),
            preserve_default=True,
        ),
    ]
