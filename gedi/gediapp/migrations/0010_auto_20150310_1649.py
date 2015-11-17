# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gediapp', '0009_auto_20150310_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajosdirigidos',
            name='autores',
            field=models.ManyToManyField(to='gediapp.Integrante'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='trabajosdirigidos',
            name='director',
            field=models.CharField(default='ninguno', max_length=100),
            preserve_default=False,
        ),
    ]
