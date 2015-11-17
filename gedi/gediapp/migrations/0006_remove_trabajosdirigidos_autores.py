# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gediapp', '0005_auto_20150305_1027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trabajosdirigidos',
            name='autores',
        ),
    ]
