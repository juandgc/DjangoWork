# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gediapp', '0002_auto_20150303_1846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='softwares',
            name='autores',
        ),
    ]
