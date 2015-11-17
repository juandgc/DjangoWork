# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gediapp', '0021_auto_20150418_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='mes',
            field=models.IntegerField(default=1, choices=[(1, b'Enero'), (2, b'Febrero'), (3, b'Marzo'), (4, b'Abril'), (5, b'Mayo'), (6, b'Junio'), (7, b'Julio'), (8, b'Agosto'), (9, b'Septiembre'), (10, b'Octubre'), (11, b'Noviembre'), (12, b'Diciembre')]),
            preserve_default=True,
        ),
    ]
