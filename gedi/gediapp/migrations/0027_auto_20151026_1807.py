# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gediapp', '0026_auto_20151026_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='medio_divulgacion',
            field=models.CharField(choices=[('P', 'Papel'), ('E', 'Electrónico')], max_length=100, default='P'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='mes',
            field=models.IntegerField(choices=[(1, 'Enero'), (2, 'Febrero'), (3, 'Marzo'), (4, 'Abril'), (5, 'Mayo'), (6, 'Junio'), (7, 'Julio'), (8, 'Agosto'), (9, 'Septiembre'), (10, 'Octubre'), (11, 'Noviembre'), (12, 'Diciembre')], default=1),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='tipo_articulo',
            field=models.CharField(choices=[('COM', 'Completo'), ('COR', 'Corto'), ('RE', 'Revisión'), ('CC', 'Caso clínico')], max_length=100, default='COM'),
        ),
        migrations.AlterField(
            model_name='capituloslibros',
            name='mes_presentacion',
            field=models.IntegerField(choices=[(1, 'Enero'), (2, 'Febrero'), (3, 'Marzo'), (4, 'Abril'), (5, 'Mayo'), (6, 'Junio'), (7, 'Julio'), (8, 'Agosto'), (9, 'Septiembre'), (10, 'Octubre'), (11, 'Noviembre'), (12, 'Diciembre')], default=1),
        ),
        migrations.AlterField(
            model_name='softwares',
            name='disponibilidad',
            field=models.CharField(choices=[('Restringido', 'Restringido'), ('No Restringido', 'No Restringido')], max_length=100, default='Restringido'),
        ),
        migrations.AlterField(
            model_name='softwares',
            name='tipo',
            field=models.CharField(choices=[('Computacional', 'Computacional'), ('Multimedia', 'Multimedia'), ('Otro', 'Otro')], max_length=100, default='Computacional'),
        ),
        migrations.AlterField(
            model_name='trabajosdirigidos',
            name='tipo',
            field=models.CharField(choices=[('Trabajo de grado de maestria o especialidad medica', 'Trabajo de grado de maestria o especialidad medica'), ('Tesis de doctorado', 'Tesis de doctorado'), ('Monografia de conclusion de curso de perfeccionamiento / especializacion', 'Monografia de conclusion de curso de perfeccionamiento / especializacion'), ('Trabajo de conclusion de curso de pregrado', 'Trabajo de conclusion de curso de pregrado'), ('Iniciacion cientifica', 'Iniciacion cientifica'), ('Trabajos dirigidos / Tutorias de otro tipo', 'Trabajos dirigidos / Tutorias de otro tipo')], max_length=100, default='Trabajo de conclusion de curso de pregrado'),
        ),
        migrations.AlterField(
            model_name='trabajosdirigidos',
            name='tipo_orientacion',
            field=models.CharField(choices=[('Tutor principal', 'Tutor principal'), ('Cotutor/asesor', ' Cotutor/asesor'), ('Asesor de orientacion', 'Asesor de orientacion')], max_length=100, default='Tutor principal'),
        ),
        migrations.AlterField(
            model_name='trabajosdirigidos',
            name='valoracion',
            field=models.CharField(choices=[('Aprobada', 'Aprobada'), ('Distincion meritoria', 'Distincion meritoria'), ('Distincion laureada', 'Distincion laureada')], max_length=100, default='Aprobada'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='foto',
            field=models.ImageField(upload_to='fotos_usuarios', blank=True),
        ),
    ]
