# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gediapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='autores',
            field=models.ManyToManyField(to='gediapp.Integrante'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='trabajosdirigidos',
            name='director',
            field=models.ForeignKey(default='0', to='gediapp.Integrante'),
            preserve_default=False,
        ),
    ]
