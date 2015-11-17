# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gediapp', '0015_integrante_activo'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='activo',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
