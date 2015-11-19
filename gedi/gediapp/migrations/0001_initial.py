# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_articulo', models.CharField(default='COM', max_length=100, choices=[('COM', 'Completo'), ('COR', 'Corto'), ('RE', 'Revisión'), ('CC', 'Caso clínico')])),
                ('titulo_articulo', models.TextField()),
                ('pagina_inicial', models.IntegerField()),
                ('pagina_final', models.IntegerField()),
                ('idioma', models.CharField(max_length=100)),
                ('anio', models.IntegerField()),
                ('mes', models.IntegerField(default=1, choices=[(1, 'Enero'), (2, 'Febrero'), (3, 'Marzo'), (4, 'Abril'), (5, 'Mayo'), (6, 'Junio'), (7, 'Julio'), (8, 'Agosto'), (9, 'Septiembre'), (10, 'Octubre'), (11, 'Noviembre'), (12, 'Diciembre')])),
                ('revista', models.CharField(max_length=100)),
                ('volumen', models.IntegerField()),
                ('fasciculo', models.CharField(max_length=20)),
                ('serie_revista', models.CharField(max_length=30)),
                ('pais', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('medio_divulgacion', models.CharField(default='P', max_length=100, choices=[('P', 'Papel'), ('E', 'Electrónico')])),
                ('sitio_web', models.URLField(max_length=100)),
                ('DOI', models.CharField(max_length=50)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='CapitulosLibros',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo_capitulo_libro', models.CharField(max_length=200)),
                ('titulo_libro', models.CharField(max_length=200)),
                ('ISBN_libro', models.CharField(max_length=100)),
                ('anio_presentacion', models.IntegerField()),
                ('mes_presentacion', models.IntegerField(default=1, choices=[(1, 'Enero'), (2, 'Febrero'), (3, 'Marzo'), (4, 'Abril'), (5, 'Mayo'), (6, 'Junio'), (7, 'Julio'), (8, 'Agosto'), (9, 'Septiembre'), (10, 'Octubre'), (11, 'Noviembre'), (12, 'Diciembre')])),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Integrante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('horas_dedicacion', models.IntegerField(default=0)),
                ('fecha_inicio_vin', models.DateField()),
                ('fecha_fin_vin', models.DateField(blank=True, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('actual', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo_libro', models.TextField()),
                ('pais', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('anio', models.IntegerField()),
                ('idioma', models.CharField(max_length=100)),
                ('ISBN', models.CharField(max_length=100)),
                ('volumen', models.IntegerField()),
                ('paginas', models.IntegerField()),
                ('editorial', models.CharField(max_length=100)),
                ('mes', models.IntegerField(default=1, choices=[(1, 'Enero'), (2, 'Febrero'), (3, 'Marzo'), (4, 'Abril'), (5, 'Mayo'), (6, 'Junio'), (7, 'Julio'), (8, 'Agosto'), (9, 'Septiembre'), (10, 'Octubre'), (11, 'Noviembre'), (12, 'Diciembre')])),
                ('activo', models.BooleanField(default=True)),
                ('autores', models.ManyToManyField(to='gediapp.Integrante')),
            ],
        ),
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo_noticia', models.TextField()),
                ('descripcion', models.TextField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField(null=True)),
                ('pic', models.ImageField(upload_to='news/', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Softwares',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(default='Computacional', max_length=100, choices=[('Computacional', 'Computacional'), ('Multimedia', 'Multimedia'), ('Otro', 'Otro')])),
                ('nombre', models.CharField(max_length=250)),
                ('pais', models.CharField(max_length=100)),
                ('year', models.IntegerField(default=0)),
                ('disponibilidad', models.CharField(default='Restringido', max_length=100, choices=[('Restringido', 'Restringido'), ('No Restringido', 'No Restringido')])),
                ('web', models.URLField(max_length=100)),
                ('nombre_comercial', models.CharField(max_length=100)),
                ('nombre_proyecto', models.CharField(max_length=250)),
                ('institucion_financiadora', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('activo', models.BooleanField(default=True)),
                ('autores', models.ManyToManyField(to='gediapp.Integrante')),
            ],
        ),
        migrations.CreateModel(
            name='TrabajosDirigidos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(default='Trabajo de conclusion de curso de pregrado', max_length=100, choices=[('Trabajo de grado de maestria o especialidad medica', 'Trabajo de grado de maestria o especialidad medica'), ('Tesis de doctorado', 'Tesis de doctorado'), ('Monografia de conclusion de curso de perfeccionamiento / especializacion', 'Monografia de conclusion de curso de perfeccionamiento / especializacion'), ('Trabajo de conclusion de curso de pregrado', 'Trabajo de conclusion de curso de pregrado'), ('Iniciacion cientifica', 'Iniciacion cientifica'), ('Trabajos dirigidos / Tutorias de otro tipo', 'Trabajos dirigidos / Tutorias de otro tipo')])),
                ('nombre', models.CharField(max_length=250)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('tipo_orientacion', models.CharField(default='Tutor principal', max_length=100, choices=[('Tutor principal', 'Tutor principal'), ('Cotutor/asesor', ' Cotutor/asesor'), ('Asesor de orientacion', 'Asesor de orientacion')])),
                ('nombre_estudiante', models.CharField(max_length=100)),
                ('programa_academico', models.CharField(max_length=100)),
                ('numero_paginas', models.IntegerField(default=0)),
                ('valoracion', models.CharField(default='Aprobada', max_length=100, choices=[('Aprobada', 'Aprobada'), ('Distincion meritoria', 'Distincion meritoria'), ('Distincion laureada', 'Distincion laureada')])),
                ('institucion', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
                ('autores', models.ManyToManyField(to='gediapp.Integrante')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('foto', models.ImageField(blank=True, upload_to='fotos_usuarios')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='capituloslibros',
            name='autores',
            field=models.ManyToManyField(to='gediapp.Integrante'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='autores',
            field=models.ManyToManyField(to='gediapp.Integrante'),
        ),
    ]
