# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gediapp', '0023_capituloslibros'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='capituloslibros',
            name='certificado_entidad',
        ),
    ]
