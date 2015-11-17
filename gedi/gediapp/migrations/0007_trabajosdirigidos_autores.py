# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gediapp', '0006_remove_trabajosdirigidos_autores'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajosdirigidos',
            name='autores',
            field=models.CharField(default='ninguno', max_length=100),
            preserve_default=False,
        ),
    ]
