# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gediapp', '0010_auto_20150310_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='softwares',
            name='disponibilidad',
            field=models.CharField(default=b'RES', max_length=100, choices=[(b'RES', b'Restringido'), (b'NORES', b'No Restringido')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='softwares',
            name='tipo',
            field=models.CharField(default=b'COM', max_length=100, choices=[(b'COM', b'Computacional'), (b'MUL', b'Multimedia'), (b'OT', b'Otro')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='softwares',
            name='web',
            field=models.URLField(max_length=100),
            preserve_default=True,
        ),
    ]
