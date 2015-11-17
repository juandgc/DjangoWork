# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gediapp', '0004_softwares_autores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='softwares',
            name='disponibilidad',
            field=models.CharField(default=b'RES', max_length=2, choices=[(b'RES', b'Restringido'), (b'NORES', b'No Restringido')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='softwares',
            name='tipo',
            field=models.CharField(default=b'COM', max_length=3, choices=[(b'COM', b'Computacional'), (b'MUL', b'Multimedia'), (b'OT', b'Otro')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trabajosdirigidos',
            name='tipo',
            field=models.CharField(default=b'CONPRE', max_length=6, choices=[(b'TMAS', b'Trabajo de grado de maestria o especialidad medica'), (b'TDOC', b'Tesis de doctorado'), (b'MON', b'Monografia de conclusion de curso de perfeccionamiento / especializacion'), (b'CONPRE', b'Trabajo de conclusion de curso de pregrado'), (b'INICI', b'Iniciacion cientifica'), (b'TUT', b'Trabajos dirigidos / Tutorias de otro tipo')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trabajosdirigidos',
            name='tipo_orientacion',
            field=models.CharField(default=b'TUT', max_length=3, choices=[(b'TUT', b'Tutor principal'), (b'COTUT', b' Cotutor/asesor'), (b'ASE', b'Asesor de orientacion')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trabajosdirigidos',
            name='valoracion',
            field=models.CharField(default=b'AP', max_length=3, choices=[(b'AP', b'Aprobada'), (b'MERI', b'Distincion meritoria'), (b'LAU', b'Distincion laureada')]),
            preserve_default=True,
        ),
    ]
