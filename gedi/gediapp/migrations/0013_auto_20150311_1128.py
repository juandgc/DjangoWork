# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gediapp', '0012_auto_20150311_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='ciudad',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articulo',
            name='idioma',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articulo',
            name='medio_divulgacion',
            field=models.CharField(default=b'P', max_length=100, choices=[(b'P', b'Papel'), (b'E', b'Electronico')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articulo',
            name='mes',
            field=models.IntegerField(default=1, max_length=100, choices=[(1, b'Enero'), (2, b'Febrero'), (3, b'Marzo'), (4, b'Abril'), (5, b'Mayo'), (6, b'Junio'), (7, b'Julio'), (8, b'Agosto'), (9, b'Septiembre'), (10, b'Octubre'), (11, b'Noviembre'), (12, b'Diciembre')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articulo',
            name='pais',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articulo',
            name='tipo_articulo',
            field=models.CharField(default=b'COM', max_length=100, choices=[(b'COM', b'Completo'), (b'COR', b'Corto'), (b'RE', b'Revision'), (b'CC', b'Caso Clinico')]),
            preserve_default=True,
        ),
    ]
