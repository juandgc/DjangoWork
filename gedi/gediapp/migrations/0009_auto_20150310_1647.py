# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gediapp', '0008_auto_20150310_1645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trabajosdirigidos',
            name='autores',
        ),
        migrations.RemoveField(
            model_name='trabajosdirigidos',
            name='director',
        ),
    ]
