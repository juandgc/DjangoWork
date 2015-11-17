# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gediapp', '0027_auto_20151026_1807'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('titulo_libro', models.TextField()),
                ('pais', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('anio', models.IntegerField()),
                ('idioma', models.CharField(max_length=100)),
                ('ISBN', models.CharField(max_length=100)),
                ('volumen', models.IntegerField()),
                ('paginas', models.IntegerField()),
                ('editorial', models.CharField(max_length=100)),
                ('mes', models.IntegerField(choices=[(1, 'Enero'), (2, 'Febrero'), (3, 'Marzo'), (4, 'Abril'), (5, 'Mayo'), (6, 'Junio'), (7, 'Julio'), (8, 'Agosto'), (9, 'Septiembre'), (10, 'Octubre'), (11, 'Noviembre'), (12, 'Diciembre')], default=1)),
                ('activo', models.BooleanField(default=True)),
                ('autores', models.ManyToManyField(to='gediapp.Integrante')),
            ],
        ),
    ]
