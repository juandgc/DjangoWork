# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gediapp', '0019_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='integrante',
            name='actual',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='integrante',
            name='fecha_fin_vin',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
    ]
