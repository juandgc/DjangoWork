# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gediapp', '0013_auto_20150311_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='medio_divulgacion',
            field=models.CharField(default=b'P', max_length=100, choices=[(b'P', b'Papel'), (b'E', b'Electr\xc3\xb3nico')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articulo',
            name='tipo_articulo',
            field=models.CharField(default=b'COM', max_length=100, choices=[(b'COM', b'Completo'), (b'COR', b'Corto'), (b'RE', b'Revisi\xc3\xb3n'), (b'CC', b'Caso cl\xc3\xadnico')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='softwares',
            name='disponibilidad',
            field=models.CharField(default=b'Restringido', max_length=100, choices=[(b'Restringido', b'Restringido'), (b'No Restringido', b'No Restringido')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='softwares',
            name='tipo',
            field=models.CharField(default=b'Computacional', max_length=100, choices=[(b'Computacional', b'Computacional'), (b'Multimedia', b'Multimedia'), (b'Otro', b'Otro')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trabajosdirigidos',
            name='tipo',
            field=models.CharField(default=b'Trabajo de conclusion de curso de pregrado', max_length=6, choices=[(b'Trabajo de grado de maestria o especialidad medica', b'Trabajo de grado de maestria o especialidad medica'), (b'Tesis de doctorado', b'Tesis de doctorado'), (b'Monografia de conclusion de curso de perfeccionamiento / especializacion', b'Monografia de conclusion de curso de perfeccionamiento / especializacion'), (b'Trabajo de conclusion de curso de pregrado', b'Trabajo de conclusion de curso de pregrado'), (b'Iniciacion cientifica', b'Iniciacion cientifica'), (b'Trabajos dirigidos / Tutorias de otro tipo', b'Trabajos dirigidos / Tutorias de otro tipo')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trabajosdirigidos',
            name='tipo_orientacion',
            field=models.CharField(default=b'Tutor principal', max_length=3, choices=[(b'Tutor principal', b'Tutor principal'), (b'Cotutor/asesor', b' Cotutor/asesor'), (b'Asesor de orientacion', b'Asesor de orientacion')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trabajosdirigidos',
            name='valoracion',
            field=models.CharField(default=b'Aprobada', max_length=3, choices=[(b'Aprobada', b'Aprobada'), (b'Distincion meritoria', b'Distincion meritoria'), (b'Distincion laureada', b'Distincion laureada')]),
            preserve_default=True,
        ),
    ]
