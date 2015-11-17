# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gediapp', '0003_remove_softwares_autores'),
    ]

    operations = [
        migrations.AddField(
            model_name='softwares',
            name='autores',
            field=models.ManyToManyField(to='gediapp.Integrante'),
            preserve_default=True,
        ),
    ]
