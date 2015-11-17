# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gediapp', '0014_auto_20150312_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='integrante',
            name='activo',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
