# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gediapp', '0020_auto_20150407_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='softwares',
            name='descripcion',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='integrante',
            name='fecha_fin_vin',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
