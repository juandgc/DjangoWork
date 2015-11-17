# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gediapp', '0017_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajosdirigidos',
            name='tipo',
            field=models.CharField(default=b'Trabajo de conclusion de curso de pregrado', max_length=100, choices=[(b'Trabajo de grado de maestria o especialidad medica', b'Trabajo de grado de maestria o especialidad medica'), (b'Tesis de doctorado', b'Tesis de doctorado'), (b'Monografia de conclusion de curso de perfeccionamiento / especializacion', b'Monografia de conclusion de curso de perfeccionamiento / especializacion'), (b'Trabajo de conclusion de curso de pregrado', b'Trabajo de conclusion de curso de pregrado'), (b'Iniciacion cientifica', b'Iniciacion cientifica'), (b'Trabajos dirigidos / Tutorias de otro tipo', b'Trabajos dirigidos / Tutorias de otro tipo')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trabajosdirigidos',
            name='tipo_orientacion',
            field=models.CharField(default=b'Tutor principal', max_length=100, choices=[(b'Tutor principal', b'Tutor principal'), (b'Cotutor/asesor', b' Cotutor/asesor'), (b'Asesor de orientacion', b'Asesor de orientacion')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trabajosdirigidos',
            name='valoracion',
            field=models.CharField(default=b'Aprobada', max_length=100, choices=[(b'Aprobada', b'Aprobada'), (b'Distincion meritoria', b'Distincion meritoria'), (b'Distincion laureada', b'Distincion laureada')]),
            preserve_default=True,
        ),
    ]
