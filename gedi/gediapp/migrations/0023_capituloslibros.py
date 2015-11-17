# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gediapp', '0022_auto_20150423_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='CapitulosLibros',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo_capitulo_libro', models.CharField(max_length=200)),
                ('titulo_libro', models.CharField(max_length=200)),
                ('ISBN_libro', models.CharField(max_length=100)),
                ('anio_presentacion', models.IntegerField()),
                ('mes_presentacion', models.IntegerField(default=1, choices=[(1, b'Enero'), (2, b'Febrero'), (3, b'Marzo'), (4, b'Abril'), (5, b'Mayo'), (6, b'Junio'), (7, b'Julio'), (8, b'Agosto'), (9, b'Septiembre'), (10, b'Octubre'), (11, b'Noviembre'), (12, b'Diciembre')])),
                ('certificado_entidad', models.TextField()),
                ('activo', models.BooleanField(default=True)),
                ('integrante', models.ManyToManyField(to='gediapp.Integrante')),
            ],
        ),
    ]
