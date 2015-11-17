# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_articulo', models.CharField(default=b'COM', max_length=2, choices=[(b'COM', b'Completo'), (b'COR', b'Corto'), (b'RE', b'Revision'), (b'CC', b'Caso Clinico')])),
                ('titulo_articulo', models.TextField()),
                ('pagina_inicial', models.IntegerField()),
                ('pagina_final', models.IntegerField()),
                ('idioma', models.CharField(max_length=20)),
                ('anio', models.IntegerField()),
                ('mes', models.IntegerField()),
                ('revista', models.CharField(max_length=100)),
                ('volumen', models.IntegerField()),
                ('fasciculo', models.CharField(max_length=20)),
                ('serie_revista', models.CharField(max_length=30)),
                ('pais', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('medio_divulgacion', models.CharField(default=b'P', max_length=1, choices=[(b'P', b'Papel'), (b'E', b'Electronico')])),
                ('sitio_web', models.URLField()),
                ('DOI', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Integrante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('horas_dedicacion', models.IntegerField(default=0)),
                ('fecha_inicio_vin', models.DateField()),
                ('fecha_fin_vin', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Softwares',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=250)),
                ('pais', models.CharField(max_length=100)),
                ('year', models.IntegerField(default=0)),
                ('disponibilidad', models.CharField(max_length=100)),
                ('web', models.URLField()),
                ('nombre_comercial', models.CharField(max_length=100)),
                ('nombre_proyecto', models.CharField(max_length=250)),
                ('institucion_financiadora', models.CharField(max_length=100)),
                ('autores', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TrabajosDirigidos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=250)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('tipo_orientacion', models.CharField(max_length=100)),
                ('nombre_estudiante', models.CharField(max_length=100)),
                ('programa_academico', models.CharField(max_length=100)),
                ('numero_paginas', models.IntegerField(default=0)),
                ('valoracion', models.CharField(max_length=100)),
                ('institucion', models.CharField(max_length=100)),
                ('autores', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
